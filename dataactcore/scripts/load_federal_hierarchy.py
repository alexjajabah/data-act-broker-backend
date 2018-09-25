import argparse
import asyncio
import csv
import json
import logging
import math
import pandas as pd
import requests
import shutil

from pandas.io.json import json_normalize
from requests.packages.urllib3.exceptions import ReadTimeoutError

from dataactcore.config import CONFIG_BROKER
from dataactcore.interfaces.db import GlobalDB
from dataactcore.logging import configure_logging
from dataactcore.models.domainModels import Office

from dataactvalidator.health_check import create_app

logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)

API_KEY = CONFIG_BROKER['sam']['federal_hierarchy_api_key']
API_URL = "https://api-alpha.sam.gov/prodlike/federalorganizations/v1/orgs?api_key={}".format(API_KEY)
REQUESTS_AT_ONCE = 10


def pull_offices(filename, update_db):
    """ Pull Office data from the Federal Hierarchy API
    
        Args:
            filename: Name of the file to be generated with the API data. If None, no file will be created.
            update_db: Boolean; update the DB tables with the new data from the API
    """
    sess = GlobalDB.db().session
    logger.info('Starting get feed: %s', API_URL.replace(API_KEY, "[API_KEY]"))

    if filename:
        # Write headers to file
        file_headers = [
            "fhorgid", "fhorgname", "fhorgtype", "description", "level", "status", "region", "categoryid",
            "effectivestartdate", "effectiveenddate", "createdby", "createddate", "updatedby", "lastupdateddate",
            "fhdeptindagencyorgid", "fhagencyorgname", "agencycode", "oldfpdsofficecode", "aacofficecode",
            "cgaclist_0_cgac", "fhorgofficetypelist_0_officetype", "fhorgofficetypelist_0_officetypestartdate",
            "fhorgofficetypelist_0_officetypeenddate", "fhorgofficetypelist_1_officetype",
            "fhorgofficetypelist_1_officetypestartdate", "fhorgofficetypelist_1_officetypeenddate",
            "fhorgofficetypelist_2_officetype", "fhorgofficetypelist_2_officetypestartdate",
            "fhorgofficetypelist_2_officetypeenddate", "fhorgaddresslist_0_city", "fhorgaddresslist_0_state",
            "fhorgaddresslist_0_country_code", "fhorgaddresslist_0_addresstype", "fhorgnamehistory_0_fhorgname",
            "fhorgnamehistory_0_effectivedate", "fhorgparenthistory_0_fhfullparentpathid",
            "fhorgparenthistory_0_fhfullparentpathname", "fhorgparenthistory_0_effectivedate", "links_0_href",
            "links_0_rel", "links_1_href", "links_1_rel", "links_2_href", "links_2_rel"]
        with open(filename, 'w+') as f:
            csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            csv_writer.writerow(file_headers)

    for level in ["3", "4", "5", "6", "7"]:
        # Create URL with the level param
        url_with_params = "{}&level={}".format(API_URL, level)

        # Retrieve the total count of expected records for this pull
        total_expected_records = json.loads(requests.get(url_with_params, timeout=60).text)['totalRecords']
        logger.info('{} record(s) expected from this feed'.format(total_expected_records))

        limit = 100
        entries_processed = 0
        while True:
            async def fed_hierarchy_async_get(entries_already_processed):
                response_list = []
                loop = asyncio.get_event_loop()
                futures = [
                    loop.run_in_executor(
                        None,
                        get_with_exception_hand,
                        "{}&limit={}&offset={}".format(url_with_params, str(limit),
                                                       str(entries_already_processed + (start_offset * limit)))
                    )
                    for start_offset in range(REQUESTS_AT_ONCE)
                ]
                for response in await asyncio.gather(*futures):
                    response_list.append(response.text)
                    pass
                return response_list
            # End async get requests def

            # Retrieve limit*REQUESTS_AT_ONCE records from the API
            logger.info("Retrieving rows %s-%s", str(entries_processed), str(entries_processed + limit * REQUESTS_AT_ONCE))
            loop = asyncio.get_event_loop()
            full_response = loop.run_until_complete(fed_hierarchy_async_get(entries_processed))

            # Create a dataframe with all the data from the API
            dataframe = pd.DataFrame()
            offices = []
            start = entries_processed + 1
            for next_resp in full_response:
                response_dict = json.loads(next_resp)

                for org in response_dict.get('orgList', []):
                    entries_processed += 1

                    # Add to the file data structure
                    if filename:
                        row = json_normalize(flatten_json(org))
                        dataframe = dataframe.append(row)

                    # Add to the list of DB objects
                    if update_db:
                        office_types = []
                        for office_type in org.get('fhorgofficetypelist', []):
                            office_types.append(office_type['officetype'].lower())
                        if org.get('aacofficecode'):
                            offices.append(Office(office_code=org.get('aacofficecode'),
                                                  office_name=org.get('fhorgname'),
                                                  sub_tier_code=org.get('agencycode'),
                                                  agency_code=org.get('cgaclist', [None])[0]))

            if filename:
                # Ensure headers are handled correctly
                df_length = len(dataframe.index)
                for header in list(dataframe.columns.values):
                    if header not in file_headers:
                        file_headers.append(header)
                        logger.info("Headers missing column: %s", header)

                # Write to file
                with open(filename, 'a') as f:
                    dataframe.to_csv(f, index=False, header=False, columns=file_headers)

            if update_db:
                sess.add_all(offices)

            logger.info("Processed rows %s-%s", start, entries_processed)

            if entries_processed < (start + limit * REQUESTS_AT_ONCE) or entries_processed > 1000:
                # Feed has finished
                # if entries_processed != total_expected_records:
                #     # Ensure we have retrieve the planned number of records
                #     raise Exception("Total expected records: {}, Number of records retrieved: {}".format(
                #         total_expected_records, entries_processed))
                break

    if update_db:
        sess.commit()

    logger.info("Finished")


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def get_with_exception_hand(url_string):
    """ Retrieve data from FPDS, allow for multiple retries and timeouts """
    exception_retries = -1
    retry_sleep_times = [5, 30, 60, 180, 300, 360, 420, 480, 540, 600]
    request_timeout = 60

    while exception_retries < len(retry_sleep_times):
        try:
            resp = requests.get(url_string, timeout=request_timeout)
            break
        except (ConnectionResetError, ReadTimeoutError, requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout) as e:
            exception_retries += 1
            request_timeout += 60
            if exception_retries < len(retry_sleep_times):
                logger.info('Connection exception. Sleeping {}s and then retrying with a max wait of {}s...'
                            .format(retry_sleep_times[exception_retries], request_timeout))
                time.sleep(retry_sleep_times[exception_retries])
            else:
                logger.info('Connection to FPDS feed lost, maximum retry attempts exceeded.')
                raise e
    return resp


def main():
    parser = argparse.ArgumentParser(description='Pull data from the Federal Hierarchy API.')
    parser.add_argument('-f', '--filename', help='Generate a local CSV file from the data.', nargs=1, type=str)
    parser.add_argument('-d', '--ignore_db', help='Do not update the DB tables', action='store_true')
    args = parser.parse_args()
    
    filename = args.filename[0] if args.filename else None
    if filename:
        logger.info("Creating a file ({}) with the data from this pull".format(filename))
    if not args.ignore_db:
        logger.info("Updating DB with the data from this pull")

    pull_offices(filename, not args.ignore_db)


if __name__ == '__main__':
    with create_app().app_context():
        configure_logging()
        main()

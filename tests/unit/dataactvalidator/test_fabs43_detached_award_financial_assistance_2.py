from tests.unit.dataactcore.factories.staging import DetachedAwardFinancialAssistanceFactory
from tests.unit.dataactvalidator.utils import number_of_errors, query_columns

_FILE = 'fabs43_detached_award_financial_assistance_2'


def test_column_headers(database):
    expected_subset = {"row_number", "place_of_performance_zip4a", "place_of_performance_congr",
                       "place_of_perform_country_c", "record_type"}
    actual = set(query_columns(_FILE, database))
    assert expected_subset == actual


def test_success(database):
    """ If no PrimaryPlaceOfPerformanceZIP+4 is provided, a PrimaryPlaceOfPerformanceCongressionalDistrict must
        be provided. Only applies to domestic records and aggregate or non-aggregate records (RecordType = 1 or 2). """

    det_award_1 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="",
                                                          place_of_performance_congr="01",
                                                          place_of_perform_country_c="USA",
                                                          record_type=1)
    det_award_2 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a=None,
                                                          place_of_performance_congr="01",
                                                          place_of_perform_country_c="USA",
                                                          record_type=2)
    det_award_3 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="123454321",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="usa",
                                                          record_type=1)
    det_award_4 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="123454321",
                                                          place_of_performance_congr=None,
                                                          place_of_perform_country_c="USA",
                                                          record_type=2)
    det_award_5 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="12345",
                                                          place_of_performance_congr="02",
                                                          place_of_perform_country_c="USA",
                                                          record_type=1)

    # Testing foreign places are ignored
    det_award_6 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="uK",
                                                          record_type=1)
    det_award_7 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="city-wide",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="uK",
                                                          record_type=2)

    # Testing record type 3 entries are ignored
    det_award_8 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="USA",
                                                          record_type=3)

    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4, det_award_5,
                                                       det_award_6, det_award_7, det_award_8])
    assert errors == 0


def test_failure(database):
    """ Test failure for if no PrimaryPlaceOfPerformanceZIP+4 is provided, a
        PrimaryPlaceOfPerformanceCongressionalDistrict must be provided. Only applies to domestic records
        and aggregate or non-aggregate records (RecordType = 1 or 2)."""

    det_award_1 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="USA",
                                                          record_type=1)
    det_award_2 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a=None,
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="UsA",
                                                          record_type=2)
    det_award_3 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="",
                                                          place_of_performance_congr=None,
                                                          place_of_perform_country_c="USA",
                                                          record_type=1)
    det_award_4 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a=None,
                                                          place_of_performance_congr=None,
                                                          place_of_perform_country_c="USA",
                                                          record_type=2)
    det_award_5 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a='city-wide',
                                                          place_of_performance_congr=None,
                                                          place_of_perform_country_c="USA",
                                                          record_type=1)
    det_award_6 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a='city-wide',
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="USA",
                                                          record_type=2)
    det_award_7 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="12345",
                                                          place_of_performance_congr="",
                                                          place_of_perform_country_c="usa",
                                                          record_type=1)
    det_award_8 = DetachedAwardFinancialAssistanceFactory(place_of_performance_zip4a="12345",
                                                          place_of_performance_congr=None,
                                                          place_of_perform_country_c="USA",
                                                          record_type=2)
    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4, det_award_5,
                                                       det_award_6, det_award_7, det_award_8])
    assert errors == 8

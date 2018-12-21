from collections import OrderedDict
from sqlalchemy import func, cast, Date

from dataactcore.models.stagingModels import DetachedAwardProcurement

file_model = DetachedAwardProcurement

mapping = OrderedDict([
    ('PIID', 'piid'),
    ('AwardModificationAmendmentNumber', 'award_modification_amendme'),
    ('Transaction Number', 'transaction_number'),
    ('Referenced IDV Agency Identifier', 'referenced_idv_agency_iden'),
    ('Referenced IDV Agency Name', 'referenced_idv_agency_desc'),
    ('ParentAwardId', 'parent_award_id'),
    ('Referenced IDV Modification Number', 'referenced_idv_modificatio'),
    ('FederalActionObligation', 'federal_action_obligation'),
    ('TotalDollarsObligated', 'total_obligated_amount'),
    ('BaseAndExercisedOptionsValue', 'base_exercised_options_val'),
    ('CurrentTotalValueOfAward', 'current_total_value_award'),
    ('BaseAndAllOptionsValue', 'base_and_all_options_value'),
    ('PotentialTotalValueOfAward', 'potential_total_value_awar'),
    ('ActionDate', 'action_date'),
    ('PeriodOfPerformanceStartDate', 'period_of_performance_star'),
    ('PeriodOfPerformanceCurrentEndDate', 'period_of_performance_curr'),
    ('PeriodOfPerformancePotentialEndDate', 'period_of_perf_potential_e'),
    ('OrderingPeriodEndDate', 'ordering_period_end_date'),
    ('AwardingAgencyCode', 'awarding_agency_code'),
    ('AwardingAgencyName', 'awarding_agency_name'),
    ('AwardingSubTierAgencyCode', 'awarding_sub_tier_agency_c'),
    ('AwardingSubTierAgencyName', 'awarding_sub_tier_agency_n'),
    ('AwardingOfficeCode', 'awarding_office_code'),
    ('AwardingOfficeName', 'awarding_office_name'),
    ('FundingAgencyCode', 'funding_agency_code'),
    ('FundingAgencyName', 'funding_agency_name'),
    ('FundingSubTierAgencyCode', 'funding_sub_tier_agency_co'),
    ('FundingSubTierAgencyName', 'funding_sub_tier_agency_na'),
    ('FundingOfficeCode', 'funding_office_code'),
    ('FundingOfficeName', 'funding_office_name'),
    ('Foreign Funding', 'foreign_funding'),
    ('Foreign Funding Description Tag', 'foreign_funding_desc'),
    ('SAM Exception', 'sam_exception'),
    ('SAM Exception Description Tag', 'sam_exception_description'),
    ('AwardeeOrRecipientUniqueIdentifier', 'awardee_or_recipient_uniqu'),
    ('AwardeeOrRecipientLegalEntityName', 'awardee_or_recipient_legal'),
    ('Vendor Doing As Business Name', 'vendor_doing_as_business_n'),
    ('CAGE Code', 'cage_code'),
    ('UltimateParentUniqueIdentifier', 'ultimate_parent_unique_ide'),
    ('UltimateParentLegalEntityName', 'ultimate_parent_legal_enti'),
    ('LegalEntityCountryCode', 'legal_entity_country_code'),
    ('LegalEntityCountryName', 'legal_entity_country_name'),
    ('LegalEntityAddressLine1', 'legal_entity_address_line1'),
    ('LegalEntityAddressLine2', 'legal_entity_address_line2'),
    ('LegalEntityCityName', 'legal_entity_city_name'),
    ('LegalEntityStateCode', 'legal_entity_state_code'),
    ('LegalEntityStateDescription', 'legal_entity_state_descrip'),
    ('LegalEntityZIP+4', 'legal_entity_zip4'),
    ('LegalEntityCongressionalDistrict', 'legal_entity_congressional'),
    ('Vendor Phone Number', 'vendor_phone_number'),
    ('Vendor Fax Number', 'vendor_fax_number'),
    ('PrimaryPlaceOfPerformanceCityName', 'place_of_perform_city_name'),
    ('PrimaryPlaceOfPerformanceCountyName', 'place_of_perform_county_na'),
    ('PrimaryPlaceOfPerformanceStateCode', 'place_of_performance_state'),
    ('PrimaryPlaceOfPerformanceStateName', 'place_of_perfor_state_desc'),
    ('PrimaryPlaceOfPerformanceZIP+4', 'place_of_performance_zip4a'),
    ('PrimaryPlaceOfPerformanceCongressionalDistrict', 'place_of_performance_congr'),
    ('PrimaryPlaceOfPerformanceCountryCode', 'place_of_perform_country_c'),
    ('PrimaryPlaceOfPerformanceCountryName', 'place_of_perf_country_desc'),
    ('Award Or IDV Flag', 'pulled_from'),
    ('ContractAwardType', 'contract_award_type'),
    ('ContractAwardTypeDescriptionTag', 'contract_award_type_desc'),
    ('IDV_Type', 'idv_type'),
    ('IDV_Type Description Tag', 'idv_type_description'),
    ('Multiple or Single Award IDV', 'multiple_or_single_award_i'),
    ('Multiple or Single Award IDV Description Tag', 'multiple_or_single_aw_desc'),
    ('Type of IDC', 'type_of_idc'),
    ('Type of IDC Description Tag', 'type_of_idc_description'),
    ('TypeOfContractPricing', 'type_of_contract_pricing'),
    ('TypeOfContractPricingDescriptionTag', 'type_of_contract_pric_desc'),
    ('AwardDescription', 'award_description'),
    ('ActionType', 'action_type'),
    ('ActionTypeDescriptionTag', 'action_type_description'),
    ('Solicitation Identifier', 'solicitation_identifier'),
    ('Number of Actions', 'number_of_actions'),
    ('Inherently Governmental Functions', 'inherently_government_func'),
    ('Inherently Governmental Functions Description Tag', 'inherently_government_desc'),
    ('Product or Service Code', 'product_or_service_code'),
    ('Product or Service Code Description Tag', 'product_or_service_co_desc'),
    ('Contract Bundling', 'contract_bundling'),
    ('Contract Bundling Description Tag', 'contract_bundling_descrip'),
    ('DoD Claimant Program Code', 'dod_claimant_program_code'),
    ('DoD Claimant Program Code Description Tag', 'dod_claimant_prog_cod_desc'),
    ('NAICS', 'naics'),
    ('NAICS_Description', 'naics_description'),
    ('Recovered Materials/Sustainability', 'recovered_materials_sustai'),
    ('Recovered Materials/Sustainability Description Tag', 'recovered_materials_s_desc'),
    ('Domestic or Foreign Entity', 'domestic_or_foreign_entity'),
    ('Domestic or Foreign Entity Description Tag', 'domestic_or_foreign_e_desc'),
    ('DOD Acquisition Program', 'program_system_or_equipmen'),
    ('DOD Acquisition Program Description Tag', 'program_system_or_equ_desc'),
    ('Information Technology Commercial Item Category', 'information_technology_com'),
    ('Information Technology Commercial Item Category Description Tag', 'information_technolog_desc'),
    ('EPA-Designated Product', 'epa_designated_product'),
    ('EPA-Designated Product Description Tag', 'epa_designated_produc_desc'),
    ('Country of Product or Service Origin', 'country_of_product_or_serv'),
    ('Country of Product or Service Origin Description Tag', 'country_of_product_or_desc'),
    ('Place of Manufacture', 'place_of_manufacture'),
    ('Place of Manufacture Description Tag', 'place_of_manufacture_desc'),
    ('Subcontracting Plan', 'subcontracting_plan'),
    ('Subcontracting Plan Description Tag', 'subcontracting_plan_desc'),
    ('Extent Competed', 'extent_competed'),
    ('Extent Competed Description Tag', 'extent_compete_description'),
    ('Solicitation Procedures', 'solicitation_procedures'),
    ('Solicitation Procedures Description Tag', 'solicitation_procedur_desc'),
    ('Type Set Aside', 'type_set_aside'),
    ('Type Set Aside Description Tag', 'type_set_aside_description'),
    ('Evaluated Preference', 'evaluated_preference'),
    ('Evaluated Preference Description Tag', 'evaluated_preference_desc'),
    ('Research', 'research'),
    ('Research Description Tag', 'research_description'),
    ('Fair Opportunity Limited Sources', 'fair_opportunity_limited_s'),
    ('Fair Opportunity Limited Sources Description Tag', 'fair_opportunity_limi_desc'),
    ('Other than Full and Open Competition', 'other_than_full_and_open_c'),
    ('Other than Full and Open Competition Description Tag', 'other_than_full_and_o_desc'),
    ('Number of Offers Received', 'number_of_offers_received'),
    ('Commercial Item Acquisition Procedures', 'commercial_item_acquisitio'),
    ('Commercial Item Acquisition Procedures Description Tag', 'commercial_item_acqui_desc'),
    ('Small Business Competitiveness Demonstration Program', 'small_business_competitive'),
    ('Commercial Item Test Program', 'commercial_item_test_progr'),
    ('Commercial Item Test Program Description Tag', 'commercial_item_test_desc'),
    ('A-76 FAIR Act Action', 'a_76_fair_act_action'),
    ('A-76 FAIR Act Action Description Tag', 'a_76_fair_act_action_desc'),
    ('FedBizOpps', 'fed_biz_opps'),
    ('FedBizOppsDescriptionTag', 'fed_biz_opps_description'),
    ('Local Area Set Aside', 'local_area_set_aside'),
    ('Local Area Set Aside Description Tag', 'local_area_set_aside_desc'),
    ('Price Evaluation Adjustment Preference Percent Difference', 'price_evaluation_adjustmen'),
    ('Clinger-Cohen Act Planning Compliance', 'clinger_cohen_act_planning'),
    ('Clinger-Cohen Act Planning Compliance Description Tag', 'clinger_cohen_act_pla_desc'),
    ('Materials, Supplies, Articles & Equip', 'materials_supplies_article'),
    ('Materials, Supplies, Articles & Equip Description Tag', 'materials_supplies_descrip'),
    ('Labor Standards', 'labor_standards'),
    ('Labor Standards Description Tag', 'labor_standards_descrip'),
    ('Construction Wage Rate Requirements', 'construction_wage_rate_req'),
    ('Construction Wage Rate Requirements Description Tag', 'construction_wage_rat_desc'),
    ('Interagency Contracting Authority', 'interagency_contracting_au'),
    ('Interagency Contracting Authority Description Tag', 'interagency_contract_desc'),
    ('Other Statutory Authority', 'other_statutory_authority'),
    ('Program Acronym', 'program_acronym'),
    ('Referenced IDV Type', 'referenced_idv_type'),
    ('Referenced IDV Type Description Tag', 'referenced_idv_type_desc'),
    ('Referenced IDV Multiple or Single', 'referenced_mult_or_single'),
    ('Referenced IDV Multiple or Single Description Tag', 'referenced_mult_or_si_desc'),
    ('Major program', 'major_program'),
    ('National Interest Action', 'national_interest_action'),
    ('National Interest Action Description Tag', 'national_interest_desc'),
    ('Cost or Pricing Data', 'cost_or_pricing_data'),
    ('Cost or Pricing Data Description Tag', 'cost_or_pricing_data_desc'),
    ('Cost Accounting Standards Clause', 'cost_accounting_standards'),
    ('Cost Accounting Standards Clause Description Tag', 'cost_accounting_stand_desc'),
    ('Government Furnished Property GFP', 'government_furnished_prope'),
    ('Government Furnished Property GFP Description Tag', 'government_furnished_desc'),
    ('Sea Transportation', 'sea_transportation'),
    ('Sea Transportation Description Tag', 'sea_transportation_desc'),
    ('Undefinitized Action', 'undefinitized_action'),
    ('Undefinitized Action Description Tag', 'undefinitized_action_desc'),
    ('Consolidated Contract', 'consolidated_contract'),
    ('Consolidated Contract Description Tag', 'consolidated_contract_desc'),
    ('Performance-Based Service Acquisition', 'performance_based_service'),
    ('Performance-Based Service Acquisition Description Tag', 'performance_based_se_desc'),
    ('Multi Year Contract', 'multi_year_contract'),
    ('Multi Year Contract Description Tag', 'multi_year_contract_desc'),
    ('Contract Financing', 'contract_financing'),
    ('Contract Financing Description Tag', 'contract_financing_descrip'),
    ('Purchase Card as Payment Method', 'purchase_card_as_payment_m'),
    ('Purchase Card as Payment Method Description Tag', 'purchase_card_as_paym_desc'),
    ('Contingency Humanitarian or Peacekeeping Operation', 'contingency_humanitarian_o'),
    ('Contingency Humanitarian or Peacekeeping Operation Description Tag', 'contingency_humanitar_desc'),
    ('Alaskan Native Owned Corporation or Firm', 'alaskan_native_owned_corpo'),
    ('American Indian Owned Business', 'american_indian_owned_busi'),
    ('Indian Tribe Federally Recognized', 'indian_tribe_federally_rec'),
    ('Native Hawaiian Owned Business', 'native_hawaiian_owned_busi'),
    ('Tribally Owned Business', 'tribally_owned_business'),
    ('Veteran Owned Business', 'veteran_owned_business'),
    ('Service Disabled Veteran Owned Business', 'service_disabled_veteran_o'),
    ('Woman Owned business', 'woman_owned_business'),
    ('Women Owned Small Business', 'women_owned_small_business'),
    ('Economically Disadvantaged Women Owned Small Business', 'economically_disadvantaged'),
    ('Joint Venture Women Owned Small Business', 'joint_venture_women_owned'),
    ('Joint Venture Economically Disadvantaged Women Owned Small Business', 'joint_venture_economically'),
    ('Minority Owned Business', 'minority_owned_business'),
    ('Subcontinent Asian Asian - Indian American Owned Business', 'subcontinent_asian_asian_i'),
    ('Asian Pacific American Owned Business', 'asian_pacific_american_own'),
    ('Black American Owned Business', 'black_american_owned_busin'),
    ('Hispanic American Owned Business', 'hispanic_american_owned_bu'),
    ('Native American Owned Business', 'native_american_owned_busi'),
    ('Other Minority Owned Business', 'other_minority_owned_busin'),
    ('Contracting Officer\'s Determination of Business Size', 'contracting_officers_deter'),
    ('Contracting Officer\'s Determination of Business Size Description Tag', 'contracting_officers_desc'),
    ('Emerging Small business', 'emerging_small_business'),
    ('Community Developed Corporation Owned Firm', 'community_developed_corpor'),
    ('Labor Surplus Area Firm', 'labor_surplus_area_firm'),
    ('U.S. Federal Government', 'us_federal_government'),
    ('Federally Funded Research and Development Corp', 'federally_funded_research'),
    ('Federal Agency', 'federal_agency'),
    ('U.S. State Government', 'us_state_government'),
    ('U.S. Local Government', 'us_local_government'),
    ('City Local Government', 'city_local_government'),
    ('County Local Government', 'county_local_government'),
    ('Inter-Municipal Local Government', 'inter_municipal_local_gove'),
    ('Local Government Owned', 'local_government_owned'),
    ('Municipality Local Government', 'municipality_local_governm'),
    ('School District Local Government', 'school_district_local_gove'),
    ('Township Local Government', 'township_local_government'),
    ('U.S. Tribal Government', 'us_tribal_government'),
    ('Foreign Government', 'foreign_government'),
    ('OrganizationalType', 'organizational_type'),
    ('Corporate Entity Not Tax Exempt', 'corporate_entity_not_tax_e'),
    ('Corporate Entity Tax Exempt', 'corporate_entity_tax_exemp'),
    ('Partnership or Limited Liability Partnership', 'partnership_or_limited_lia'),
    ('Sole Proprietorship', 'sole_proprietorship'),
    ('Small Agricultural Cooperative', 'small_agricultural_coopera'),
    ('International Organization', 'international_organization'),
    ('U.S. Government Entity', 'us_government_entity'),
    ('Community Development Corporation', 'community_development_corp'),
    ('Domestic Shelter', 'domestic_shelter'),
    ('Educational Institution', 'educational_institution'),
    ('Foundation', 'foundation'),
    ('Hospital Flag', 'hospital_flag'),
    ('Manufacturer of Goods', 'manufacturer_of_goods'),
    ('Veterinary Hospital', 'veterinary_hospital'),
    ('Hispanic Servicing Institution', 'hispanic_servicing_institu'),
    ('Contracts', 'contracts'),
    ('Grants', 'grants'),
    ('Receives Contracts and Grants', 'receives_contracts_and_gra'),
    ('Airport Authority', 'airport_authority'),
    ('Council of Governments', 'council_of_governments'),
    ('Housing Authorities Public/Tribal', 'housing_authorities_public'),
    ('Interstate Entity', 'interstate_entity'),
    ('Planning Commission', 'planning_commission'),
    ('Port Authority', 'port_authority'),
    ('Transit Authority', 'transit_authority'),
    ('Subchapter S Corporation', 'subchapter_s_corporation'),
    ('Limited Liability Corporation', 'limited_liability_corporat'),
    ('Foreign Owned and Located', 'foreign_owned_and_located'),
    ('For Profit Organization', 'for_profit_organization'),
    ('Nonprofit Organization', 'nonprofit_organization'),
    ('Other Not For Profit Organization', 'other_not_for_profit_organ'),
    ('The AbilityOne Program', 'the_ability_one_program'),
    ('NumberOfEmployees', 'number_of_employees'),
    ('AnnualRevenue', 'annual_revenue'),
    ('Private University or College', 'private_university_or_coll'),
    ('State Controlled Institution of Higher Learning', 'state_controlled_instituti'),
    ('1862 Land Grant College', 'c1862_land_grant_college'),
    ('1890 Land Grant College', 'c1890_land_grant_college'),
    ('1994 Land Grant College', 'c1994_land_grant_college'),
    ('Minority Institution', 'minority_institution'),
    ('Historically Black College or University', 'historically_black_college'),
    ('Tribal College', 'tribal_college'),
    ('Alaskan Native Servicing Institution', 'alaskan_native_servicing_i'),
    ('Native Hawaiian Servicing Institution', 'native_hawaiian_servicing'),
    ('School of Forestry', 'school_of_forestry'),
    ('Veterinary College', 'veterinary_college'),
    ('DoT Certified Disadvantaged Business Enterprise', 'dot_certified_disadvantage'),
    ('Self-Certified Small Disadvantaged Business', 'self_certified_small_disad'),
    ('Small Disadvantaged Business', 'small_disadvantaged_busine'),
    ('8a Program Participant', 'c8a_program_participant'),
    ('Historically Underutilized Business Zone HUBZone Firm', 'historically_underutilized'),
    ('SBA Certified 8 a Joint Venture', 'sba_certified_8_a_joint_ve'),
    ('LastModifiedDate', 'last_modified')
])
db_columns = [val for key, val in mapping.items()]


def query_data(session, agency_code, agency_type, start, end):
    """ Request D1 file data

        Args:
            session: DB session
            agency_code: FREC or CGAC code for generation
            agency_type: The type of agency (awarding or funding) to generate the file for
            start: Beginning of period for D file
            end: End of period for D file
            page_start: Beginning of pagination
            page_stop: End of pagination

        Returns:
            The rows using the provided dates and page size for the given agency.
    """
    rows = initial_query(session).\
        filter(func.cast_as_date(file_model.action_date) >= start).\
        filter(func.cast_as_date(file_model.action_date) <= end)

    # Funding or awarding agency filtering
    if agency_type == 'funding':
        rows = rows.filter(file_model.funding_agency_code == agency_code)
    else:
        rows = rows.filter(file_model.awarding_agency_code == agency_code)

    return rows


def initial_query(session):
    return session.query(*[
        file_model.piid,
        file_model.award_modification_amendme,
        file_model.transaction_number,
        file_model.referenced_idv_agency_iden,
        file_model.referenced_idv_agency_desc,
        file_model.parent_award_id,
        file_model.referenced_idv_modificatio,
        file_model.federal_action_obligation,
        file_model.total_obligated_amount,
        file_model.base_exercised_options_val,
        file_model.current_total_value_award,
        file_model.base_and_all_options_value,
        file_model.potential_total_value_awar,
        func.to_char(cast(file_model.action_date, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_performance_star, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_performance_curr, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_perf_potential_e, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.ordering_period_end_date, Date), 'YYYYMMDD'),
        file_model.awarding_agency_code,
        file_model.awarding_agency_name,
        file_model.awarding_sub_tier_agency_c,
        file_model.awarding_sub_tier_agency_n,
        file_model.awarding_office_code,
        file_model.awarding_office_name,
        file_model.funding_agency_code,
        file_model.funding_agency_name,
        file_model.funding_sub_tier_agency_co,
        file_model.funding_sub_tier_agency_na,
        file_model.funding_office_code,
        file_model.funding_office_name,
        file_model.foreign_funding,
        file_model.foreign_funding_desc,
        file_model.sam_exception,
        file_model.sam_exception_description,
        file_model.awardee_or_recipient_uniqu,
        file_model.awardee_or_recipient_legal,
        file_model.vendor_doing_as_business_n,
        file_model.cage_code,
        file_model.ultimate_parent_unique_ide,
        file_model.ultimate_parent_legal_enti,
        file_model.legal_entity_country_code,
        file_model.legal_entity_country_name,
        file_model.legal_entity_address_line1,
        file_model.legal_entity_address_line2,
        file_model.legal_entity_city_name,
        file_model.legal_entity_state_code,
        file_model.legal_entity_state_descrip,
        file_model.legal_entity_zip4,
        file_model.legal_entity_congressional,
        file_model.vendor_phone_number,
        file_model.vendor_fax_number,
        file_model.place_of_perform_city_name,
        file_model.place_of_perform_county_na,
        file_model.place_of_performance_state,
        file_model.place_of_perfor_state_desc,
        file_model.place_of_performance_zip4a,
        file_model.place_of_performance_congr,
        file_model.place_of_perform_country_c,
        file_model.place_of_perf_country_desc,
        file_model.pulled_from,
        file_model.contract_award_type,
        file_model.contract_award_type_desc,
        file_model.idv_type,
        file_model.idv_type_description,
        file_model.multiple_or_single_award_i,
        file_model.multiple_or_single_aw_desc,
        file_model.type_of_idc,
        file_model.type_of_idc_description,
        file_model.type_of_contract_pricing,
        file_model.type_of_contract_pric_desc,
        file_model.award_description,
        file_model.action_type,
        file_model.action_type_description,
        file_model.solicitation_identifier,
        file_model.number_of_actions,
        file_model.inherently_government_func,
        file_model.inherently_government_desc,
        file_model.product_or_service_code,
        file_model.product_or_service_co_desc,
        file_model.contract_bundling,
        file_model.contract_bundling_descrip,
        file_model.dod_claimant_program_code,
        file_model.dod_claimant_prog_cod_desc,
        file_model.naics,
        file_model.naics_description,
        file_model.recovered_materials_sustai,
        file_model.recovered_materials_s_desc,
        file_model.domestic_or_foreign_entity,
        file_model.domestic_or_foreign_e_desc,
        file_model.program_system_or_equipmen,
        file_model.program_system_or_equ_desc,
        file_model.information_technology_com,
        file_model.information_technolog_desc,
        file_model.epa_designated_product,
        file_model.epa_designated_produc_desc,
        file_model.country_of_product_or_serv,
        file_model.country_of_product_or_desc,
        file_model.place_of_manufacture,
        file_model.place_of_manufacture_desc,
        file_model.subcontracting_plan,
        file_model.subcontracting_plan_desc,
        file_model.extent_competed,
        file_model.extent_compete_description,
        file_model.solicitation_procedures,
        file_model.solicitation_procedur_desc,
        file_model.type_set_aside,
        file_model.type_set_aside_description,
        file_model.evaluated_preference,
        file_model.evaluated_preference_desc,
        file_model.research,
        file_model.research_description,
        file_model.fair_opportunity_limited_s,
        file_model.fair_opportunity_limi_desc,
        file_model.other_than_full_and_open_c,
        file_model.other_than_full_and_o_desc,
        file_model.number_of_offers_received,
        file_model.commercial_item_acquisitio,
        file_model.commercial_item_acqui_desc,
        file_model.small_business_competitive,
        file_model.commercial_item_test_progr,
        file_model.commercial_item_test_desc,
        file_model.a_76_fair_act_action,
        file_model.a_76_fair_act_action_desc,
        file_model.fed_biz_opps,
        file_model.fed_biz_opps_description,
        file_model.local_area_set_aside,
        file_model.local_area_set_aside_desc,
        file_model.price_evaluation_adjustmen,
        file_model.clinger_cohen_act_planning,
        file_model.clinger_cohen_act_pla_desc,
        file_model.materials_supplies_article,
        file_model.materials_supplies_descrip,
        file_model.labor_standards,
        file_model.labor_standards_descrip,
        file_model.construction_wage_rate_req,
        file_model.construction_wage_rat_desc,
        file_model.interagency_contracting_au,
        file_model.interagency_contract_desc,
        file_model.other_statutory_authority,
        file_model.program_acronym,
        file_model.referenced_idv_type,
        file_model.referenced_idv_type_desc,
        file_model.referenced_mult_or_single,
        file_model.referenced_mult_or_si_desc,
        file_model.major_program,
        file_model.national_interest_action,
        file_model.national_interest_desc,
        file_model.cost_or_pricing_data,
        file_model.cost_or_pricing_data_desc,
        file_model.cost_accounting_standards,
        file_model.cost_accounting_stand_desc,
        file_model.government_furnished_prope,
        file_model.government_furnished_desc,
        file_model.sea_transportation,
        file_model.sea_transportation_desc,
        file_model.undefinitized_action,
        file_model.undefinitized_action_desc,
        file_model.consolidated_contract,
        file_model.consolidated_contract_desc,
        file_model.performance_based_service,
        file_model.performance_based_se_desc,
        file_model.multi_year_contract,
        file_model.multi_year_contract_desc,
        file_model.contract_financing,
        file_model.contract_financing_descrip,
        file_model.purchase_card_as_payment_m,
        file_model.purchase_card_as_paym_desc,
        file_model.contingency_humanitarian_o,
        file_model.contingency_humanitar_desc,
        file_model.alaskan_native_owned_corpo,
        file_model.american_indian_owned_busi,
        file_model.indian_tribe_federally_rec,
        file_model.native_hawaiian_owned_busi,
        file_model.tribally_owned_business,
        file_model.veteran_owned_business,
        file_model.service_disabled_veteran_o,
        file_model.woman_owned_business,
        file_model.women_owned_small_business,
        file_model.economically_disadvantaged,
        file_model.joint_venture_women_owned,
        file_model.joint_venture_economically,
        file_model.minority_owned_business,
        file_model.subcontinent_asian_asian_i,
        file_model.asian_pacific_american_own,
        file_model.black_american_owned_busin,
        file_model.hispanic_american_owned_bu,
        file_model.native_american_owned_busi,
        file_model.other_minority_owned_busin,
        file_model.contracting_officers_deter,
        file_model.contracting_officers_desc,
        file_model.emerging_small_business,
        file_model.community_developed_corpor,
        file_model.labor_surplus_area_firm,
        file_model.us_federal_government,
        file_model.federally_funded_research,
        file_model.federal_agency,
        file_model.us_state_government,
        file_model.us_local_government,
        file_model.city_local_government,
        file_model.county_local_government,
        file_model.inter_municipal_local_gove,
        file_model.local_government_owned,
        file_model.municipality_local_governm,
        file_model.school_district_local_gove,
        file_model.township_local_government,
        file_model.us_tribal_government,
        file_model.foreign_government,
        file_model.organizational_type,
        file_model.corporate_entity_not_tax_e,
        file_model.corporate_entity_tax_exemp,
        file_model.partnership_or_limited_lia,
        file_model.sole_proprietorship,
        file_model.small_agricultural_coopera,
        file_model.international_organization,
        file_model.us_government_entity,
        file_model.community_development_corp,
        file_model.domestic_shelter,
        file_model.educational_institution,
        file_model.foundation,
        file_model.hospital_flag,
        file_model.manufacturer_of_goods,
        file_model.veterinary_hospital,
        file_model.hispanic_servicing_institu,
        file_model.contracts,
        file_model.grants,
        file_model.receives_contracts_and_gra,
        file_model.airport_authority,
        file_model.council_of_governments,
        file_model.housing_authorities_public,
        file_model.interstate_entity,
        file_model.planning_commission,
        file_model.port_authority,
        file_model.transit_authority,
        file_model.subchapter_s_corporation,
        file_model.limited_liability_corporat,
        file_model.foreign_owned_and_located,
        file_model.for_profit_organization,
        file_model.nonprofit_organization,
        file_model.other_not_for_profit_organ,
        file_model.the_ability_one_program,
        file_model.number_of_employees,
        file_model.annual_revenue,
        file_model.private_university_or_coll,
        file_model.state_controlled_instituti,
        file_model.c1862_land_grant_college,
        file_model.c1890_land_grant_college,
        file_model.c1994_land_grant_college,
        file_model.minority_institution,
        file_model.historically_black_college,
        file_model.tribal_college,
        file_model.alaskan_native_servicing_i,
        file_model.native_hawaiian_servicing,
        file_model.school_of_forestry,
        file_model.veterinary_college,
        file_model.dot_certified_disadvantage,
        file_model.self_certified_small_disad,
        file_model.small_disadvantaged_busine,
        file_model.c8a_program_participant,
        file_model.historically_underutilized,
        file_model.sba_certified_8_a_joint_ve,
        func.to_char(cast(file_model.last_modified, Date), 'YYYYMMDD')])

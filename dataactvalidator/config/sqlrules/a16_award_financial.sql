SELECT row_number,
	gross_outlay_amount_by_awa_fyb,
	gross_outlays_delivered_or_fyb,
	gross_outlays_undelivered_fyb,
	obligations_delivered_orde_fyb,
	obligations_undelivered_or_fyb
FROM award_financial
WHERE submission_id = {0}
	AND is_first_quarter = TRUE
	AND gross_outlay_amount_by_awa_fyb IS NOT DISTINCT FROM NULL
	AND gross_outlays_delivered_or_fyb IS NOT DISTINCT FROM NULL
	AND gross_outlays_undelivered_fyb IS NOT DISTINCT FROM NULL
	AND obligations_delivered_orde_fyb IS NOT DISTINCT FROM NULL
	AND obligations_undelivered_or_fyb IS NOT DISTINCT FROM NULL

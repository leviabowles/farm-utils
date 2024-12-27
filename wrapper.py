import land_evaluation
import statistics

farm = land_evaluation.land(crop_revenue_mu = 120, crop_revenue_sig = 30, crop_cogs_mu = 40, crop_cogs_sig = 10, crop_acres = 100)

farm.annual_profit()
farm.simple_valuator(irr = .03)

farm.prob_field_value()

farm.prob_multiyear_profit(years = 10)
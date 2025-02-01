import land_evaluation.land_evaluation as land_evaluation
import statistics

farm = land_evaluation.land(crop_revenue_mu = 120, crop_revenue_sig = 30, crop_cogs_mu = 40, crop_cogs_sig = 10, crop_acres = 100)
casino = land_evaluation.casino_carlo(farm,years = 10, iterations = 100)
z = casino.run_iterations()

farm.annual_profit()
farm.simple_valuator(irr = .03)

simulator = land_evaluation.land_simulator(farm,3)

simulator.prob_field_value()

profit, value, df = simulator.prob_multiyear_profit(years = 10)

simulator.multiyear_summary()
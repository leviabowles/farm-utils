import forecast
import pandas as pd
path = '/Users/levi.bowles/Downloads/wheat-prices-historical-chart-data.csv'

mod = forecast.commodity_forecast(path = path)

mod.monthitize()

mod.auto_arima()

mod.forecast_next(periods = 3)

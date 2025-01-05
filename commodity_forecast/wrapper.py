import forecast
import pandas as pd
path = '/Users/levi.bowles/Downloads/wheat-prices-historical-chart-data.csv'

mod = forecast.commodity_forecast(path = path)

mod.monthitize()

model = forecast.auto_arima(mod.df['price'])

forecast.forecast_next(model, mod.df['price'], periods = 12)

mod.roll_forward(24,1)

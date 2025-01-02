import forecast
path = '/Users/levi.bowles/Downloads/wheat-prices-historical-chart-data.csv'

mod = forecast.commodity_forecast(path = path)

mod.auto_arima()

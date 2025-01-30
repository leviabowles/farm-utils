import forecast
import pandas as pd
path = '/Users/levi.bowles/Downloads/wheat-prices-historical-chart-data.csv'

mod = forecast.commodity_forecast(path = path)

mod.monthitize()

model = forecast.auto_arima(mod.df['price'])

mod.roll_forward(24,1)

mod.back_test.model_slices(model)



i = 101
mod.back_test.predictions[i].name = 'fuck'
merged = pd.merge(mod.back_test.predictions[i], mod.back_test.slices_forward[i], left_index = True, right_index = True)

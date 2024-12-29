import pandas as pd
import pmdarima as pm

pd.

m12 = pm.auto_arima(train, error_action='ignore', seasonal=True, m=12)



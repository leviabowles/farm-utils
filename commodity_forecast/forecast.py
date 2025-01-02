import pmdarima as pm
import pandas as pd



class commodity_forecast:
    
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def auto_arima(self):
        self.aa = pm.auto_arima(self.df['price'], error_action='ignore', seasonal=True, m=12)



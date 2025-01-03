import pmdarima as pm
import pandas as pd



class commodity_forecast:
    
    def __init__(self, path):
        self.df = pd.read_csv(path)
        
    def monthitize(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['date'] = self.df['date'].dt.to_period('M')
        self.df = self.df.groupby(['date']).mean()

    def auto_arima(self):
        self.aa = pm.auto_arima(self.df['price'], error_action='ignore', seasonal=True, m=12)
        print(self.aa.params())
        
    def forecast_next(self, periods):
        pred = self.aa.fit_predict(y = self.df['price'],n_periods = periods)
        return(pred)
      
    def roll_forward(self, min_start, iter_width):
        self.eva =pd.DataFrame(columns=['iteration', 'forward_period', 'price', 'pred'])
        for i in range(min_start,len(self.df.index)):
            print(self.df.iloc[0:i+1,])
            print(self.df.iloc[i+1:i+13,])



import pmdarima as pm
import pandas as pd

def forecast_next(model, data, periods):
    pred = model.fit_predict(y = data,n_periods = periods)
    return(pred)

def auto_arima(data):
    
    aa = pm.auto_arima(data, error_action='ignore', seasonal=True, m=12)
    #print(aa.params())
    
    print(aa.summary())
    return(aa)
  
def model_wrapper(data, fit, verbose = False):
    
    model = pm.arima.ARIMA(order=fit.get_params().get("order")).fit(data)
    
    if verbose: 
      print(model.summary())
    
    return(model)

class back_test:
    
    def __init__(self, slices, slices_forward):
        
        self.slices = slices
        self.slices_forward = slices_forward
        
    def model_slices(self, model):
        
        self.predictions = {}
        
        for i in self.slices:
            inmod = model_wrapper(data = self.slices[i],fit = model)
            pred = forecast_next(inmod, self.slices[i], 12)
            self.predictions[i] = pred
            #print(inmod.summary)
            #print(pred)
            
        for j in self.predictions:
            self.predictions[i].name = "predicted"
            merged = pd.merge(self.predictions[i], self.slices_forward[i], left_index = True, right_index = True)
            self.predictions[i] = merged


class commodity_forecast:
    
    def __init__(self, path):
        self.df = pd.read_csv(path)
        
    def monthitize(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['date'] = self.df['date'].dt.to_period('M')
        self.df = self.df.groupby(['date']).mean()
        print('group by complete at month level')

    def roll_forward(self, min_start, iter_width):
        self.eva =pd.DataFrame(columns=['iteration', 'forward_period', 'price', 'pred'])
        slices = {}
        slices_forward = {}
        for i in range(min_start,len(self.df.index)):
            #print(self.df.iloc[0:i+1,])
            slices[i] = self.df.iloc[0:i+1,]
            #print(self.df.iloc[i+1:i+13,])
            slices_forward[i] = self.df.iloc[i+1:i+13,]
            
        self.back_test = back_test(slices = slices, slices_forward = slices_forward)
        return(self.back_test)


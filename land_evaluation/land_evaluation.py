import random 
import statistics

class land():
    def __init__(self,
                crop_revenue_mu,
                crop_revenue_sig,
                crop_cogs_mu,
                crop_cogs_sig,
                crop_acres = 80,
                field_paid = 250000,
                non_crop_revenue_mu = 0.0,
                non_crop_revenue_sig = 0.0,
                non_crop_cogs_mu = 0.0,
                non_crop_cogs_sig = 0.0,
                inflation_mu = 0.03, 
                inflation_sig = 0.01,
                inflation_land_mu = .05,
                inflation_land_sig = .03):
        self.crop_acres = crop_acres
        self.inflation_mean = inflation_mu
        self.inflation_sig = inflation_sig
        self.crop_revenue_mu = crop_revenue_mu
        self.crop_revenue_sig = crop_revenue_sig
        self.crop_cogs_mu = crop_cogs_mu
        self.crop_cogs_sig = crop_cogs_sig
        self.non_crop_revenue_mu = non_crop_revenue_mu
        self.non_crop_revenue_sig = non_crop_revenue_sig
        self.non_crop_cogs_mu = non_crop_cogs_mu
        self.non_crop_cogs_sig = non_crop_cogs_sig
        self.inflation_land_mu = inflation_land_mu
        self.inflation_land_sig = inflation_land_sig
        self.field_paid = field_paid
        self.pred_field_value = self.field_paid

    
    def annual_profit(self):
        profit = (self.crop_revenue_mu + self.non_crop_revenue_mu) - (self.crop_cogs_mu + self.non_crop_cogs_mu)
        profit = profit * self.crop_acres
        return(profit)
    
    def simple_valuator(self, irr):
        profit = self.annual_profit()
        max_value = profit/irr
        return(max_value)

class land_simulator(land):

    def __init__(self, current_land:land, id):
        self.id = id
        self.current_land = current_land
        

    def prob_profit(self):
        profit = ((random.normalvariate(mu = self.current_land.crop_revenue_mu, sigma = self.current_land.crop_revenue_sig) + 
                  random.normalvariate(mu = self.current_land.non_crop_revenue_mu, sigma = self.current_land.non_crop_revenue_sig)) -
                  ((random.normalvariate(mu = self.current_land.crop_cogs_mu, sigma = self.current_land.crop_cogs_sig) + 
                  random.normalvariate(mu = self.current_land.non_crop_cogs_mu, sigma = self.current_land.non_crop_cogs_sig))))
        profit = profit * self.current_land.crop_acres
        return(profit)
    

    def prob_field_value(self):
        self.current_land.pred_field_value = (self.current_land.pred_field_value + 
                                 self.current_land.pred_field_value * 
                                 random.normalvariate(mu = self.current_land.inflation_land_mu , sigma = self.current_land.inflation_land_sig ))
        
        return(self.current_land.pred_field_value)
    
    def prob_multiyear_profit(self, years = 20):

        x = []
        value = []
        self.current_land.pred_field_value = self.current_land.field_paid
        for i in range(years):
            x.append(self.prob_profit())
            value.append(self.prob_field_value())
        
        x.append(statistics.mean(x))
        value.append(statistics.mean(value))
        return(x, value)
        
        




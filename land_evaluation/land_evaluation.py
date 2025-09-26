import random 
import statistics
import pandas as pd

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

    
    def annual_profit(self, appreciation = False):
        '''
        TO DO: add method to account for annualized land inflation
        Simple method to evaluate annual profit based on crop sales.
        This is really a cash-flow methodology.
        Could add a switch to estimate central estimate of appreciation.
        '''
        profit = (self.crop_revenue_mu + self.non_crop_revenue_mu) - (self.crop_cogs_mu + self.non_crop_cogs_mu)
        profit = profit * self.crop_acres

        if appreciation:
            apprec = self.field_paid * self.inflation_land_mu
            profit = apprec + profit 

        return(profit)
    
    def simple_valuator(self, irr, appreciation = False):
        '''
        Valuation method working backwards from desired IRR
        '''

        profit = self.annual_profit(appreciation=appreciation)
        max_value = profit/irr
        return(max_value)

class land_simulator(land):

    def __init__(self, current_land:land, id):
        self.id = id
        self.current_land = current_land
        

    def prob_profit(self):
        '''
        TO DO: scale variance to grow profit over time
        This is a simulator that uses simple gaussian variance each year.
        I could have tore these apart a little more and may do that later. 
        '''
        profit = ((random.normalvariate(mu = self.current_land.crop_revenue_mu, sigma = self.current_land.crop_revenue_sig) + 
                  random.normalvariate(mu = self.current_land.non_crop_revenue_mu, sigma = self.current_land.non_crop_revenue_sig)) -
                  ((random.normalvariate(mu = self.current_land.crop_cogs_mu, sigma = self.current_land.crop_cogs_sig) + 
                  random.normalvariate(mu = self.current_land.non_crop_cogs_mu, sigma = self.current_land.non_crop_cogs_sig))))
        profit = profit * self.current_land.crop_acres
        return(profit)
    

    def prob_field_value(self):
        '''
        simple next-value-up estimator for data.
        '''
        
        self.current_land.pred_field_value = (self.current_land.pred_field_value + 
                                 self.current_land.pred_field_value * 
                                 random.normalvariate(mu = self.current_land.inflation_land_mu , sigma = self.current_land.inflation_land_sig ))
        
        return(self.current_land.pred_field_value)
    
    def prob_multiyear_profit(self, years = 20):
        '''
        Multi year simulator that iterates over years and calls annual simulation calls.
        '''
        x = []
        value = []
        self.current_land.pred_field_value = self.current_land.field_paid
        for i in range(years):
            x.append(self.prob_profit())
            value.append(self.prob_field_value())

        self.annual_df = pd.DataFrame({'year':range(years),
                           'profit':x,
                           'field_value':value})
        
        #x.append(statistics.mean(x))
        #value.append(statistics.mean(value))
        return(x, value, self.annual_df)
    
    def multiyear_summary(self):
        
        '''
        Takes annualized DF and aggregates, then runs profit calculations.
        '''

        try:
            self.annual_df
        except:
            print("Have not simulated profit yet try running prob_multiyear_profit()")

        field_appreciation = self.annual_df['field_value'].iloc[-1] - self.current_land.field_paid
        profit = self.annual_df['profit'].sum()
        total_returns = profit + field_appreciation

        ratio_return = (self.current_land.field_paid + total_returns)/self.current_land.field_paid
        years = len(self.annual_df.index)
        annualized_return = ratio_return ** (1/years)

        #print(field_appreciation)
        #print(profit)
        #print(field_appreciation + profit)
        return(annualized_return)
    

class casino_carlo:

    '''
    Need to add in graphing capabilities as well as a few other metrics
    '''

    def __init__(self, current_land:land, years = 10, iterations = 1000):
        self.years = years
        self.iterations = iterations
        self.current_land = current_land

    def run_iterations(self):
        
        returns_holder = []
        
        for i in range(self.iterations):
            simulator = land_simulator(current_land=self.current_land, id = i)
            simulator.prob_multiyear_profit(years = self.years)
            returns = simulator.multiyear_summary()
            returns_holder.append(returns)
        
        returns_holder = pd.Series(returns_holder)

        return(returns_holder)
        
        



    

        
        




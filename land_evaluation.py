class land():
    def __init__(self,
                crop_revenue_mu,
                crop_revenue_sig,
                crop_cogs_mu,
                crop_cogs_sig,
                crop_acres,
                non_crop_revenue_mu = 0.0,
                non_crop_revenue_sig = 0.0,
                non_crop_cogs_mu = 0.0,
                non_crop_cogs_sig = 0.0,
                inflation_mu = 3.0, 
                inflation_sig = 1.0):
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
    
    def annual_profit(self):
        profit = (self.crop_revenue_mu + self.non_crop_revenue_mu) - (self.crop_cogs_mu + self.non_crop_cogs_mu)
        profit = profit * self.crop_acres
        return(profit)
    
    def simple_valuator(self, irr):
        profit = self.annual_profit()
        max_value = profit/irr
        print(max_value)

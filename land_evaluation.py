class land():
    def __init__(self, 
                crop_revenue_mu,
                crop_revenue_sig,
                inflation_mu = 3.0, 
                inflation_sig = 1.0):
        self.inflation_mean = inflation_mu
        self.inflation_sig = inflation_sig
        self.crop_revenue_mu = crop_revenue_mu
        self.crop_revenue_sig = crop_revenue_sig
    
    def annual_evaluator(self):

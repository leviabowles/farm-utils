import torch 
import pandas as pd

def data_reader(file):
    '''
    A simple method to return a dataframe with the core training data from local flat file.
    '''
    df = pd.read_csv(file)
    return(df)


class ts_prep: 

    '''
    Beginner class to push data into time-series friendly format:
    1. Create lags prior to tensor creation.
    2. bring in correct covariates in latency windows
    3. Split into train/test by cut-date.
    '''

    def __init__(self, df, cut_date):
        self.df = df
        self.cut_date = cut_date


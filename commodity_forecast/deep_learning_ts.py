import torch 
import pandas as pd

def data_reader(file):
    '''
    A simple method to return a dataframe with the core training data from local flat file.
    '''
    df = pd.read_csv(file)
    return(df)
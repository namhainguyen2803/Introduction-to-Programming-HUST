import numpy as np
import pandas as pd

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('real_estate.csv', index_col='No')
        self.dataframe = df
    
    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        self.X = np.array(self.dataframe[self.dataframe.columns[:-1]])
        self.y = np.array(self.dataframe[self.dataframe.columns[-1]])
dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
print('First house\'s age:', dp.X[0][1])
print('House price/unit are:', dp.y[0])
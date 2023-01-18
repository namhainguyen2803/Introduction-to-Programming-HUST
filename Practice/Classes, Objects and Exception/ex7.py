import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

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
        self.X = np.array(self.dataframe[self.dataframe.columns[:-1]])
        self.y = np.array(self.dataframe[self.dataframe.columns[-1]])
    
    def final_train_test_data(self, attributes_list=[0,1,2,3,4,5], test_size=0.2):
        X = np.array(self.dataframe.iloc[:,attributes_list])
        y = self.y
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size, random_state=42)
        return (X_train, X_test, y_train, y_test)
dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
X_train, X_test, y_train, y_test = dp.final_train_test_data(attributes_list=[2,4,5], test_size=0.2)
print('Shape of X_train: ', X_train.shape)
print('Shape of y_train: ', y_train.shape)
print('Shape of X_test: ', X_test.shape)
print('Shape of y_test: ', y_test.shape)
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 21:51:40 2018

@author: Reda
"""

#### House Price Prediction Example
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class housePrice():
    def __init__(self):
        self.df = pd.read_csv(r"data\house_data.csv")        
        self.important_features = ['price','bedrooms','bathrooms','floors','waterfront','grade','lat','long']
        self.data = self.df[self.important_features]
        self.lin_reg = LinearRegression()
    
    def train(self):
        X = self.data.iloc[:, 1:].values
        Y = self.data.iloc[:, 0].values
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size = 0.3)
        return self.lin_reg.fit(self.x_train, self.y_train)
    
    def predict(self):
        print('\nPredicted price: \n\n', self.lin_reg.predict(self.x_test))
    
    def yourPrediction(self, bedrooms, bathrooms, floors, waterfront, grade, lat, long):
        print('\nPredicted price: \n\n', self.lin_reg.predict([[bedrooms, bathrooms, floors, waterfront, grade, lat, long]]))
    
    def plot(self, x_axis, y_axis):
        x_axis = x_axis.lower()
        y_axis = y_axis.lower()
        figure(figsize=(8,6))
        plt.scatter(self.data[x_axis], self.data[y_axis])
        plt.xlabel("{}".format(x_axis))
        plt.ylabel("{}".format(y_axis))
        plt.title("{} vs {}".format(x_axis, y_axis))
        return plt.show()
    
    def run(self):
        self.train()
        self.predict()
        print("\nDone")

if __name__ == "__main__":
    hP = housePrice()
    hP.run()
    
    

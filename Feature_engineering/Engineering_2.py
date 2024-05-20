import pandas as pd 
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 
from sklearn.preprocessing import StandardScaler
import os
flights = pd.read_csv('Feature_engineering/engineering_data.csv')
print(flights)
#Dropping the arrivals and departure hours 
flights = flights.drop(['First flight departure','Second flight departure','Third flight departure','First flight arrival','Second flight arrival','Third flight arrival'], axis=1)
print(flights)
print(flights.isnull().sum())
#Remove lastTicketingDate
#Remove the meal option column -> non information 
#Remove baggage is charable --> from EDA results 
#Remove row where ET is 
flights = flights.drop(['lastTicketingDate','BAGGAGE_isChargeable','BAGGAGE_description','Meal Option'], axis=1)
#Remove rows where Branded fare Lables is missing 
flights.dropna(subset=['Branded Fare Labels'], inplace=True)
#Removing Base Price --> high correlation to Grand Total Price 
flights = flights.drop(['Base Price'], axis=1)
num_rows, num_columns = flights.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)
#Removing the Grand Total Price 
flights = flights.drop(['Grand Total Price'], axis=1)

# Assuming 'flights' is your DataFrame
flights['Duration'] = np.log(flights['Duration'])
#Drop the price as we have the log price now 


flights.to_csv('final_data.csv', index=False)

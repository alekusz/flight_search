# Decision trees 

# Read the CSV file
data = pd.read_csv('cleaned_data.csv')

# Print the first few rows of the DataFrame
print(data.head())
data.columns
data.dtypes

#load libraries 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn import tree
import matplotlib.pyplot as plt

#Initial split

data['Grand Total Price']
# Split data into features (X) and target (y)
X = data.drop('Grand Total Price', axis=1)  # Features
y = data['Grand Total Price']  # Target variable

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Perform a regression to predict a scalar grand total
# Initialize the Decision Tree Regressor
reg = DecisionTreeRegressor(random_state=42)

# Train the regressor
reg.fit(X_train, y_train)


# Predict on the test set
y_pred = reg.predict(X_test)  # For regression


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')


import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np
flights = pd.read_csv('/Users/aleksandrakusz/Desktop/2nd BI/flight_search/cleaned_data.csv')
#Imputing null values as mentioned in the EDA with layovers 

# Imputing missing values with "No layover"
columns_to_fill = ['Airport layover 1', 'Airport layover 2']
for column in columns_to_fill:
    flights[column] = flights[column].replace('', 'No layover')

columns_to_fill_2 = ['Flight duration 1', 'Flight duration 2']
for column in columns_to_fill:
    flights[column] = flights[column].replace('', '0')

# Imputing missing values with "No layover"
columns_to_impute = ['Flight duration 2', 'Flight duration 3']
flights[columns_to_impute] = flights[columns_to_impute].fillna("0")

#Second and third  flight departure, second and third flight arrival 



# Visualize missing values using a matrix
msno.matrix(flights)
plt.title('Missing Values Matrix')
plt.show()
print(flights.isnull().sum())

#Log transformation Grand Total Price and Base Price 

# Apply log transformation to the price variable
flights['Log Grand Total Price'] = np.log(flights['Grand Total Price'])

# Check the transformation
print(flights[['Log Grand Total Price', 'Grand Total Price']].head())



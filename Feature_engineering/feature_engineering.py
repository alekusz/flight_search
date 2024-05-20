import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 
import os

current_directory = os.getcwd()
print(current_directory)

# Change the current working directory
os.chdir("data_preprocessing")

flights = pd.read_csv('cleaned_data.csv')
print(flights)
#Change the arrivals and departure dates to morning/afternoon/evening 

# Function to categorize flight times into morning, afternoon and evening
def categorize_time(time_str):
        if time_str:
            hour = int(time_str.split(':')[0])
            if 6 <= hour < 12:
                return "Morning"
            elif 12 <= hour < 18:
                return "Afternoon"
            else:
                return "Evening"

flights['Departure Time'] = flights['First flight departure'].apply(categorize_time)



# Function to categorize arrival time based on the the first non-empty column (there are 3 arrival time columns for layovers)
def categorize_arrival_time(row):
    for column in ['Third flight arrival', 'Second flight arrival', 'First flight arrival']:
        if pd.notna(row[column]) and row[column]:  # Check if the value is not NaN and not empty
            return categorize_time(row[column])
    return "Unknown"  # Return 'Unknown' if all columns are empty or NaN

# Apply function and generate new column called 'Arrival Time'
flights['Arrival Time'] = flights.apply(categorize_arrival_time, axis=1)

# Print dataframe
print(flights)

flights['Flight depature date'].unique()
# array(['2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20',
#       '2024-06-21', '2024-06-22', '2024-06-23'], dtype=object)


# Make these into Monday, tuesday, wednesday, etc. --------------------------------------------------------
# Function to get day of the week from a date string
def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')

# Apply the function to create Day of Departure
flights['Day of Week Departure'] = flights['Flight depature date'].apply(get_day_of_week)

# check if new row was made
print(flights)

# Make new variable for weekday/weekend: ------------------------------------------------

# Function to classify day as 'Weekday' or 'Weekend'
def classify_day(day_of_week):
    if day_of_week in ['Saturday', 'Sunday']:
        return 'Weekend'
    else:
        return 'Weekday'

# Apply the function to create Day of Departure
flights['Day Type Departure'] = flights['Day of Week Departure'].apply(classify_day)

# check if new row was made
print(flights)

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

parent_directory = os.path.dirname(current_directory)
print(parent_directory)

os.chdir(parent_directory)
os.chdir("Feature_engineering")

# Convert data frame to csv file.
flights.to_csv('engineering_data.csv', index=False)



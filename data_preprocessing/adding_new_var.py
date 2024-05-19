import pandas as pd
import csv
from datetime import datetime

# Read the appended CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# Creating a new column for departure and arrival times to be categorized ---------------------------

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

df['Departure Time'] = df['First flight departure'].apply(categorize_time)

# Function to categorize arrival time based on the the first non-empty column (there are 3 arrival time columns for layovers)
def categorize_arrival_time(row):
    for column in ['Third flight arrival', 'Second flight arrival', 'First flight arrival']:
        if pd.notna(row[column]) and row[column]:  # Check if the value is not NaN and not empty
            return categorize_time(row[column])
    return "Unknown"  # Return 'Unknown' if all columns are empty or NaN

# Apply function and generate new column called 'Arrival Time'
df['Arrival Time'] = df.apply(categorize_arrival_time, axis=1)

# Print dataframe
print(df)

df['Flight depature date'].unique()
# array(['2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20',
#       '2024-06-21', '2024-06-22', '2024-06-23'], dtype=object)


# Make these into Monday, tuesday, wednesday, etc. --------------------------------------------------------
# Function to get day of the week from a date string
def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')

# Apply the function to create Day of Departure
df['Day of Week Departure'] = df['Flight depature date'].apply(get_day_of_week)

# check if new row was made
print(df)

# Make new variable for weekday/weekend: ------------------------------------------------

# Function to classify day as 'Weekday' or 'Weekend'
def classify_day(day_of_week):
    if day_of_week in ['Saturday', 'Sunday']:
        return 'Weekend'
    else:
        return 'Weekday'

# Apply the function to create Day of Departure
df['Day Type Departure'] = df['Day of Week Departure'].apply(classify_day)

# check if new row was made
print(df)

# Convert data frame to csv file.
df.to_csv('engineering_data.csv', index=False)

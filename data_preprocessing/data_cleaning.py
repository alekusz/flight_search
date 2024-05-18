import pandas as pd
import csv

# Read the appended CSV file into a DataFrame
df = pd.read_csv('modified_flights_data.csv')

# Deleting columns with >80% missing data
df = df.drop(['TRAVEL_SERVICES_amenityProvider', 'TRAVEL_SERVICES_isChargeable', 'TRAVEL_SERVICES_description',
              'PRE_RESERVED_SEAT_amenityProvider', 'PRE_RESERVED_SEAT_isChargeable', 'PRE_RESERVED_SEAT_description',
              'BRANDED_FARES_amenityProvider', 'BRANDED_FARES_isChargeable', 'BRANDED_FARES_description'], axis=1)

print(df)

# Checking the columns: 
# Currency.1
unique_values = df['Currency.1'].unique()

# Print the unique values
print("Unique values:", unique_values)
    # only currency is EUR -> delete

df = df.drop('Currency.1', axis=1)

# Total Price.1 -> these have the same as grand total, so we also delete this. 
df = df.drop('Total Price.1', axis=1)

# Flight departures -> turn into categorical variable

# Function to extract time after 'T'
def extract_time(datetime_str):
    if isinstance(datetime_str, str) and 'T' in datetime_str:
        return datetime_str.split('T')[1]
    else:
        return ''
    
# apply function to all departures and arrivals
df['Firt flight departure'] = df['Firt flight departure'].apply(extract_time)
df['Second flight departure'] = df['Second flight departure'].apply(extract_time)
df['Third flight departure'] = df['Third flight departure'].apply(extract_time)
df['Firt flight arrival'] = df['Firt flight arrival'].apply(extract_time)
df['Second flight arrival'] = df['Second flight arrival'].apply(extract_time)
df['Third flight arrival'] = df['Third flight arrival'].apply(extract_time)

# Rename column
df.rename(columns={'Firt flight departure': 'First flight departure'}, inplace=True)
df.rename(columns={'Firt flight arrival': 'First flight arrival'}, inplace=True)

print(df)

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
        if row[column]:
            return categorize_time(row[column])
    return "Unknown"  # Return 'Unknown' if all columns are empty

# Apply function and generate new column called 'Arrival Time'
df['Arrival Time'] = df.apply(categorize_arrival_time, axis=1)

# Print dataframe
print(df)

# Convert data frame to csv file.
df.to_csv('cleaned_data.csv', index=False)








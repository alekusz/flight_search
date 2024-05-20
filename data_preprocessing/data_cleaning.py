import pandas as pd
import csv
import os

current_directory = os.getcwd()
print(current_directory)

# Change the current working directory
os.chdir("data_preprocessing")

# Read the appended CSV file into a DataFrame
df = pd.read_csv('modified_flights_data.csv')

# Deleting columns with >80% missing data
df = df.drop(['TRAVEL_SERVICES_amenityProvider', 'TRAVEL_SERVICES_isChargeable', 'TRAVEL_SERVICES_description',
              'PRE_RESERVED_SEAT_amenityProvider', 'PRE_RESERVED_SEAT_isChargeable', 'PRE_RESERVED_SEAT_description',
              'BRANDED_FARES_amenityProvider', 'BRANDED_FARES_isChargeable', 'BRANDED_FARES_description'], axis=1)

print(df)

# Checking the columns: 

# id -> these this is the primary key for SQL database, but it is not used in the analysis
df = df.drop('id', axis=1)

# Currency.1
unique_values = df['Currency.1'].unique()

# Print the unique values
print("Unique values:", unique_values)
    # only currency is EUR -> delete

df = df.drop('Currency.1', axis=1)

# Remove Airport origin (all should be from CPH)
df = df.drop('Origin Airport', axis=1)

# DUPLICATE COLUMNS

# Total Price.1 -> these have the same as grand total, so we also delete this. 
df = df.drop('Total Price.1', axis=1)

# Base price.1 -> these this is duplicate column of Base price. 
df = df.drop('Base Price.1', axis=1)

# 1st layover
df = df.drop('1st layover', axis=1)

# 2nd layover
df = df.drop('2nd layover', axis=1)

# Branded Fares Lables
df = df.drop('Branded Fares Lables', axis=1)

# Origin airport
df = df.drop('Origin airport', axis=1)

# Flight departures -> get a date variable

# Function to extract date from datetime string
def extract_date(datetime_str):
    if datetime_str:
        return datetime_str.split('T')[0]
    return ''

df['Flight depature date'] = df['Firt flight departure'].apply(extract_date)

print(df['Flight depature date'])

# Flight departures extracting time of departure

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

# Define the function to convert ISO durations to hours
def iso_to_hours(duration_str):
    if duration_str.strip():  # Check if the string is not empty or contains only whitespace
        duration_str = duration_str.replace('PT', '')
        if 'H' in duration_str and 'M' in duration_str:
            hours, minutes = duration_str.split('H')
            minutes = minutes.replace('M', '')
            total_hours = int(hours) + int(minutes) / 60
            return total_hours
        elif 'H' in duration_str:
            hours = duration_str.replace('H', '')
            total_hours = int(hours)
            return total_hours
        elif 'M' in duration_str:
            minutes = duration_str.replace('M', '')
            total_hours = int(minutes) / 60
            return total_hours
    else:
        return None

# Apply the function to the "Flight duration 2" column
df['Duration'] = df['Duration'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(df['Duration'])

# Define the function to convert ISO durations to hours
def iso_to_hours(duration_str):
    if duration_str.strip():  # Check if the string is not empty or contains only whitespace
        duration_str = duration_str.replace('PT', '')
        if 'H' in duration_str and 'M' in duration_str:
            hours, minutes = duration_str.split('H')
            minutes = minutes.replace('M', '')
            total_hours = int(hours) + int(minutes) / 60
            return total_hours
        elif 'H' in duration_str:
            hours = duration_str.replace('H', '')
            total_hours = int(hours)
            return total_hours
        elif 'M' in duration_str:
            minutes = duration_str.replace('M', '')
            total_hours = int(minutes) / 60
            return total_hours
    else:
        return None

# Apply the function to the "Flight duration 2" column
df['Flight duration 1'] = df['Flight duration 1'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(df['Flight duration 1'])


# Define a function to convert ISO durations to hours
def iso_to_hours(duration_str):
    if isinstance(duration_str, str) and duration_str.strip():  # Check if the string is not empty or contains only whitespace
        duration_str = duration_str.replace('PT', '')  # Remove 'PT' from the string
        
        # Initialize hours and minutes
        hours, minutes = 0, 0
        
        # Split the duration string into hours and minutes
        if 'H' in duration_str:
            hours = int(duration_str.split('H')[0])  # Extract hours part
            duration_str = duration_str.split('H')[1]  # Remaining string after hours
        
        if 'M' in duration_str:
            minutes = int(duration_str.split('M')[0])  # Extract minutes part
        
        # Convert to total hours
        total_hours = hours + minutes / 60
        return total_hours
    else:
        return None

# Apply the function to the "Flight duration 2" column
df['Flight duration 2'] = df['Flight duration 2'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(df['Flight duration 2'])

def iso_to_hours(duration_str):
    if isinstance(duration_str, str) and duration_str.strip():  # Check if the string is not empty or contains only whitespace
        duration_str = duration_str.replace('PT', '')  # Remove 'PT' from the string
        
        # Initialize hours and minutes
        hours, minutes = 0, 0
        
        # Split the duration string into hours and minutes
        if 'H' in duration_str:
            hours = int(duration_str.split('H')[0])  # Extract hours part
            duration_str = duration_str.split('H')[1]  # Remaining string after hours
        
        if 'M' in duration_str:
            minutes = int(duration_str.split('M')[0])  # Extract minutes part
        
        # Convert to total hours
        total_hours = hours + minutes / 60
        return total_hours
    else:
        return None

# Apply the function to the "Flight duration 2" column
df['Flight duration 3'] = df['Flight duration 3'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(df['Flight duration 3'])

print(df)

#Remove lastTicketingDateTime as this is a duplicate 
df = df.drop('lastTicketingDateTime', axis=1)
#Remove Airline as this is a duplicate 
df = df.drop('Airline', axis=1)
#Remove branded fares as this is a duplicate 
df = df.drop('Branded Fares', axis=1)

print(df['First flight departure'])

# Convert data frame to csv file.
df.to_csv('cleaned_data.csv', index=False)









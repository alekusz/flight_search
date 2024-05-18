import pandas as pd
flights = pd.read_csv('/Users/aleksandrakusz/Desktop/2nd BI/flight_search/modified_flights_data.csv')
print(flights)
#Chaning flight duration 

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
flights['Duration'] = flights['Duration'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(flights['Duration'])

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
flights['Flight duration 1'] = flights['Flight duration 1'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(flights['Flight duration 1'])


# Define a function to convert ISO durations to hours
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
flights['Flight duration 2'] = flights['Flight duration 2'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(flights['Flight duration 2'])

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
flights['Flight duration 3'] = flights['Flight duration 3'].apply(iso_to_hours)

# Print the modified DataFrame to verify the changes
print(flights['Flight duration 3'])













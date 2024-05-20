import pandas as pd
flights = pd.read_csv('/Users/aleksandrakusz/Desktop/2nd BI/appended_flight_data.csv')
print(flights).head()
print("Number of rows:", flights.shape[0])
print("Number of columns:", flights.shape[1])
print("Column names:", flights.columns.tolist())
#Splitting the columns 
# Split the 'layover durations' column into new columns based on the comma-separated values
new_columns = flights['layover durations'].str.split(r'[:,]', expand=True)
#Remove the curly brackets and ' ' 
new_columns = new_columns.applymap(lambda x: x.replace('{', '').replace('}', '').replace("'", '') if isinstance(x, str) else x)
# Concatenate the new columns with the original DataFrame
flights = pd.concat([flights, new_columns], axis=1)
print(flights)
#Changing the column names: 
new_column_names = {
    0: 'Origin Airport',
    1: 'Flight duration 1',
    2: 'Airport layover 1',
    3: 'Flight duration 2',
    4: 'Airport layover 2',
    5: 'Flight duration 3'
}
flights = flights.rename(columns=new_column_names)
print(flights)
#Arrival terminal remove now 
flights.drop('Arrival Terminals', axis=1, inplace=True)
#Departure time 
# Split each string in the list based on commas
new_columns = flights['Departure Times'].str.split(r'[,]', expand=True)
print(new_columns)
new_column_names = {
    0: 'Firt flight departure',
    1: 'Second flight departure',
    2: 'Third flight departure',
}
flights = pd.concat([flights, new_columns], axis=1)
flights = flights.rename(columns=new_column_names)

#Arrival times
new_columns = flights['Arrival Times'].str.split(r'[,]', expand=True)
print(new_columns)
new_column_names = {
    0: 'Firt flight arrival',
    1: 'Second flight arrival',
    2: 'Third flight arrival',
}
flights = pd.concat([flights, new_columns], axis=1)
flights = flights.rename(columns=new_column_names)
flights.drop('layover durations', axis=1, inplace=True)

#Airline
# Split the values by comma and extract the first part
flights['Airline'] = flights['Airline'].str.split(',').str[0]
print(flights['Airline'])
#DRop currency as it is only EUR 
flights.drop('Currency', axis=1, inplace=True)
##Drop Fee Amount (it is only 0)
flights.drop('Fee Amount', axis=1, inplace=True)
#Removing more columns: 
# Assuming 'flights' is your DataFrame
columns_to_remove = ['Additional fees', 'Fee Type', 'Traveler ID', 'Fare Option', 'Traveler Type', 'Total Price']
flights = flights.drop(columns=columns_to_remove)
#removing more colums that have the same data everywhere 
columns_to_remove = ['type','source','instantTicketingRequired','nonHomogeneous','oneWay']
flights = flights.drop(columns=columns_to_remove)

#Validating airline codes revmoing the brackets etc 
flights['validatingAirlineCodes'] = flights['validatingAirlineCodes'].apply(lambda x: x.replace('[', '').replace(']', '').replace('"', '') if isinstance(x, str) else x)
print(flights['validatingAirlineCodes'])
##Departure IATACodes
new_columns = flights['Departure IATACodes'].str.split(r'[,]', expand=True)
print(new_columns)
new_column_names = {
    0: 'Origin airport',
    1: '1st layover',
    2: '2nd layover',
}
flights = pd.concat([flights, new_columns], axis=1)
flights = flights.rename(columns=new_column_names)
flights.drop('Departure IATACodes', axis=1, inplace=True)
#Departure terminals remove 
flights.drop('Departure Terminals', axis=1, inplace=True)
#Blacklist 
flights.drop('Blacklist', axis=1, inplace=True)
#Segments ID 
flights.drop('Segment IDs', axis=1, inplace=True)
#Cabins 
flights.drop('Cabins', axis=1, inplace=True)
#Fare bases 
flights.drop('Fare Bases', axis=1, inplace=True)
#Branded fares 
flights['Branded Fares'] = flights['Branded Fares'].str.split(',').str[0]
flights['Branded Fares'] = flights['Branded Fares'].apply(lambda x: x.replace('[', '').replace(']', '').replace("'", '') if isinstance(x, str) else x)
print(flights['Branded Fares'])

#Branded fares labels 
flights['Branded Fares Lables'] = flights['Branded Fares'].str.split(',').str[0]
flights['Branded Fares Lables'] = flights['Branded Fares Labels'].apply(lambda x: x.replace('[', '').replace(']', '').replace("'", '') if isinstance(x, str) else x)
print(flights['Branded Fares Lables'])

#Classes 
flights.drop('Classes', axis=1, inplace=True)

#Included checked bags 
flights['Included Checked Bags Quantities'] = flights['Included Checked Bags Quantities'].str.split(',').str[0]
flights['Included Checked Bags Quantities'] = flights['Included Checked Bags Quantities'].apply(lambda x: x.replace('[', '').replace(']', '').replace("'", '') if isinstance(x, str) else x)
print(flights['Included Checked Bags Quantities'])

#Checked baggage description 
flights['BAGGAGE_description'] = flights['BAGGAGE_description'].str.split(';').str[0]
print(flights['BAGGAGE_description'])

#Chargable baggage
flights['BAGGAGE_isChargeable'] = flights['BAGGAGE_isChargeable'].str.split(';').str[0]
print(flights['BAGGAGE_isChargeable'])

#BAGGAGE_amenityProvider
flights.drop('BAGGAGE_amenityProvider', axis=1, inplace=True)

#Remove meal and entertainment
columns_to_remove = ['ENTERTAINMENT_description', 'ENTERTAINMENT_isChargeable', 'ENTERTAINMENT_amenityProvider']
flights.drop(columns=columns_to_remove, inplace=True)

#Branded fares 
flights['BRANDED_FARES_description'] = flights['BRANDED_FARES_description'].str.split(';').str[0]
print(flights['BRANDED_FARES_description'])

flights['BRANDED_FARES_isChargeable'] = flights['BRANDED_FARES_isChargeable'].str.split(';').str[0]
print(flights['BRANDED_FARES_isChargeable'])

flights['BRANDED_FARES_amenityProvider'] = flights['BRANDED_FARES_amenityProvider'].str.split(';').str[0]
print(flights['BRANDED_FARES_amenityProvider'])

flights['PRE_RESERVED_SEAT_description'] = flights['PRE_RESERVED_SEAT_description'].str.split(';').str[0]
print(flights['PRE_RESERVED_SEAT_description'])

flights['PRE_RESERVED_SEAT_isChargeable'] = flights['PRE_RESERVED_SEAT_isChargeable'].str.split(';').str[0]
print(flights['PRE_RESERVED_SEAT_isChargeable'])

flights['PRE_RESERVED_SEAT_amenityProvider'] = flights['PRE_RESERVED_SEAT_amenityProvider'].str.split(';').str[0]
print(flights['PRE_RESERVED_SEAT_amenityProvider'])

flights['TRAVEL_SERVICES_description'] = flights['TRAVEL_SERVICES_description'].str.split(';').str[0]
print(flights['TRAVEL_SERVICES_description'])

flights['TRAVEL_SERVICES_isChargeable'] = flights['TRAVEL_SERVICES_isChargeable'].str.split(';').str[0]
print(flights['TRAVEL_SERVICES_isChargeable'])

flights['TRAVEL_SERVICES_amenityProvider'] = flights['TRAVEL_SERVICES_amenityProvider'].str.split(';').str[0]
print(flights['TRAVEL_SERVICES_amenityProvider'])

flights.drop('Arrival Times', axis=1, inplace=True)
#Branded fare lables 
flights['Branded Fare Labels'] = flights['Branded Fare Labels'].str.split(',').str[0]
flights['Branded Fare Labels'] = flights['Branded Fare Labels'].apply(lambda x: x.replace('[', '').replace(']', '').replace("'", '') if isinstance(x, str) else x)
print(flights['Branded Fare Labels'])

# Function to extract the string before the semicolon
def extract_string(entry):
    if isinstance(entry, str):
        return entry.split(";")[0].strip()
    else:
        return entry  # If entry is not a string, return it as is

# Apply the function to the 'MEAL_description' column and create a new column 'extracted_string'
flights['Meal Option'] = flights['MEAL_description'].apply(extract_string)

# Display the DataFrame
print(flights['Meal Option'])

columns_to_remove = ['MEAL_isChargeable','MEAL_amenityProvider']
flights = flights.drop(columns=columns_to_remove)

flights.drop('', axis=1, inplace=True)







# Save the modified DataFrame to a CSV file
flights.to_csv('modified_flights_data.csv', index=False)
print(flights)


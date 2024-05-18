import pandas as pd

# Read the flight_nyc CSV file into a DataFrame
df1 = pd.read_csv('flight_nyc.csv')
 
#  Specify columns to delete (these were extracted in other files.)
columns_to_delete = ['itineraries', 'price', 'pricingOptions', 'travelerPricings']  

# Delete itineraries, price, pricing options and travelerPricings columns 
df1 = df1.drop(columns=columns_to_delete)

# Read the itinerary CSV file into a DataFrame
df2 = pd.read_csv('itinerary.csv')

# Read the price CSV file into a DataFrame
df3 = pd.read_csv('price.csv')

# Read the travelprice CSV file into a DataFrame
df4 = pd.read_csv('travelprice.csv')

# Append the dataframes
df = pd.concat([df1, df2, df3, df4], axis = 1)

# REMEMBER TO CHANGE DIRECTORY
# Save the final DataFrame as a CSV file
df.to_csv('appended_flight_data.csv', index=False)

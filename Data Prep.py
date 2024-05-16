import pandas as pd

# Import the data
data = pd.read_csv('output.csv')


# Custom function to extract duration
def extract_duration(observation):
    start_index = observation.find("'duration': '") + len("'duration': '")
    end_index = observation.find("',", start_index)
    
    duration = observation[start_index:end_index]
    
    return duration

# Apply the custom function to the entire 'itineraries' column
data['duration'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'duration' values
print(data)


# Function to extract the Departure date 
def extract_duration(depart):
    start_index = depart.find("'at': '") + len("'at': '")
    end_index = depart.find("T", start_index)
    
    depart = depart[start_index:end_index]
    
    return depart

# Apply the custom function to the entire 'itineraries' column
data['Departure'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'depart' values
print(data)


# Function to extract the Departure time 
def extract_duration(departtime):
    start_index = departtime.find("'at': '2024-06-21T") + len("'at': '2024-06-21T")
    end_index = departtime.find("'", start_index)
    
    departtime = departtime[start_index:end_index]
    
    return departtime

# Apply the custom function to the entire 'itineraries' column
data['Departure_time'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'departtime' values
print(data)


# Function to extract the Destination  
def extract_duration(dest):
    start_index = dest.find("'arrival': {'iataCode': '") + len("'arrival': {'iataCode': '")
    end_index = dest.find("'", start_index)
    
    dest = dest[start_index:end_index]
    
    return dest

# Apply the custom function to the entire 'itineraries' column
data['Destination'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'Destination' values
print(data)


# Function to extract the Airline 
def extract_duration(airline):
    start_index = airline.find("{'carrierCode': '") + len("{'carrierCode': '")
    end_index = airline.find("'},", start_index)
    
    airline = airline[start_index:end_index]
    
    return airline

# Apply the custom function to the entire 'itineraries' column
data['Airline'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'airline' values
print(data)


# Function to extract the FlightID
def extract_duration(id):
    start_index = id.find("'id': '") + len("'id': '")
    end_index = id.find("',", start_index)
    
    id = id[start_index:end_index]
    
    return id

# Apply the custom function to the entire 'itineraries' column
data['FlightID'] = data['itineraries'].apply(extract_duration)

# Print the DataFrame with the extracted 'id' values
print(data)

# Function to count occurrences of 'destination' in each row (number of flights to take)
def count_destinations(row_text):
    return row_text.count("departure")

# Apply the function to count 'destination' occurrences and create a new column
data['nr_of_flights'] = data['itineraries'].apply(count_destinations)

print(data)

#Extracting base prices 
def extract_baseprice(base):
    start_index = base.find("'base': '") + len("'base': '")
    end_index = base.find("'}", start_index)
    
    base = base[start_index:end_index]
    
    return base

# Apply the custom function to the entire 'itineraries' column
data['Base_Price'] = data['travelerPricings'].apply(extract_baseprice)

print(data)


#Extracting Branded Fare
def extract_label(label):
    start_index = label.find("'brandedFare': '") + len("'brandedFare': '")
    end_index = label.find("',", start_index)
    
    label = label[start_index:end_index]
    
    return label

# Apply the custom function to the entire 'itineraries' column
data['Fare_Label'] = data['travelerPricings'].apply(extract_label)

print(data)


#Change name of Price column 
data['Price'] = data['price.grandTotal']


#Basic data cleaning 

data.info

#Look at missing data 
data.isna().any()
#no missing values, Fare_label does have a lot of '1' that dont have meaning 

#Look at the Fare_Label more
data["Fare_Label"].describe

#See if we have any duplicate values 
data[data["FlightID"].duplicated()]

#Look at the datatypes
data.dtypes

#Change the datatypes 

data['Base_Price'] = data['Base_Price'].astype(float)

data['numberOfBookableSeats'] = data['numberOfBookableSeats'].astype(float)
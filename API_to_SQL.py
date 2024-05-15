import sqlite3
from amadeus import Client, ResponseError
import json

# Establish a connection to the SQLite database
connection = sqlite3.connect(r'/Users/aleksandrakusz/Desktop/amadeus_API.db')
cursor = connection.cursor()

# Create a table to store flight offers data
create_table_sql = '''
CREATE TABLE IF NOT EXISTS flight_search (
    type VARCHAR(255),
    id VARCHAR(255),
    source VARCHAR(255),
    instantTicketingRequired BOOLEAN,
    nonHomogeneous BOOLEAN,
    oneWay BOOLEAN,
    lastTicketingDate DATE,
    lastTicketingDateTime TIMESTAMP,
    numberOfBookableSeats INT,
    itineraries TEXT,
    price TEXT,
    pricingOptions TEXT,
    validatingAirlineCodes TEXT,
    travelerPricings TEXT,
    PRIMARY KEY (id)
)
'''
cursor.execute(create_table_sql)

# Initialize Amadeus client
amadeus = Client(
    client_id='ABwWtJRY4Yr6GG1Pej89OuioWf1lZi1q',
    client_secret='DG1oAYlSQty9fTSh'
)

# Function to fetch flight offers and update SQLite database
# Function to fetch flight offers and update SQLite database
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='CPH', 
        destinationLocationCode='LGW', 
        departureDate='2024-06-21',
        adults=1)
    print(response.data)
except ResponseError as error:
    print(error)
        # Insert flight offers into the SQLite database

for offer in response.data:
            try:
                    cursor.execute('INSERT INTO flight_search (type, id, source, instantTicketingRequired, nonHomogeneous, oneWay, lastTicketingDate, lastTicketingDateTime, numberOfBookableSeats, itineraries, price, pricingOptions, validatingAirlineCodes, travelerPricings) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                   (offer['type'], offer['id'], offer['source'], offer['instantTicketingRequired'], offer['nonHomogeneous'], offer['oneWay'], offer['lastTicketingDate'], offer['lastTicketingDateTime'], offer['numberOfBookableSeats'], json.dumps(offer['itineraries']), json.dumps(offer['price']), json.dumps(offer['pricingOptions']), json.dumps(offer['validatingAirlineCodes']), json.dumps(offer['travelerPricings'])))
                    connection.commit()
            except ResponseError as error:
                print(error)


    # Commit changes and close connection
connection.commit()
connection.close()
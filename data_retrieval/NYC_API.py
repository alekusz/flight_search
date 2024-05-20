import sqlite3
from amadeus import Client, ResponseError
import json
from datetime import datetime, timedelta

# Establish a connection to the SQLite database
connection = sqlite3.connect(r'/Users/aleksandrakusz/Desktop/amadeus_API.db')
cursor = connection.cursor()

# Create a table to store flight offers data
create_table_sql = '''
CREATE TABLE IF NOT EXISTS flight_nyc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(255),
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
    travelerPricings TEXT
)
''' 
cursor.execute(create_table_sql)

# Initialize Amadeus client
amadeus = Client(
    client_id='ABwWtJRY4Yr6GG1Pej89OuioWf1lZi1q',
    client_secret='DG1oAYlSQty9fTSh'
)

# Fetch flight offers from Amadeus API for dates from 17.06 to 24.06.2024
start_date = datetime(2024, 6, 17)
end_date = datetime(2024, 6, 23)
delta = timedelta(days=1)

while start_date <= end_date:
    departure_date = start_date.strftime('%Y-%m-%d')
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='CPH', 
            destinationLocationCode='JFK', 
            departureDate=departure_date,
            adults=1
        )
        print(response.data)
        
        # Insert flight offers into the SQLite database
        for offer in response.data:
            cursor.execute('INSERT INTO flight_nyc (type, source, instantTicketingRequired, nonHomogeneous, oneWay, lastTicketingDate, lastTicketingDateTime, numberOfBookableSeats, itineraries, price, pricingOptions, validatingAirlineCodes, travelerPricings) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (offer['type'], offer['source'], offer['instantTicketingRequired'], offer['nonHomogeneous'], offer['oneWay'], offer['lastTicketingDate'], offer['lastTicketingDateTime'], offer['numberOfBookableSeats'], json.dumps(offer['itineraries']), json.dumps(offer['price']), json.dumps(offer['pricingOptions']), json.dumps(offer['validatingAirlineCodes']), json.dumps(offer['travelerPricings'])))
        
        # Commit changes after each day's data insertion
        connection.commit()
    except ResponseError as error:
        print(error)
    
    start_date += delta

# Close connection
connection.close()
import json
import csv

# Function to extract desired fields from JSON itinerary
def extract_fields(json_data):
    duration = json_data["duration"]
    segments = json_data["segments"]
    arrival = json_data["segments"][0]["arrival"]
    arrival_iataCode = arrival["iataCode"]
    aircraft = json_data["segments"][0]["aircraft"]
    aircraft_code = aircraft.get("code")
    blacklist = json_data["segments"][0]["blacklistedInEU"]
    
    departure_iataCodes = []
    departure_terminals = []
    departure_times = []
    departure_durations = {}
    arrival_terminals = []
    
    # Extract departure iataCodes, terminals, durations, terminals and time for each segment
    for segment in segments:
        departure = segment["departure"]
        departure_iataCode = departure["iataCode"]
        departure_iataCodes.append(departure_iataCode)
        departure_times.append(departure.get("at", None))
        departure_terminals.append(departure.get("terminal", None))
        arrival_terminals.append(arrival.get("terminal", None)) 


        if departure_iataCode not in departure_durations:
            departure_durations[departure_iataCode] = []
        departure_durations[departure_iataCode].append(segment["duration"])

    
    # Combine iataCodes and terminals and times into a single string
    iataCodes_str = ', '.join(departure_iataCodes)
    terminals_str = ', '.join(str(terminal) if terminal is not None else "" for terminal in departure_terminals)
    times_str = ', '.join(str(at) if at is not None else "" for at in departure_times)
    arrival_terminals_str = ', '.join(str(terminal) if terminal is not None else "" for terminal in arrival_terminals)   
    
    # Calculate number of stops based on the number of segments
    number_of_stops = max(0, len(segments) - 1)
    
    arrival_terminals_str = ', '.join(str(terminal) if terminal is not None else "" for terminal in arrival_terminals)   
    return duration, iataCodes_str, terminals_str, number_of_stops, departure_durations, arrival_iataCode, arrival_terminals_str, times_str, aircraft_code, blacklist

# Read CSV file and process each row
with open('flight_search.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Define output headers
    output_headers = ['Duration', 'Departure IATACodes', 'Departure Terminals', 'Number of Stops', 'layover durations', 'Arrival IATACode', 'Departure Times',
                      'Arrival Times', 'Aircraft', 'Blacklist']
    
    # Open a new CSV file for writing output
    with open('itinerary.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(output_headers)
        
        # Process each row
        for row in csv_reader:
            # Extract itinerary from the 'itineraries' column
            itinerary_json = row['itineraries']
            itinerary_data = json.loads(itinerary_json)[0]  # Assuming there's only one itinerary per row
            
            # Extract desired fields
            duration, departure_iataCodes, departure_terminals, number_of_stops, departure_durations, arrival_iataCode, arrival_terminal, departure_time, aircraft_code, blacklist = extract_fields(itinerary_data)
            
            # Write extracted data to output CSV
            writer.writerow([duration, departure_iataCodes, departure_terminals, number_of_stops, departure_durations, arrival_iataCode, arrival_terminal, departure_time, aircraft_code, blacklist])

import json
import csv

# Function to extract desired fields from JSON itinerary
def extract_fields(json_data):
    duration = json_data["duration"]
    segments = json_data["segments"]
    
    departure_iataCodes = []
    departure_terminals = []
    departure_times = []
    departure_durations = {}
    arrival_terminals = []
    arrival_times = []
    airline_codes = []
    blacklists = []
    
    for segment in segments:
        departure = segment["departure"]
        departure_iataCode = departure["iataCode"]
        departure_iataCodes.append(departure_iataCode)
        departure_times.append(departure.get("at", None))
        departure_terminals.append(departure.get("terminal", None))
        departure_durations[departure_iataCode] = segment["duration"]

        arrival = segment["arrival"]
        arrival_terminals.append(arrival.get("terminal", None))
        arrival_times.append(arrival.get("at", None))

        airline_codes.append(segment.get("carrierCode", False))

        blacklists.append(segment.get("blacklistedInEU", False))

    iataCodes_str = ', '.join(departure_iataCodes)
    terminals_str = ', '.join(str(terminal) if terminal is not None else "" for terminal in departure_terminals)
    departure_times_str = ', '.join(str(at) if at is not None else "" for at in departure_times)
    arrival_terminals_str = ', '.join(str(terminal) if terminal is not None else "" for terminal in arrival_terminals)   
    arrival_times_str = ', '.join(str(at) if at is not None else "" for at in arrival_times)
    airline_codes_str = ', '.join(str(carrierCode) if carrierCode is not None else "" for carrierCode in airline_codes)
    blacklists_str = ', '.join(str(blacklist) for blacklist in blacklists)

    number_of_stops = max(0, len(segments) - 1)
    
    return duration, iataCodes_str, terminals_str, number_of_stops, departure_durations, arrival_terminals_str, departure_times_str, arrival_times_str, airline_codes_str, blacklists_str

# Read CSV file and process each row
with open('flight_search.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    output_headers = ['Duration', 'Departure IATACodes', 'Departure Terminals', 'Number of Stops', 'layover durations', 'Arrival Terminals', 'Departure Times', 'Arrival Times', 'Airline', 'Blacklist']
    
    with open('itinerary.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(output_headers)
        
        for row in csv_reader:
            itinerary_json = row['itineraries']
            itinerary_data = json.loads(itinerary_json)[0]
            
            duration, departure_iataCodes, departure_terminals, number_of_stops, departure_durations, arrival_terminal, departure_times, arrival_times, airline_codes, blacklists = extract_fields(itinerary_data)
            
            writer.writerow([duration, departure_iataCodes, departure_terminals, number_of_stops, departure_durations, arrival_terminal, departure_times, arrival_times, airline_codes, blacklists])

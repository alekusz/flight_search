import json
import csv
from collections import defaultdict

# Function to extract all possible fields from JSON data
def extract_fields(json_data):
    amenities_fields = defaultdict(list)  # To collect all unique amenity types
    
    # First pass to determine all unique amenity types
    for data in json_data:
        fare_details_by_segment = data.get("fareDetailsBySegment", [])
        for segment in fare_details_by_segment:
            amenities_list = segment.get("amenities", [])
            for amenity in amenities_list:
                amenities_fields[amenity.get("amenityType")].append({
                    "description": amenity.get("description", None),
                    "isChargeable": amenity.get("isChargeable", None),
                    "amenityProvider": amenity.get("amenityProvider", {}).get("name", None)
                })
    
    extracted_data = []
    for data in json_data:
        traveler_id = data.get("travelerId", None)
        fare_option = data.get("fareOption", None)
        traveler_type = data.get("travelerType", None)
        
        price = data.get("price", {})
        currency = price.get("currency", None)
        total = price.get("total", None)
        base = price.get("base", None)
        
        fare_details_by_segment = data.get("fareDetailsBySegment", [])
        
        segment_ids = []
        cabins = []
        fare_bases = []
        branded_fares = []
        branded_fare_labels = []
        classes = []
        included_checked_bags_quantities = []
        
        # Dictionary to hold amenities for each segment
        amenities_by_type = defaultdict(lambda: defaultdict(list))
        
        for segment in fare_details_by_segment:
            segment_ids.append(segment.get("segmentId", None))
            cabins.append(segment.get("cabin", None))
            fare_bases.append(segment.get("fareBasis", None))
            branded_fares.append(segment.get("brandedFare", None))
            branded_fare_labels.append(segment.get("brandedFareLabel", None))
            classes.append(segment.get("class", None))
            included_checked_bags = segment.get("includedCheckedBags", {})
            included_checked_bags_quantities.append(included_checked_bags.get("quantity", None))
            
            # Extracting amenities
            amenities_list = segment.get("amenities", [])
            for amenity in amenities_list:
                amenity_type = amenity.get("amenityType", None)
                amenities_by_type[amenity_type]["description"].append(amenity.get("description", None))
                amenities_by_type[amenity_type]["isChargeable"].append(amenity.get("isChargeable", None))
                amenities_by_type[amenity_type]["amenityProvider"].append(amenity.get("amenityProvider", {}).get("name", None))
        
        # Flatten amenities_by_type for CSV output
        flattened_amenities = {}
        for amenity_type, amenity_details in amenities_by_type.items():
            flattened_amenities[f"{amenity_type}_description"] = '; '.join(amenity_details["description"])
            flattened_amenities[f"{amenity_type}_isChargeable"] = '; '.join(map(str, amenity_details["isChargeable"]))
            flattened_amenities[f"{amenity_type}_amenityProvider"] = '; '.join(amenity_details["amenityProvider"])
        
        extracted_data.append((traveler_id, fare_option, traveler_type, currency, total, base, segment_ids, cabins, 
                               fare_bases, branded_fares, branded_fare_labels, classes, included_checked_bags_quantities, 
                               flattened_amenities))
    return extracted_data, amenities_fields

# Read CSV file and process each row
with open('flight_search.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Pass through the data once to determine all unique amenities
    amenities_fields = defaultdict(list)
    for row in csv_reader:
        json_column = row['travelerPricings']  
        json_data = json.loads(json_column)
        _, single_amenities_fields = extract_fields(json_data)
        for k, v in single_amenities_fields.items():
            amenities_fields[k].extend(v)
    
    # Define output headers
    output_headers = ['Traveler ID', 'Fare Option', 'Traveler Type', 'Currency', 'Total Price', 'Base Price', 
                      'Segment IDs', 'Cabins', 'Fare Bases', 'Branded Fares', 'Branded Fare Labels', 
                      'Classes', 'Included Checked Bags Quantities']
    
    # Add unique amenity types to headers
    for amenity_type in amenities_fields.keys():
        output_headers.append(f"{amenity_type}_description")
        output_headers.append(f"{amenity_type}_isChargeable")
        output_headers.append(f"{amenity_type}_amenityProvider")
    
    with open('travelprice.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(output_headers)
        
        csv_file.seek(0)  # Reset file pointer to the start
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            json_column = row['travelerPricings']  # replace 'your_json_column' with the actual column name
            json_data = json.loads(json_column)
            
            extracted_data, _ = extract_fields(json_data)
            
            for data in extracted_data:
                (traveler_id, fare_option, traveler_type, currency, total, base, segment_ids, cabins, 
                 fare_bases, branded_fares, branded_fare_labels, classes, included_checked_bags_quantities, 
                 flattened_amenities) = data
                
                row_data = [traveler_id, fare_option, traveler_type, currency, total, base, segment_ids, cabins, 
                            fare_bases, branded_fares, branded_fare_labels, classes, included_checked_bags_quantities]
                
                for amenity_type in amenities_fields.keys():
                    row_data.append(flattened_amenities.get(f"{amenity_type}_description", ""))
                    row_data.append(flattened_amenities.get(f"{amenity_type}_isChargeable", ""))
                    row_data.append(flattened_amenities.get(f"{amenity_type}_amenityProvider", ""))
                
                writer.writerow(row_data)

import json
import csv

# Function to extract price fields from JSON Price
def extract_fields(json_data):
    currency = json_data.get("currency", None) # Handle None as there may be some values with empty currency
    total = json_data.get("total", None)
    base = json_data.get("base", None)
    grand_total = json_data.get("grandTotal", None)
    
    fees = json_data.get("fees", [])
    fees_amounts = [fee.get("amount", None) for fee in fees] # extract "amount" from fees
    
    additional_services = json_data.get("additionalServices", [])
    additional_services_amounts = [service.get("amount", None) for service in additional_services] # extract "amount" from additionalServices
    additional_services_types = [service.get("type", None) for service in additional_services] # extract "type" from additionalServices

    return currency, total, base, fees_amounts, grand_total, additional_services_amounts, additional_services_types


# Read CSV file and process each row

# Open flight_search csv to read in information 
with open('flight_search.csv', mode='r') as csv_file: 
    csv_reader = csv.DictReader(csv_file)
    
    # Give column names to extracted information (in order)
    output_headers = ['Currency', 'Total Price', 'Base Price', 'Fee Amount', 'Grand Total Price', 'Additional fees', 'Fee Type']
    
    # create new CSV 
    with open('price.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(output_headers)
        
        # Process each row 
        for row in csv_reader:
            price_json = row['price']
            price_data = json.loads(price_json)
            
            currency, total, base, fees_amounts, grand_total, additional_services_amounts, additional_services_types = extract_fields(price_data)
            
            writer.writerow([currency, total, base, fees_amounts, grand_total, additional_services_amounts, additional_services_types])

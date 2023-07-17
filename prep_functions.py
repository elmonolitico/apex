import pandas as pd
import requests
import json
import time
from prep_functions import calculate_processing_time, categorize_processing_time, calculate_profit_margin, calculate_unit_price_sale, calculate_unit_profit, calculate_unit_cost, calculate_cost

API_TOKEN = ""
API_URL = ""

def upload_data_to_api(df):
    api_token = API_TOKEN
    url = API_URL

    payload = json.dumps({
        "collection": "PAPELERIA",
        "database": "APEX",
        "dataSource": "Cluster0",
        "documents": df.to_dict(orient='records')
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': api_token
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response_data = response.json()
        if response.ok:
            print("Data uploaded successfully")
        else:
            print(f"Data upload failed: {response_data['message']}")
    except Exception as e:
        print(f"Data upload failed: {str(e)}")

def process_and_upload_data(df):
    df = calculate_processing_time(df)
    df = categorize_processing_time(df)
    df = calculate_profit_margin(df)
    df = calculate_unit_price_sale(df)
    df = calculate_unit_profit(df)
    df = calculate_unit_cost(df)
    df = calculate_cost(df)

    chunk = 50
    start = 0
    for a in range(chunk, len(df), chunk):
        print(start)
        print(a)
        upload_data_to_api(df[start:a])
        start = a + 1
        time.sleep(1)  # Sleep for 1 second between uploads

# Read the dataset from the CSV file
df = pd.read_csv('EXPORT_PAPELERIA.csv')

# Process and upload the data
process_and_upload_data(df)
import os
import requests
import pandas as pd
from google.cloud import storage
from datetime import date  # Import only 'date' from 'datetime'

# Google cloud Credentials
project_id = 'clean-circle-391119'
bucket_name = 'thd_de_mock_api_data'
# Use 'date.today()' for the current date and ensure there's no 'datetime' reference
destination_blob_name = f"sales_data_{date.today().strftime('%Y%m%d')}.csv"


def request_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []


def save_to_csv(data, output_file):
    df = pd.DataFrame(data)  # Change ps.DataFrame to pd.DataFrame for pandas
    df.to_csv(output_file, index=False)


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}")


def main():
    url = 'https://671c3d3d2c842d92c38271ad.mockapi.io/api/v1/sales'
    data = request_data(url)

    if data:
        output_filepath = 'sales_data.csv'
        save_to_csv(data, output_filepath)
        print('Data saved to CSV')
        upload_to_gcs(bucket_name, output_filepath, destination_blob_name)


if __name__ == "__main__":
    main()
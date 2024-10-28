# Mock API Data Pipeline with Airflow and Google Cloud

This repository contains code to fetch data from a mock API, store it as a CSV file in Google Cloud Storage, and schedule this process daily using Apache Airflow. This project demonstrates how to set up a basic ETL pipeline using Airflow, Python, and Google Cloud services.

## Project Structure

- **`api_request.py`**: Fetches data from the mock API, saves it as a CSV file, and uploads it to Google Cloud Storage.
- **`dag.py`**: Airflow DAG file that schedules the `api_request.py` script as a task using Airflow's `PythonOperator`.
- **`requirements.txt`**: Lists the necessary Python packages for the project.

## API Structure

The mock API used in this project provides sales data, which includes product details, sales information, and location metadata. The API endpoint is `https://[project_secret].mockapi.io/api/v1/sales`.

### API Endpoint
- **URL**: `https://[project_secret].mockapi.io/api/v1/sales`
- **Method**: GET

### Sample Response Data

The data returned by the API is in JSON format. Here is an example of the structure:

```json
[
  {
    "product_name": "Tasty Steel Ball",
    "sale_id": "0776764b-b483-49c9-855a-7940f535e5a4",
    "sale_date": "2024-10-25T20:31:53.515Z",
    "quantity_sold": "2",
    "revenue": 27910,
    "category": "Refined",
    "region": "fr_BE",
    "id": "1"
  },
  {
    "product_name": "Unbranded Plastic Towels",
    "sale_id": "43eed79d-4966-4006-bd38-7c775068d5d3",
    "sale_date": "2024-10-26T00:36:31.861Z",
    "quantity_sold": "8",
    "revenue": 69788,
    "category": "Intelligent",
    "region": "ge",
    "id": "2"
  }
]
```

## Files and Purpose

### `api_request.py`

This script performs the following steps:
1. **Fetch Data**: Retrieves data from the mock API at `https://[project_secret].mockapi.io/api/v1/sales`.
2. **Save to CSV**: Converts the data into a CSV file.
3. **Upload to Google Cloud Storage**: Uploads the CSV file to a specified GCS bucket.

#### Main Functions
- `request_data(url)`: Fetches data from the provided URL.
- `save_to_csv(data, output_file)`: Saves the data to a CSV file.
- `upload_to_gcs(bucket_name, source_file_name, destination_blob_name)`: Uploads the CSV file to a GCS bucket.

### `dag.py`

This Airflow DAG script defines a daily job to run the `api_request.py` script.

- **`default_args`**: Specifies Airflow DAG settings such as retry attempts and start date.
- **`run_script_task`**: Defines a task that runs `api_request.py` using Airflow’s `PythonOperator`.

### `requirements.txt`

Lists the Python dependencies required for the project:
- **apache-airflow**: Manages the task scheduling and orchestration.
- **pandas**: Handles data transformation and saves data as a CSV.
- **requests**: Fetches data from the API.
- **google-cloud-storage**: Enables interactions with Google Cloud Storage.

## Setup and Usage

### Prerequisites

1. **Google Cloud Project** with BigQuery and Cloud Storage enabled.
2. **Apache Airflow** installed, or use Google Cloud Composer to manage the DAG.
3. **Google Cloud SDK** and service account JSON key for Google Cloud authentication.
4. **Python 3.7+** and `pip` installed.

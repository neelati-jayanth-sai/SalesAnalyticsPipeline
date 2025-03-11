import functions_framework
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import os

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]
    
    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    
    table_id = "orders"  
    
    # Call the function to load CSV file to BigQuery
    load_csv_to_bigquery(bucket, name, table_id)

def load_csv_to_bigquery(bucket_name, file_name, table_id):
    """
    Loads a CSV file from Google Cloud Storage to BigQuery.
    Creates the table if it doesn't exist.
    
    Args:
        bucket_name: The name of the GCS bucket
        file_name: The name of the CSV file in the bucket
        table_id: The ID of the table to load data into
    """
    try:
        # Initialize BigQuery client
        bq_client = bigquery.Client()
        
        # Configure the dataset
        dataset_id = "dataset_name" #Replace with your dataset name  
        
        # Make sure the dataset exists
        dataset_ref = bq_client.dataset(dataset_id)
        try:
            bq_client.get_dataset(dataset_ref)
        except NotFound:
            # Create the dataset if it doesn't exist
            dataset = bigquery.Dataset(dataset_ref)
            dataset.location = "US"  # Set the dataset location
            bq_client.create_dataset(dataset, timeout=30)
            print(f"Created dataset {dataset_id}")
        
        # Create table reference
        table_ref = dataset_ref.table(table_id)
        
        # Check if table exists
        try:
            bq_client.get_table(table_ref)
            print(f"Table {table_id} already exists")
        except NotFound:
            print(f"Table {table_id} not found, it will be created")
        
        # Configure the load job for CSV
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip header row
            autodetect=True,      # Auto-detect schema
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  # Overwrite if exists
        )
        
        # URI for the GCS file
        gcs_uri = f"gs://{bucket_name}/{file_name}"
        
        # Start the load job
        load_job = bq_client.load_table_from_uri(
            gcs_uri, table_ref, job_config=job_config
        )
        
        # Wait for the job to complete
        load_job.result()
        
        # Get the table and print info
        table = bq_client.get_table(table_ref)
        print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {dataset_id}.{table_id}")
        
    except Exception as e:
        print(f"Error loading CSV file to BigQuery: {e}")
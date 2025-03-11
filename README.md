# SalesAnalyticsPipeline

This full-stack sales analytics pipeline streamlines the process of collecting, processing, and visualizing sales data to enhance business insights. It allows sales data to be inputted through an intuitive web-based user interface built with Flask. The collected data is then stored in Google Cloud Storage (GCS) for reliable, scalable, and secure storage. Once in GCS, the data is automatically loaded into BigQuery for processing and analysis, where it is organized, cleaned, and transformed for querying and reporting. The final step involves visualizing key insights using Looker, which provides detailed, interactive, and real-time reports to empower businesses to make data-driven decisions.

## Tech Stack Used
- Python
- Flask
- Google Cloud Storage (GCS)
- Cloud Run
- BigQuery
- Looker

## Step-by-Step Guide

### Step 1: Generating Dummy Data Using Faker
1. Install the required dependencies using:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the script to generate dummy sales data for 10 days:
   ```sh
   python generate_dummy_data.py
   ```
3. Modify the start date in the script if you want to generate data for a longer period.

### Step 2: Creating the Web UI and Setting Up a GCS Bucket
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the **Navigation Menu** (top left corner).
3. Navigate to **Cloud Storage** and select **Buckets**.
4. Click **Create Bucket** and provide a unique bucket name. Leave other options as default and click **Create**.
5. Copy the bucket name.

#### Setting Up the Web UI
1. Refer to `app.py` for the complete UI code.
2. Install dependencies using:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add the following variable:
   ```sh
   GCS_BUCKET_NAME=<your-bucket-name>
   GCS_PROJECT_ID=<your-project-id>
   ```
4. To authenticate with Google Cloud, install the Google Cloud SDK and run:
   ```sh
   gcloud auth application-default login
   ```
5. Run the Flask application:
   ```sh
   python app.py
   ```
6. Open the URL provided in the terminal to access the web UI.
7. Upload a file and verify if it has been successfully uploaded to the GCS bucket via the Google Cloud Console.

### Step 3: Deploying a Cloud Run Function with a Trigger
1. Navigate to **Cloud Run** in the Google Cloud Console.
2. Click **Create Service** and ensure you have selected **Cloud Functions**.
3. Provide a service name.
4. Change the runtime to **Python 3.11**.
5. Click **Add Trigger** and choose **Cloud Storage Trigger**.
6. Modify the trigger name if needed.
7. Set the event type to `google.cloud.storage.object.v1.finalized`.
8. Select your bucket by using **Browse**.
9. Click **Save Trigger**, then click **Create**.

### Step 4: Setting Up BigQuery
1. Open **BigQuery** from the **Navigation Menu**.
2. In the **Explorer**, find your project and click on the three dots next to it.
3. Click **Create Dataset**.
4. Provide a dataset name and click **Create Dataset**.

### Step 5: Configuring the Cloud Function
1. Open the Cloud Run service created in Step 3.
2. Click **Source**.
3. Copy the code from `main.py` in the `service-load-data` folder.
4. Copy the dependencies from `requirements.txt`.
5. Replace the dataset name in the code with your dataset name.
6. Click **Save and Redeploy**.
7. Delete the previously uploaded data from the GCS bucket and re-upload a new file from the web UI.
8. In BigQuery, under your project and dataset, a new table will be created with the uploaded data.

### Step 6: Querying Data in BigQuery
1. Go to **BigQuery**.
2. Under your project and dataset, find the newly created table.
3. Click **Query** to perform SQL queries on the data.
4. Use aggregation functions and save the queries as **Views** for better analysis.

---

By following these steps, you will successfully set up an end-to-end sales analytics pipeline that collects, processes, and visualizes sales data using Google Cloud services. 🚀


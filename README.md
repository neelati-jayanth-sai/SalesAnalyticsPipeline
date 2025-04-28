
# SalesAnalyticsPipeline

This full-stack Sales Analytics Pipeline streamlines the process of collecting, processing, and visualizing sales data to unlock powerful business insights.

It allows users to input sales data through an intuitive, web-based user interface built with **Flask**. The collected data is securely stored in **Google Cloud Storage (GCS)**, automatically ingested into **BigQuery** for processing and analysis, and finally visualized using **Looker**, enabling businesses to make data-driven decisions based on detailed, interactive, real-time reports.

---

## 🚀 Tech Stack
- **Python** (Backend and Scripts)
- **Flask** (Web UI)
- **Google Cloud Storage (GCS)** (Storage Layer)
- **Cloud Run** (Serverless Execution)
- **BigQuery** (Data Warehouse)
- **Looker** (Business Intelligence and Dashboards)

---

## 📋 Step-by-Step Setup Guide

### Step 1: Generate Dummy Sales Data
1. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Generate dummy sales data for 10 days:
   ```sh
   python generate_dummy_data.py
   ```
   - *(Optional)* Modify the start date in the script to generate data for a different time range.

---

### Step 2: Set Up the Web UI and GCS Bucket

#### Create a GCS Bucket
1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **Cloud Storage** → **Buckets** → **Create Bucket**.
3. Enter a unique bucket name and leave other options at their defaults.
4. Note down the bucket name.

#### Set Up the Flask Web Application
1. Refer to `app.py` for the Web UI code.
2. Install the dependencies again if not already done:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add:
   ```env
   GCS_BUCKET_NAME=<your-bucket-name>
   GCS_PROJECT_ID=<your-project-id>
   ```
4. Authenticate with Google Cloud:
   ```sh
   gcloud auth application-default login
   ```
5. Run the Flask application:
   ```sh
   python app.py
   ```
6. Open the provided URL and use the UI to upload files.
7. Confirm successful uploads via the GCS Console.

---

### Step 3: Deploy a Cloud Run Service with a Cloud Storage Trigger

1. In the **Google Cloud Console**, navigate to **Cloud Run**.
2. Click **Create Service**.
3. Select **Cloud Functions** during service setup.
4. Set:
   - Runtime: **Python 3.11**
5. Add a trigger:
   - Trigger type: **Cloud Storage**
   - Event type: `google.cloud.storage.object.v1.finalized`
   - Select your bucket.
6. Save and create the service.

---

### Step 4: Set Up BigQuery

1. Open **BigQuery** from the **Navigation Menu**.
2. Under your project, click on the three dots → **Create Dataset**.
3. Provide a dataset name and create it.

---

### Step 5: Configure and Deploy the Cloud Function

1. Open the Cloud Run service created in Step 3.
2. Click **Edit & Deploy New Revision** → **Source Code**.
3. Replace the source code with the contents of `service-load-data/main.py`.
4. Update `requirements.txt` accordingly.
5. In the code, replace placeholder values (like dataset names) with your actual dataset details.
6. Save and deploy.
7. **Test:** Delete any old files in GCS and upload a new file through the Web UI.  
8. **Result:** A new table should automatically appear in BigQuery within your dataset.

---

### Step 6: Query Your Data in BigQuery

1. Open your BigQuery dataset.
2. Click on the created table.
3. Use **Query** to perform SQL analysis.
4. Save common queries as **Views** for easy dashboarding.

---

### Step 7: Connect BigQuery to Looker and Build Dashboards

1. Open **Google Looker Studio** (formerly Data Studio).
2. Click **Create** → **Data Source** → Select **BigQuery**.
3. Connect to your project and dataset.
4. Build custom dashboards and visualizations according to your needs!

---

## 🎯 Outcome

By following these steps, you'll set up a **complete, scalable, and cloud-native sales analytics pipeline** — from data collection to actionable insights — all powered by Google Cloud! 🚀

---

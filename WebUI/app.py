from flask import Flask, request
from google.cloud import storage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set your Google Cloud Storage bucket name from environment variable
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')
# Get the project ID from environment variable
GCS_PROJECT_ID = os.getenv('GCS_PROJECT_ID')

# Initialize the GCS client with project ID
storage_client = storage.Client()
bucket = storage_client.bucket(GCS_BUCKET_NAME)

@app.route('/')
def upload_form():
    return '''
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f0f0f0; margin: 0; padding: 0; }
                .container { max-width: 500px; margin: 50px auto; padding: 20px; background-color: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
                h2 { color: #333; }
                input[type="file"] { margin-bottom: 10px; }
                input[type="submit"] { background-color: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
                input[type="submit"]:hover { background-color: #0056b3; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Upload File to GCS</h2>
                <form method="post" action="/upload" enctype="multipart/form-data">
                    <input type="file" name="file"><br>
                    <input type="submit" value="Upload">
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    return f'File {file.filename} uploaded to GCS successfully!'

if __name__ == '__main__':
    app.run(debug=True)
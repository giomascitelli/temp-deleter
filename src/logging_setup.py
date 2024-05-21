import logging
import os
from datetime import datetime
from azure.storage.blob import BlobServiceClient

sas_url = ''

log_filename = "temp-deleter.log"

# Setting up logging configuration to write to a file and overwrite it every time the script runs
def setup_logging():
    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s', filemode='w')

# Function to upload the log file to Azure Blob Storage
def upload_log_to_blob(log_filename):
    try:
        blob_service_client = BlobServiceClient(account_url=sas_url)
        container_name = sas_url.split('/')[3]

        # Add timestamp to the log file name
        timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        blob_name = f"{os.path.splitext(log_filename)[0]}_{timestamp}{os.path.splitext(log_filename)[1]}"

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        with open(log_filename, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        logging.info(f'Log file successfully uploaded to Azure Blob Storage as {blob_name}')
    except Exception as e:
        logging.error(f"Couldn't upload log file to Azure Blob Storage: {e}")


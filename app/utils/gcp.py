from fastapi import UploadFile
import json
import base64
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.config import settings



BUCKET_NAME = settings.get('BUCKET_NAME')
GOOGLE_APPLICATION_CREDENTIALS_BASE_64 = settings.get('GOOGLE_APPLICATION_CREDENTIALS')
GOOGLE_APPLICATION_CREDENTIALS = json.loads(base64.b64decode(GOOGLE_APPLICATION_CREDENTIALS_BASE_64))
GOOGL_SHEET_RATE_ID = settings.get('GOOGL_SHEET_RATE_ID')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def read_rates():
    credentials = service_account.Credentials.from_service_account_info(
        GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES
    )
    service = build('sheets', 'v4', credentials=credentials)    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=GOOGL_SHEET_RATE_ID, range='RATES!A:AQ').execute()
    try:
        values = result.get('values', [])
        df = pd.DataFrame(values[1:], columns=values[0])
    except:
        df = pd.DataFrame()
    return df

def read_constraints():
    credentials = service_account.Credentials.from_service_account_info(
        GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES
    )
    service = build('sheets', 'v4', credentials=credentials)    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=GOOGL_SHEET_RATE_ID, range='CONSTRAINTS!A:F').execute()
    values = result.get('values', [])
    try:
        df = pd.DataFrame(values[1:], columns=values[0])
        df = df.set_index('Bank')
        df = df.replace({',': ''}, regex=True)
        df = df.apply(pd.to_numeric)    
        df = df.fillna(0)        
    except:
        df = pd.DataFrame()
    return df


def upload_documents(
    file: UploadFile,
    folder: str,
    client_id: int,
    document_type: str,
) -> str:
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_APPLICATION_CREDENTIALS
    )
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(BUCKET_NAME)
    unique_filename = f"{folder}/client_id:_{client_id}_document_type_{document_type}"
    blob = bucket.blob(unique_filename)
    blob.upload_from_file(file.file, content_type=file.content_type)
    return blob.public_url
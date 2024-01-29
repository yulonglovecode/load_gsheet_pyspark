from google.oauth2 import service_account
from googleapiclient.discovery import build


# Path to your service account JSON key file
json_key_path = '/Users/guanyulong/Documents/pyspark/google_drive_keys.json'

# Load credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file(
    json_key_path, scopes=['https://www.googleapis.com/auth/spreadsheets']
)

# Build the Google Sheets API service
service = build('sheets', 'v4', credentials=credentials)

# Spreadsheet ID (you can find this in the URL of your Google Spreadsheet)
spreadsheet_id = '1hB1M5e-jktPteC1FCZ59cE9df2w8lmjpIqiC2KPM_DQ'


range_name = 'Sheet1!A1:B10'

# Make the request to retrieve values
result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

# Get the values from the response
values = result.get('values', [])

# Print the values
for row in values:
    print(row)
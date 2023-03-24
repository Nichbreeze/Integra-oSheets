from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = ''


def main():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId='17eIc3MhT8Q3rpCyi05U4dEpptPn33dZoo86XozFIK',
                                    range='Página1!A1:f12').execute()
        values = result.get('values', [])
        print (values)


        valores_adicionar=[
            ['funcionando, para, edição, pelo, python'],
        ]
        result = sheet.values().update(spreadsheetId='17eIc3MhT8Q3rpCyi05U4dEpptPn33dZoo86XozFIK',
                                    range='PáginaA1!A12',valueInputOption='USER_ENTERED',
                                    body={'values=valores_adicionar'}).execute()



if __name__ == '__main__':
    main()
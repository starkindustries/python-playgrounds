import os.path
import pprint
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_emails(service):
    results_file = "senders.txt"
    if os.path.exists(results_file):
        print(f"ERROR: results file `{results_file}` already exists. Delete this file and re-run script.")
        return

    query = "before:2020-01-01"
    page_token = None
    
    # Create a dictionary of "senders" to "number of emails from that sender"
    senders = {}

    while True:
        # Fetch emails
        results = service.users().messages().list(userId='me', q=query, pageToken=page_token, maxResults=None).execute()
        messages = results.get('messages', [])        

        # Process messages
        for item in messages:
            message = service.users().messages().get(userId='me', id=item['id']).execute()
            # print(message)
            headers = message['payload']['headers']
            for header in headers:
                if header['name'] == 'From':
                    sender = header['value']                    
                    email_match = re.search(r'<(.*?)>', sender)
                    email = email_match.group(1) if email_match else sender                                        
                    print(f"{sender=}, {email=}")

                    # senders.setdefault(sender, set()).add(item['id'])
                    senders.setdefault(email, 0)
                    senders[email] += 1
        
        # printer = pprint.PrettyPrinter(indent=4)
        # printer.pprint(senders)

        page_token = results.get('nextPageToken')
        if not page_token:
            break
        if len(senders.keys()) > 500:
            break
        print(f"{page_token=}, {len(senders.keys())}")
    
    # end while-loop

    sorted_senders = (sorted(senders.items(), key=lambda item: item[1]))
    with open(results_file, "w") as senders_file:
        for key, value in sorted_senders:
            senders_file.write(f"{key}: {value}\n")


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])
        
        # Get emails:
        get_emails(service)

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
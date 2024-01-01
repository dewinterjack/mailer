import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

SCOPES = ['https://mail.google.com/']
email = 'jackdewinter1@gmail.com'

def authenticate():
  # Authenticate with the Gmail API by loading credentials 
  # from a token pickle file if valid credentials exist, 
  # otherwise go through the OAuth flow to generate new credentials, 
  # save them to a token pickle file, and return a 
  # Gmail API service object.
  creds = None
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)
  return build('gmail', 'v1', credentials=creds)

service = authenticate()
from __future__ import print_function

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


CLIENT_SECRETS_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

# Set the channel ID that you want to fetch videos for
CHANNEL_ID = 'UCK7sq6kGFTz1xixvGupu1jQ'


def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """

    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
    creds = flow.run_local_server(port=0)

    try:
        youtube = build('youtube', 'v3', credentials=creds)

        request = youtube.search().list(
          part='id,snippet',
          channelId=CHANNEL_ID,
          order='date',
          type='video'
        )

        response = request.execute()

        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            print(f'{video_title}: {video_id}')

    except HttpError as err:
        print(err)

main()





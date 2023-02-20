import json
import os

from googleapiclient.discovery import build


# APIKEY = "AIzaSyDWTWr6n9chNNxfe2UElrSkN4HtZ9O2ukg"

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))

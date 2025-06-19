
import os
import time
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CANAL_ID")
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
POST_INTERVAL = 1800

def authenticate_drive():
    credentials_info = json.loads(GOOGLE_CREDENTIALS)
    credentials = service_account.Credentials.from_service_account_info(
        credentials_info, scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build('drive', 'v3', credentials=credentials)
    return service

def list_files(service):
    results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType contains 'image/'",
        pageSize=10, fields="files(id, name)"
    ).execute()
    return results.get('files', [])

def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    file_path = f"/tmp/{file_name}"
    with open(file_path, 'wb') as f:
        f.write(request.execute())
    return file_path

def post_to_telegram(bot, file_path, caption):
    with open(file_path, 'rb') as photo:
        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption)

def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    drive_service = authenticate_drive()

    while True:
        files = list_files(drive_service)
        if not files:
            print("No files found.")
        else:
            for file in files:
                try:
                    file_path = download_file(drive_service, file['id'], file['name'])
                    caption = file['name'].replace("_", " ").replace("-", " ").split('.')[0]
                    post_to_telegram(bot, file_path, caption)
                    print(f"Posted {file['name']}")
                except TelegramError as e:
                    print(f"Failed to send {file['name']}: {e}")
        time.sleep(POST_INTERVAL)

if __name__ == "__main__":
    main()

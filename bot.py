import os
import random
import time
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
    import json
    credentials_info = json.loads(GOOGLE_CREDENTIALS)
    credentials = service_account.Credentials.from_service_account_info(
        credentials_info,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build('drive', 'v3', credentials=credentials)
    return service


def list_images(service):
    results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType contains 'image/'",
        fields="files(id, name)"
    ).execute()
    return results.get('files', [])


def download_image(service, file_id):
    from io import BytesIO
    from googleapiclient.http import MediaIoBaseDownload

    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)
    return fh


def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    drive_service = authenticate_drive()

    while True:
        try:
            files = list_images(drive_service)
            if not files:
                print("Nenhuma imagem encontrada na pasta.")
                time.sleep(POST_INTERVAL)
                continue

            file = random.choice(files)
            image_stream = download_image(drive_service, file['id'])

            bot.send_photo(chat_id=CHANNEL_ID, photo=image_stream, caption=file['name'])
            print(f"Imagem {file['name']} enviada com sucesso!")

            time.sleep(POST_INTERVAL)

        except TelegramError as e:
            print(f"Erro no Telegram: {e}")
            time.sleep(60)
        except Exception as e:
            print(f"Erro geral: {e}")
            time.sleep(60)


if __name__ == "__main__":
    main()
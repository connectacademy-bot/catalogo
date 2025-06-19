import os
import json
import time
import schedule
import logging
from telegram import Bot
from google.oauth2 import service_account
from googleapiclient.discovery import build

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")
CANAL_ID = os.getenv("CANAL_ID")
YUAN_PARA_REAL = float(os.getenv("YUAN_PARA_REAL", 0.76))
YUAN_PARA_EURO = float(os.getenv("YUAN_PARA_EURO", 0.12))
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")
GOOGLE_CREDENTIALS = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON"))

bot = Bot(token=TOKEN)

def job():
    bot.send_message(chat_id=CANAL_ID, text="Postagem automática funcionando!")

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

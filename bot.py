import os
import logging
import time
from telegram import Bot
import schedule

# Configurações
TOKEN = os.getenv("TOKEN")
CANAL_ID = os.getenv("CANAL_ID")

bot = Bot(token=TOKEN)

def job():
    bot.send_message(chat_id=CANAL_ID, text="Bot Fly.io funcionando!")

schedule.every(30).minutes.do(job)

print("Bot rodando no Fly.io...")

while True:
    schedule.run_pending()
    time.sleep(1)
import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_TOKEN = '1659225196:AAG1x4TPMx29kZvk5SHTKlnamsCgOoBTuL0'
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "👋")
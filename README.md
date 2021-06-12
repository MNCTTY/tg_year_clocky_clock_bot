# tg_year_clocky_clock_bot

Send you how many percents of the year are already passed. Not by the request, but by the expiration another percent! 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## How it works:

1. A user send hello message to bot.
2. Bot starts the count of percents.

## .env variables

You need to specify these env variables to run this bot. If you run it locally, you can also write them in `.env` text file.

``` bash
TELEGRAM_TOKEN=  # your bot's token

# optional params
HEROKU_APP_NAME=  # name of your Heroku app for webhook setup
WELCOME_MESSAGE=  # text of a message that bot will write on /start command
```

## Run bot locally

First, you need to install all dependencies:

```bash
pip install -r requirements.txt
```

Then you can run the bot. Don't forget to create `.env` file in the root folder with all required params (read above).

``` bash
python main.py
```
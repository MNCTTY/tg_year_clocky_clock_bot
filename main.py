import telebot
import datetime
import time

from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

from flask import Flask, request
import logging

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(content_types=['text'])
def communication(message):
    
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, я буду прислыать тебе проценты от года")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
    bot.send_message(message.from_user.id, 'тестовое сообщение, после будет твой айди')
    bot.send_message(message.from_user.id, message.from_user.id)
    
    start = datetime.datetime(2021,1,1)
    delta = datetime.timedelta(days=3, hours=15, minutes=36)

    all_100 = []
    for i in range(1,101):
        all_100.append(start+delta*i)

    last_percent = 44 
    
    ### (1) у каждого пользователя он будет свой
    ### можно вычислить по now дате и тому, между чем и чем она находится
    
    
    ### а еесли бот падает, то пользователю его надо перезапускать 
    ### или он сам как-то подтягивается и продолжает молча работать (выяснить)
    
    ### (2) а что с нагрузкой на сервера??? счетчики-то для КАЖДОГО пользователя запускаются, 
    ### а нее для всех сразу
    
    ### а как такая проблема решается для всяких ботов-постеров и все такое??
    
    ### (3) сделать вебхуки вместо полинга, чтобы встроить на heroku
    
    ### (4) кнопка деплоя на хероку вроде работает, надо проверить работоспособность потом итогового кода,
    ### но это последний самый этап


    while True:
        now = datetime.datetime.today()
        now_parsed = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
        if any(now_parsed == ckpt for ckpt in all_100):
            last_percent += 1
            msg = str(last_percent) + '% года!'
            bot.send_message(message.from_user.id, msg)

        time.sleep(60) 

        if last_percent == 100:
            msg = 'Now we did it! Lets do it again?'
            bot.send_message(message.from_user.id, msg)
            break
    
    
# bot.polling(none_stop=True, interval=0)  

# if HEROKU_APP_NAME is None:  # pooling mode
#     print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
#     print("Note: this is not a great way to deploy the bot in Heroku.")

# #     updater.start_polling()
# #     updater.idle()

# else:  # webhook mode
#     print(f"Running bot in webhook mode. Make sure that this url is correct: https://{HEROKU_APP_NAME}.herokuapp.com/")
# #     updater.start_webhook(
# #         listen="0.0.0.0",
# #         port=PORT,
# #         url_path=TELEGRAM_TOKEN,
# #         webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}"
# #     )

# #     updater.idle()

if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}") 
        # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=PORT) #os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)
    

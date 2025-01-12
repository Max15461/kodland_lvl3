import config

import telebot



bot = telebot.TeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "пппп")

@bot.message_handler(commands=['info'])
def send_info(message):
    car = config.Car(2024, "Red")
    bot.reply_to(message, f'cc{car.info()}')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.polling()
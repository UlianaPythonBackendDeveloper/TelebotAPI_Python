import telebot

bot = telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['start','help'])
def send_welcome_message(message):
    bot.reply_to(message,"Hello, how are you?")
 
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    try:
        bot.reply_to(message,"👍")
    except Exception as e:
        print("Ошибка")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text:
        bot.reply_to(message, f"Вы сказали: {message.text}" )


bot.infinity_polling()
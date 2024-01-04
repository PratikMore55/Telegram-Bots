import telebot

Token = "YOUR-BOT-TOKEN"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Welcome to MatMath Bot")
    
@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "This can't be evaluated"
    bot.reply_to(message,msg)

bot.polling()
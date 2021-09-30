import telebot;
bot = telebot.TeleBot('2043844414:AAEG8NR2BDKg7OiLwYyrzhZH0uO8AFJ2NMQ');

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
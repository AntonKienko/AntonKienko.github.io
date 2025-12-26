import telebot

bot = telebot.TeleBot('8510153447:AAH4TXIm2kPtNP8LKACRl9icn7GD5l78u38')


bot.message_handler(commands=['start'])

def main (message):

    bot.send_message (message.chat.id, 'Здравствуйте, для записи на экскурсию нажмите команду reserve')


bot.polling(non_stop=True)
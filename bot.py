import telebot

token = '1350430470:AAHvozkFbmcHy1hGzqTVAOrFc0v4tb1Bln8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello ' + message.from_user.first_name)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я могу поприветствовать а больше ничего не могу')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.from_user.username == 'sashka_gavr':
        bot.send_message(message.chat.id, 'Привет Сашка Гавр мой хозяин')
    if message.from_user.username == 'helnsss':
        bot.send_message(message.chat.id, 'слобакова похудей')
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')
    else:
        bot.send_message(message.chat.id, 'Братан ты почеловечески вообще изъясняться можешь или нет')


bot.polling()
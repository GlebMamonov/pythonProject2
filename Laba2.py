#@four_hundred_rubles_bot
import os;
import telebot;
import random
import array as arr

bot = telebot.TeleBot('6787480235:AAHoX8A9efi6v5IEV10_or6p9Se1dRKiS08')


@bot.message_handler(commands=['start'])
def start_command(message):
    msg = bot.reply_to(message,"Здравствуйте")
@bot.message_handler(commands=['motivate_me'])
def data_command(message):
    x = random.randrange(1,5)
    if (x == 1):
        bot.send_photo(message.chat.id, 'https://avatars.dzeninfra.ru/get-zen_doc/1873797/pub_5e40cb3ee678cb0ce06eb672_5e40cb404a28a11ab2b479ff/scale_1200')
    if (x == 2):
        bot.send_photo(message.chat.id, 'https://i.redd.it/m5g8lcp2a3dy.jpg')
    if (x == 3):
        bot.send_photo(message.chat.id, 'https://images-cdn.9gag.com/photo/a677zxL_700b.jpg')
    if (x == 4):
        bot.send_photo(message.chat.id, 'https://repository-images.githubusercontent.com/258767441/35718a00-8bbb-11ea-9d61-7fcda562c735')
@bot.message_handler()
def list_command(message):
    bot.send_message(message.chat.id,"а?")
bot.polling(none_stop=True, interval=0)
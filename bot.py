import telebot
import webbrowser
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('7890096551:AAFgvsM-QNbH_1BxGy0moD377cyOMjK_MIk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Для продолжения нажмите команду /site')




@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://vsu.by')



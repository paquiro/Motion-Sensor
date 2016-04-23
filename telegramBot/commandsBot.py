# -*- coding: utf-8 -*-

import telebot # Library of Telegram Bot.

import data
from data import configure

config=configure()
bot = telebot.TeleBot(config['telegram']['token'])
admin = int(config['telegram']['admin'])

commands = { # command description used in the "help" command
 'help': 'Shows help menu.'
}

@bot.message_handler(commands=['help'])
def help(message):
    cid = message.chat.id
    if (cid == admin):
        help_text="List of commands:\n"
        for command in commands:
            help_text += "/" + command + ": "
            help_text += commands[command] + "\n"
        bot.reply_to(message, help_text)
    else:
        help_text="I'm sorry. I only can be used by my owner.\nVisit https://github.com/Paco1994/Motion-Sensor for more info."
        bot.reply_to(message, help_text)

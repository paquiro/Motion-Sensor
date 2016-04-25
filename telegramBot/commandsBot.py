# -*- coding: utf-8 -*-

import telebot # Library of Telegram Bot.
from telebot import types # for keyboards

import data
import os #for ffmpeg
import sys
import datetime
from data import configure

config=configure()
bot = telebot.TeleBot(config['telegram']['token'])
admin = int(config['telegram']['admin'])

commands = { # command description used in the "help" command
 'help': 'Shows help menu.'
}

@bot.message_handler(commands=['start'])
def start(message):
    cid = message.chat.id
    f = open('users.txt', 'a')
    f.write(str(cid)+"\n")
    f.close()
    if (cid == admin):
        bot.reply_to(message, "Welcome! Feel more safe with me.")
    else:
        text_to_send="I'm sorry. I only can be used by my owner.\nVisit https://github.com/Paco1994/Motion-Sensor for more info."
        bot.reply_to(message, text_to_send)

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

@bot.message_handler(commands=['cameraOn'])
def cameraOn(message):
    pass
    #TODO

@bot.message_handler(commands=['cameraOff'])
def cameraOff(message):
    pass
    #TODO

@bot.message_handler(commands=['record'])
def record(message):
    cid = message.chat.id
    if (cid == admin):
        args = message.text[7:]
        vArgs = args.split()
        if (len(vArgs) == 0):#if the message is '/record'
            fileName=datetime.datetime.now().strftime('%d-%m-%Y_%X') + '.avi'
            #commandRecord='ffmpeg -f v4l2 -i /dev/video0 -f alsa -i hw:1 -acodec mp2 -r 60 -t 5 records/'+fileName
            commandRecord='ffmpeg -f v4l2 -i /dev/video0 -r 60 -t 5 records/'+fileName
            os.system(commandRecord)
            bot.send_document(cid, open('records/' + fileName, 'rb'), reply_to_message_id=message.id)
        elif (len(vArgs) == 1):#if the message is 'record arg'
            try:
                int(vArgs[0])
                #os.system('ffmpeg -f v4l2 -i /dev/video0 -f alsa -i hw:1 -acodec mp2 -r 60 -t 5 records/$(date \'+%d-%m-%Y_%X\').avi')
                os.system('ffmpeg -f v4l2 -i /dev/video0 -r 60 -t 5 records/$(date \'+%d-%m-%Y_%X\').avi')
            except IndexError:
                bot.reply_to(message, "Argument of /record must be a number. It represents the number of seconds you want to record")
            except:
                text_error = "Se ha producido un error no contemplado. Por favor, envíe el error a mi creador: @pavhjs\n"
                text_error += "```\n" + str(sys.exc_info()) + "```"
                bot.reply_to(message, text_error, parse_mode="Markdown")
        else:
            bot.reply_to(message, "/record excepts only an argument. It represents the number of seconds you want to record")
    else:
        help_text="I'm sorry. I can only be used by my owner.\nVisit https://github.com/Paco1994/Motion-Sensor for more info."
        bot.reply_to(message, help_text)

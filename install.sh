#!/bin/bash

if [ $EUID != 0 ]
then
    echo -e "\E[31mThis script should be run using sudo or as the root user because we need to install libraries\e[0m"
    exit 1
fi

python -c "import telebot" 2> /dev/null
if [ $? != 0 ]
then
  pip install pyTelegramBotAPI
fi

python -c "import simpleyaml" 2> /dev/null
if [ $? != 0 ]
then
  pip install simpleyaml
fi

if [ ! -d telegramBot/config ]
then
  mkdir telegramBot/config
fi

if [ ! -f telegramBot/config/parameters.yml ]
then
  echo -e "\E[32mWhat is your Telegram Bot Token? \e[0m"
  read token
  echo -e "\E[32mWhat is your Telegram id? \e[0m"
  read id
  echo -e "telegram:\n   token: '$token'\n   admin: '$id'" > telegramBot/config/parameters.yml
fi

python -c "import cv2" 2> /dev/null
if [ $? != 0 ]
then
  apt-get install python-opencv
fi

if [ ! -d telegramBot/media ]
then
  mkdir -p telegramBot/media/video telegramBot/media/photo
fi

echo -e "\E[32mAlready up to date! If you have any problem, contact me in Telegram: \E[34m@pavhjs\e[0m"

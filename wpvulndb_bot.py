#!venv/bin/python
# -*- coding: utf-8 -*-

import requests
import telebot

FILENAME_CURRENT_ID = '/home/flash/home/bot/last_known_id.txt'

BOT_TOKEN = '1234567890:AAG74zgy*********************'
URL = 'https://wpvulndb.com/vulnerabilities/'
bot = telebot.TeleBot(BOT_TOKEN)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def check_url():
    with open(FILENAME_CURRENT_ID, 'rt') as file:
        last_id = int(file.read())
    url = '{!s}{!s}'.format(URL, last_id)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('Status: %d' % response.status_code)
        print('Найдена новая уязвимость: %s' % last_id)
        message = 'Найдена новая уязвимость: %s' % url
        bot.send_message(257090961, message)
        bot.send_message(164679790, message)
        last_id += 1
        with open(FILENAME_CURRENT_ID, 'wt') as file:
            file.write(str(last_id))
    return response.status_code


while check_url() == 200:
    check_url()
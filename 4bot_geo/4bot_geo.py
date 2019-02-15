#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
from socket import timeout
import os
def link():
    req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
    time.sleep(2)
    try:
        page=urlopen(req,timeout=10).read()
        time.sleep(2)
        soup = BeautifulSoup(page,"html.parser")
        time.sleep(1)
        data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
        link = (data["body"][5]['magazine_package']['sub_story_details']['sub_stories'][1]['uri'])
        return link
    except Exception:
        pass
def post():
    try:
        BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
        CHANNEL_NAME = os.environ.get("CHANNEL_NAME", None)
        time.sleep(1)
        bot = telebot.TeleBot(BOT_TOKEN)
        time.sleep(1)
        bot.send_message(CHANNEL_NAME, c)
        time.sleep(1)
    except Exception:
        pass
a=""
b=""
c=link()
while True:
	time.sleep(1)
	if a == c:
		print("The strings are the same: "+str(a))
		time.sleep(5)
		link()
		time.sleep(5)
		c=link()
		time.sleep(9560)
		time.sleep(360)
	elif b == c:
		print("The strings are the same b: "+str(b))
		time.sleep(5)
		link()
		time.sleep(5)
		c=link()
		time.sleep(9560)
		time.sleep(360)
	else:
		print("The strings are not the same")
		post()
		print (c)
		a=b
		b=c


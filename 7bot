#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
from socket import timeout
def link():
    req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
    time.sleep(2)
    try:
        page=urlopen(req,timeout=10).read()
        time.sleep(2)
        soup = BeautifulSoup(page,"html.parser")
        time.sleep(1)
        data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
        link = (data["body"][0]['homepage_package']["cards"][0]['uri'])
        return link
    except Exception:
        pass
def post():
    try:
        BOT_TOKEN ="681010915:AAFmaiTSpNN7DfVVY3Bp2pTjuHtg-PsccfE"
        CHANNEL_NAME = "@natgeofeed"
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
		time.sleep(360)
	elif b == c:
		print("The strings are the same b: "+str(b))
		time.sleep(5)
		link()
		time.sleep(5)
		c=link()
		time.sleep(360)
	else:
		print("The strings are not the same")
		post()
		print (c)
		a=b
		b=c


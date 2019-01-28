#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
from socket import timeout
import re
def link():
    req = Request('https://www.instagram.com/natgeo/', headers={'User-Agent': 'Mozilla/62.0'})
    time.sleep(2)
    page=urlopen(req,timeout=10).read()
    try:
        soup = BeautifulSoup(page,"html.parser")
        data = soup.find('script', type='text/javascript').find_next('script', type='text/javascript').find_next('script', type='text/javascript').find_next('script', type='text/javascript').text
        time.sleep(1)
        json_data=json.loads(data[21:-1])
        linktmp = (json_data['entry_data']['ProfilePage'][0]["graphql"]['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode'])
        link='https://www.instagram.com/p/'+linktmp
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


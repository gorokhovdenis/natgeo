#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
from socket import timeout
import re
import os
import redis
def link():
        try:
                req = Request('https://www.instagram.com/natgeo/', headers={'User-Agent': 'Mozilla/62.0'})
                time.sleep(2)
                page=urlopen(req,timeout=10).read()
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
                BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
                CHANNEL_NAME = os.environ.get("CHANNEL_NAME", None)
                time.sleep(1)
                bot = telebot.TeleBot(BOT_TOKEN)
                time.sleep(1)
                bot.send_message(CHANNEL_NAME, link())
                time.sleep(1)
        except Exception:
                pass
def getlastpost():
        redis_host = "redis-server"
        redis_port = 6379
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        msg = r.get("insta:last")
        return msg
def setlastpost():
        try:
                redis_host = "redis-server"
                redis_port = 6379
                r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
                r.set("insta:last", link())
        except Exception:
                pass
while True:
	if link() == getlastpost():
		print("The url is already posted")
		link()
		time.sleep(1360)
	else:
		print("The strings are not the same")
		post()
		setlastpost()
		print (link())
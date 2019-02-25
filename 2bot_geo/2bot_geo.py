#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
from socket import timeout
import os
import redis
def link():
        req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
        time.sleep(2)
        try:
                page=urlopen(req,timeout=10).read()
                time.sleep(2)
                soup = BeautifulSoup(page,"html.parser")
                time.sleep(1)
                data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
                link = (data["body"][0]['homepage_package']["cards"][1]['uri'])
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
        msg = r.get("2geo:last")
        return msg
def setlastpost():
        try:
                redis_host = "redis-server"
                redis_port = 6379
                r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
                r.set("2geo:last", link())
        except Exception:
                pass
while True:
	if link() == getlastpost() or link() == 'None':
		print("The url is already posted")
		link()
		time.sleep(1360)
	else:
		print("The strings are not the same")
		post()
		setlastpost()
		print (link())
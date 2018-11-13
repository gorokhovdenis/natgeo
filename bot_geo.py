#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
def link():
	req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
	time.sleep(2)
	page=urlopen(req).read()
	time.sleep(2)
	soup = BeautifulSoup(page,"html.parser")
	time.sleep(1)
	data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
	link = (data["body"][0]['homepage_package']["list"]['stories'][0]['uri'])
	return link
def post():
	BOT_TOKEN ="681010915:AAFmaiTSpNN7DfVVY3Bp2pTjuHtg-PsccfE"
	CHANNEL_NAME = "@natgeographlc"
	time.sleep(1)
	bot = telebot.TeleBot(BOT_TOKEN)
	time.sleep(1)
	bot.send_message(CHANNEL_NAME, c)
	time.sleep(1)

with open('/home/den/natgeo/url', 'r') as f:
	s=f.readlines()
c=link()
if s[0] == c:
	print("The strings are the same")
else:
	post()
	with open('/home/den/natgeo/url', 'w') as f:
		f.write(c)

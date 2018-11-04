from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import json
def link():
    try:
        req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
        time.sleep(2)
        page=urlopen(req).read()
        time.sleep(2)
        soup = BeautifulSoup(page,"html.parser")
        time.sleep(1)
        data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
        link = (data["body"][0]['homepage_package']["list"]['stories'][0]['uri'])
        return link
    except:
        print ("can't get webpage")
        time.sleep(100)

def post():
    try:
	    BOT_TOKEN ="681010915:AAFmaiTSpNN7DfVVY3Bp2pTjuHtg-PsccfE"
	    CHANNEL_NAME = "@natgeographlc"
	    time.sleep(1)
	    bot = telebot.TeleBot(BOT_TOKEN)
	    time.sleep(1)
	    bot.send_message(CHANNEL_NAME, c)
	    time.sleep(180)
    except:
        print ("post error")

a=""
b=""
c=link()
while True:
	time.sleep(2)
	if a == c:
		print("The strings are the same a")
		time.sleep(5)
		link()
		time.sleep(5)
		c=link()
		time.sleep(1360)
	elif b == c:
		print("The strings are the same b")
		time.sleep(5)
		link()
		time.sleep(5)
		c=link()
		time.sleep(1360)
	else:
		print("The strings are not the same")
		post()
		print (c)
		a=b
		b=c

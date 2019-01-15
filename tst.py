#!/usr/bin/python3.6
from urllib.request import Request, urlopen
import certifi
from bs4 import BeautifulSoup
import time
import telebot
import json
def link():
	req = Request('https://www.nationalgeographic.com/', headers={'User-Agent': 'Mozilla/62.0'})
	time.sleep(2)
	page=urlopen(req).read()
	time.sleep(2)
	soup = BeautifulSoup(page,"lxml")
	time.sleep(1)
	data = json.loads(soup.find('script', type='text/json').find_next('script', type='text/json').text)
	link = (data["body"][0]['homepage_package']["cards"][0]['uri'])
	link01 = (data["body"][0]['homepage_package']["cards"][1]['uri'])
	
	
	link03 = (data["body"][5]['magazine_package']['sub_story_details']['sub_stories'][0]['uri'])
	link04 = (data["body"][5]['magazine_package']['sub_story_details']['sub_stories'][1]['uri'])
	link05 = (data["body"][5]['magazine_package']['sub_story_details']['sub_stories'][2]['uri'])
	link06 = (data["body"][0]['homepage_package']["cards"][2]['uri'])
	#link07 = (data["body"][3]['community_package'][0]['pod_card'][0]['pod'][0]['uri'])
	#link08 = (data["body"][4]['society_package']["cards"][1]['uri'])
	print (link)
	print (link01)
	print (link02)
	print (link03)
	print (link04)
	print (link05)
	print (link06)
	#print (link07)
	#print (link08)
link ()

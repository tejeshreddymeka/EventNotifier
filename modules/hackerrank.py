import requests
import json
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime
from dateutil import tz
import time


class Hackerrank:


	def __init__(self):
		self.getHackerrankEvents()

	def saveEvents(self):
		with open("hackerrank.json",'w') as fp:
			json.dump(self.hackerrankEvents,fp)

	def getLocalFormat(self,rawDateTime : str):
		rawDateTime = rawDateTime.split('T')
		rawTime = rawDateTime[1].split(':')
		localFormat = rawDateTime[0] + ' ' + rawTime[0] + ':' + rawTime[1]
		return localFormat

	def getEvents(self):
		with open("hackerrank.json",'r') as fp:
			self.hackerrankEvents = json.load(fp)

	def getEpochTime(self,rawTime : str):
		from_fmt = "%Y-%m-%d %H:%M"
		curTime = datetime.strptime(rawTime,from_fmt)
		epochTime = curTime.timestamp()
		# verfTime = time.strftime(from_fmt,time.localtime(epochTime))
		# print(verfTime)
		return epochTime


	def getHackerrankEvents(self):
		url = 'https://www.hackerrank.com/contests'
		try:
		#if True:
			req = requests.get(url,
				headers={'User-agent': 'Mozilla/5.0'})

			self.hackerrankEvents = []
			if req.status_code == 200:
				pass
				#print(req.text)
				# print("----------------------------------------")
				# print(" Not finished yet.....! Need to scrap the webpage..!")
				# print("----------------------------------------")
			else:
				self.getEvents()
		except:
			self.getEvents()

	def printEvents(self):
		print('---------------------------------------------------------------------------')
		print('                   HACKERRANK EVENTS')
		print('---------------------------------------------------------------------------')

		for event in self.hackerrankEvents:
			print(" [+] {}\n\t-> Starts: {}\n\t-> Finishs: {}\n\t-> url: {}\n\t-> Event Code: {}\n".
				format(event['title'],
					event['start'],
					event['finish'],
					event['url'],
					event['EventCode']
					))

if __name__=="__main__":
	Hackerrank().printEvents()


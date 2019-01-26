import requests
import json
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime
from dateutil import tz
import time


class Codechef:


	def __init__(self):
		self.getCodechefEvents()

	def saveEvents(self):
		with open("codechef.json",'w') as fp:
			json.dump(self.codechefEvents,fp)

	def getLocalFormat(self,rawDateTime : str):
		rawDateTime = rawDateTime.split('T')
		rawTime = rawDateTime[1].split(':')
		localFormat = rawDateTime[0] + ' ' + rawTime[0] + ':' + rawTime[1]
		return localFormat

	def getEvents(self):
		with open("codechef.json",'r') as fp:
			self.codechefEvents = json.load(fp)

	def getEpochTime(self,rawTime : str):
		from_fmt = "%Y-%m-%d %H:%M"
		curTime = datetime.strptime(rawTime,from_fmt)
		epochTime = curTime.timestamp()
		# verfTime = time.strftime(from_fmt,time.localtime(epochTime))
		# print(verfTime)
		return epochTime


	def getCodechefEvents(self):
		url = 'https://www.codechef.com/contests'
		try:
		#if True:
			req = requests.get(url,
				headers={'User-agent': 'Mozilla/5.0'})

			self.codechefEvents = []
			if req.status_code == 200:
				data = req.text
				html = BeautifulSoup(data,features="html.parser")
				header = html.findAll('h3',text="Future Contests")
				if header!=None:
					div = header[0].next_sibling.next_sibling
					rows = div.table.tbody.findAll('tr')
					#print(rows)
					for row in rows:
						event = {}
						
						eventCodeBlock = row.td
						event['EventCode'] = eventCodeBlock.text.strip()
						titleBlock = eventCodeBlock.next_sibling.next_sibling
						
						event['title'] = titleBlock.a.text
						event['url'] = "https://www.codechef.com"+titleBlock.a['href']

						startBlock = titleBlock.next_sibling.next_sibling
						event['start'] = self.getLocalFormat(startBlock['data-starttime'].strip())
						endBlock = startBlock.next_sibling.next_sibling
						event['finish'] = self.getLocalFormat(endBlock['data-endtime'].strip())
						event['epochTime'] = self.getEpochTime(event['start'])
						self.codechefEvents.append(event)

				self.saveEvents()
			else:
				self.getEvents()
		except:
			self.getEvents()

	def printEvents(self):
		print('---------------------------------------------------------------------------')
		print('                   CODECHEF EVENTS')
		print('---------------------------------------------------------------------------')

		for event in self.codechefEvents:
			print(" [+] {}\n\t-> Starts: {}\n\t-> Finishs: {}\n\t-> url: {}\n\t-> Event Code: {}\n".
				format(event['title'],
					event['start'],
					event['finish'],
					event['url'],
					event['EventCode']
					))

if __name__=="__main__":
	Codechef().printEvents()

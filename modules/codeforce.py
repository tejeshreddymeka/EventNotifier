import requests
import json
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime
from dateutil import tz
import time


class Codeforce:


	def __init__(self):
		self.getCodeforceEvents()

	def saveEvents(self):
		with open("codeforce.json",'w') as fp:
			json.dump(self.codeforceEvents,fp)

	def getLocalTime(self,msk:str):
		#rawDateTime is in MSK i,e russia format
		
		msk = datetime.strptime(msk,'%b/%d/%Y %H:%M')
		utc = int(msk.timestamp() - 3*60*60)
		utc = time.strftime('%b/%d/%Y %H:%M',time.localtime(utc))
		
		from_zone = tz.tzutc()
		to_zone = tz.tzlocal()
		utc = datetime.strptime(utc,'%b/%d/%Y %H:%M')
		utc = utc.replace(tzinfo=from_zone)
		local = utc.astimezone(to_zone)
		return local.strftime('%b/%d/%Y %H:%M')
		

	def getEvents(self):
		with open("codeforce.json",'r') as fp:
			self.codeforceEvents = json.load(fp)

	def getEpochTime(self,rawTime : str):
		from_fmt = "%b/%d/%Y %H:%M"
		curTime = datetime.strptime(rawTime,from_fmt)
		epochTime = curTime.timestamp()
		#verfTime = time.strftime(from_fmt,time.localtime(epochTime))
		return epochTime


	def getCodeforceEvents(self):
		url = 'https://codeforces.com/contests'
		try:
		#if True:
			req = requests.get(url,
				headers={'User-agent': 'Mozilla/5.0'})

			self.codeforceEvents = []
			if req.status_code == 200:
				data = req.text
				html = BeautifulSoup(data,features="html.parser")
				tables = html.findAll('div',attrs={'class':'datatable'})
				upcomingTable = tables[0].findAll('table')
				rows = upcomingTable[0].findAll('tr')
				numRows = len(rows)
				for rowInd in range(1,numRows):
					event = {}
					event['contestId'] = rows[rowInd]['data-contestid']
					event['url'] = url+"/"+event['contestId']
					cells = rows[rowInd].findAll('td')
					event['title'] = cells[0].text.strip()
					event['start'] = self.getLocalTime(cells[2].span.text.strip())
					
					event['epochTime'] = self.getEpochTime(event['start'])

					event['duration'] = cells[3].text.strip()
					beforeStart = cells[4].span
					if beforeStart.find('span')==None:
						beforeStart = beforeStart.text
					else:
						beforeStart = beforeStart.span['title']

					event['beforeStart'] = beforeStart.strip()
					beforeReg = cells[5].span
					if beforeReg.find('span')==None:
						beforeReg = beforeReg.text
					else:
						beforeReg = beforeReg.span['title']
					event['beforeReg'] = beforeReg.strip()

					self.codeforceEvents.append(event)

				self.saveEvents()
			else:
				self.getEvents()
		except:
			self.getEvents()

	def printEvents(self):
		print('---------------------------------------------------------------------------')
		print('                   CODEFORCE EVENTS')
		print('---------------------------------------------------------------------------')

		for event in self.codeforceEvents:
			print(" [+] {}\n\t-> Starts: {}\n\t-> Duration: {}\n\t-> Time before Start: {}\n\t-> Time before Registration: {}\n\t-> url:{}".
				format(event['title'],
					event['start'],
					event['duration'],
					event['beforeStart'],
					event['beforeReg'],
					event['url']
					))

if __name__=="__main__":
	Codeforce().printEvents()
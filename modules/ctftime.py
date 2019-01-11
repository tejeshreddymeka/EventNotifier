import requests 
import time
from datetime import datetime
from dateutil import tz
import json

class ctftime:
	"""
		To get Upcomming ctf events from ctftime.org
		Usage:
			ctftime().ctfEvents will return list of events in dict format

		Thanks ctftime.org for providing api.
	"""
	def __init__(self):
		self.getUpcomingCtfEvents()

	def getLocalFormat(self,rawDateTime : str):
		rawDateTime = rawDateTime.split('T')
		rawTime = rawDateTime[1].split(':')
		utc = rawDateTime[0] + ' ' + rawTime[0] + ':' + rawTime[1] + ':' + '00'
		from_zone = tz.tzutc()
		to_zone = tz.tzlocal()
		utc = datetime.strptime(utc,'%Y-%m-%d %H:%M:%S')
		utc = utc.replace(tzinfo=from_zone)
		local = utc.astimezone(to_zone)
		return local.strftime('%Y-%m-%d %H:%M:%S %Z')

	def writeCtfFile(self,events : dict):
		with open('ctftime.json','w') as fp:
			json.dump(events,fp)

	def readCtfFile(self):
		with open('ctftime.json','r') as fp:
			events = json.load(fp)
		return events

	def getEpochTime(self,rawTime : str):
		from_fmt = "%Y-%m-%d %H:%M:%S %Z"
		curTime = datetime.strptime(rawTime,from_fmt)
		epochTime = curTime.timestamp()
		#verfTime = time.strftime(from_fmt,time.localtime(epochTime))
		
		return epochTime


	def printCtfEvents(self):
		print('---------------------------------------------------------------------------')
		print('                       CTF EVENTS')
		print('---------------------------------------------------------------------------')
		for event in self.ctfEvents:
			name = event['title']
			startTime = event['start']
			endTime = event['finish']
			ctfFormat = event['format']
			location = event['location']
			if len(location.strip())==0:
				location = "Online"
			weight = event['weight']
			ctftimeUrl = event['ctftime_url']
			ctfEventUrl = event['url']	
			print("\n{}\n\t->Starts: {}\n\t->Ends: {}\n\t->Format: {}\n\t->Location: {}\n\t->Weight: {}\n\t->Ctftime Url: {}\n\t->Ctf Event Url: {}".format(name,startTime,endTime,ctfFormat,location,weight,ctftimeUrl,ctfEventUrl))
		print('---------------------------------------------------------------------------')
		

	def getUpcomingCtfEvents(self):
		#'https://ctftime.org/api/v1/events/?limit=100&start=1422019499&finish=1423029499'
		url = 'https://ctftime.org/api/v1/events/?limit=100&start='+str(time.time())
		try:
			req = requests.get(url,
				headers={'User-agent': 'Mozilla/5.0'})
			if req.status_code == 200:
				events = req.json()
				for event in events:
					event['epochTime'] = self.getEpochTime(self.getLocalFormat(event['start'])) 
					event['start'] = self.getLocalFormat(event['start'])
					event['finish'] = self.getLocalFormat(event['finish'])
				self.writeCtfFile(events)			
			else:
				events = self.readCtfFile()
		except:
			events = self.readCtfFile()
		self.ctfEvents = events

if __name__=="__main__":
	ctfObj = ctftime()
	ctfEvents = ctfObj.ctfEvents
	ctfObj.printCtfEvents()


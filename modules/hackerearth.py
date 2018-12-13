from requests import Session
import requests
import json
from bs4 import BeautifulSoup
import time
import webbrowser
from datetime import datetime

import warnings
warnings.filterwarnings("ignore",category=UserWarning,module='bs4')


class Hackerearth():
	"""
		To get Upcomming hackathons , hiring and rating challenges from hackerearth.com
		Usage:
			Hackerearth().hackerearthEvents will return list of events in dict format

		Thanks hackerearth.com for providing such a platform for us.
	"""

	def __init__(self): 
		self.getChallenges()
	def writeHackerearthFile(self,events : dict):
		with open('hackerearth.json','w') as fp:
			json.dump(events,fp)

	def readHackerearthFile(self):
		with open('hackerearth.json','r') as fp:
			events = json.load(fp)
		return events

	def getChallenges(self):
		"""
			This will return the all the challenges as list of dict.

		"""

		url = "https://www.hackerearth.com/challenges/"
		try:
			res = requests.get(url,
				headers={
				'Host': 'www.hackerearth.com',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate, br',
				'DNT': '1',
				'Connection': 'keep-alive',
				"Upgrade-Insecure-Requests": "1"
				}
				)

			if res.status_code == 200:
				csrftoken = res.cookies['csrftoken']
				cookies = "; ".join([str(x)+"="+str(y) for x,y in res.cookies.items()])
				session = Session()
				session.head("https://www.hackerearth.com/challenges/")
				response = session.post(
				    url='https://www.hackerearth.com/AJAX/filter-challenges/',
					data = """-----------------------------256531432826495
					Content-Disposition: form-data; name="is_competitive"

					on
					-----------------------------256531432826495
					Content-Disposition: form-data; name="is_hackathon"

					on
					-----------------------------256531432826495
					Content-Disposition: form-data; name="is_hiring"

					on
					-----------------------------256531432826495
					Content-Disposition: form-data; name="submit"

					True
					-----------------------------256531432826495--
					""",
					headers={
					"Host": "www.hackerearth.com",
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
					"Accept": "*/*",
					"Accept-Language": "en-US,en;q=0.5",
					"Accept-Encoding": "gzip, deflate, br",
					"Referer": "https://www.hackerearth.com/challenges/",
					"X-CSRFToken": csrftoken,
					"X-Requested-With" : "XMLHttpRequest",
					"Content-Type" : "multipart/form-data; boundary=---------------------------256531432826495",
					"Content-Length": "463",
					"DNT": "1",
					"Connection": "keep-alive",
					"Cookie" : cookies,
					"TE" : "Trailers"
					})

				if response.status_code == 200:
					data = response.json()
					self.writeHackerearthFile(data)
				else:
					data = self.readHackerearthFile()
			else:
				data = self.readHackerearthFile()
		except:
			data = self.readHackerearthFile()

		#------------remove this block  after uncommenting above code
		# with open('hackerearth.json','r') as fp:
		# 		data = json.load(fp)
		#-----------------
		data = data['data']
		html = BeautifulSoup(data)
		baseUrl = "https://hackerearth.com"

		upcomingChallenges = []
		upcomingChallegesList = html.findAll('div',attrs={'class':'upcoming challenge-list'})
		upcomingChallegesList = upcomingChallegesList[0].findAll('div',attrs={'class':'challenge-card-modern'})
		for upcomingChallenge in upcomingChallegesList:
			block = upcomingChallenge.a.div.next_sibling.next_sibling
			block = block.div
			challengeType = block.text
			challengeType = challengeType.replace("\n","").strip()
			block = block.next_sibling.next_sibling
			name = block.span.text
			startTime = block.next_sibling.next_sibling.div.div.next_sibling.next_sibling.text
			url = upcomingChallenge.a['href']
			if 'http' not in url:
				if url[0] != '/':
					url = baseUrl +'/' + url
				else:
					url = baseUrl + url
			
			challenge = {}
			challenge['title']  = name
			challenge['format'] = challengeType
			challenge['start'] = startTime
			challenge['url'] = url
			challenge['epochTime'] = self.getEpochTime(challenge['start'])
			upcomingChallenges.append(challenge)
			#webbrowser.open_new(url)
			self.hackerearthEvents = upcomingChallenges			


	def getEpochTime(self,rawTime : str):
		rawTime = rawTime[:-4]
		preRawTime = rawTime
		
		curTime = datetime.now()
		curEpoch = curTime.timestamp()
		curYear = curTime.year
		rawTime += " {}".format(curYear)
		from_fmt = "%b %d, %I:%M %p %Y"
		reqTime = datetime.strptime(rawTime,from_fmt)
		epochTime = reqTime.timestamp()

		if epochTime < curEpoch:
			rawTime = preRawTime
			rawTime += " {}".format(curYear+1)
			reqTime = datetime.strptime(rawTime,from_fmt)
			epochTime = reqTime.timestamp()
		#verfTime = time.strftime(from_fmt,time.localtime(epochTime))
		return epochTime
	
	def printHackerearthEvents(self):
		print('---------------------------------------------------------------------------')
		print('                       HACKEREARTH EVENTS')
		print('---------------------------------------------------------------------------')
		for challenge in self.hackerearthEvents:
			print("\n",challenge['title'],
				"\n\t > ",challenge['format'],
				"\n\t > ",challenge['start'],
				"\n\t > ",challenge['url'],
				)
		print('---------------------------------------------------------------------------')

if __name__ == "__main__":
	hackerearthObj = Hackerearth()
	hackerearthEvents = hackerearthObj.hackerearthEvents
	hackerearthObj.printHackerearthEvents()
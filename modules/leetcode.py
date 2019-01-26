from requests import Session
import requests
import json
from bs4 import BeautifulSoup
import time

class Leetcode:

	def __init__(self):
		self.leetcodeEvents = []
		self.getLeetcodeEvents()

	def writeLeetcodeFile(self,events : dict):
		with open('leetcode.json','w') as fp:
			json.dump(events,fp)

	def readLeetcodeFile(self):
		with open('leetcode.json','r') as fp:
			events = json.load(fp)
		return events


	def getLocalTime(self,epochTime : int):
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))


	def getLeetcodeEvents(self):
		url = "https://leetcode.com/contest/"
		try:
			res = requests.get(url,
				headers={
				'Host': 'leetcode.com',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate, br',
				'DNT': '1',
				'Connection': 'keep-alive',
				'Upgrade-Insecure-Requests': '1'
				})
			
			if res.status_code == 200:		
				contentUrl = 'https://leetcode.com/graphql'
				csrftoken = res.cookies['csrftoken']
				cookies = "; ".join([str(x)+"="+str(y) for x,y in res.cookies.items()])
				session = Session()
				session.head(url)
				response = session.post(
				    url=contentUrl,
					data = r'''{"operationName":null,"variables":{},"query":"{\n  brightTitle\n  allContests {\n    containsPremium\n    title\n    cardImg\n    titleSlug\n    description\n    startTime\n    duration\n    originStartTime\n    isVirtual\n    company {\n      watermark\n      __typename\n    }\n    __typename\n  }\n}\n"}''',
					headers={
					'Host': 'leetcode.com',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
					'Accept': '*/*',
					'Accept-Language': 'en-US,en;q=0.5',
					'Accept-Encoding': 'identity',
					'Referer': 'https://leetcode.com/contest/',
					'X-NewRelic-ID': 'UAQDVFVRGwEAXVlbBAg=',
					'content-type': 'application/json',
					'x-csrftoken': csrftoken,
					'Content-Length': '206',
					'DNT': '1',
					'Connection': 'keep-alive',
					'Cookie': cookies, 
					'TE': 'Trailers'
				})
				if response.status_code == 200:
					data = response.json()
					contest = data['data']['allContests'][0]
					#print(contest)
					title = contest['title']
					description = contest['description']
					startTime = contest['startTime']
					duration = contest['duration']
					event = {}
					event['title'] = title
					event['epochTime'] = startTime;
					event['start'] = self.getLocalTime(startTime)
					event['finish'] = self.getLocalTime(startTime+duration)
					event['url'] = url+contest['titleSlug']
					self.leetcodeEvents.append(event)
					self.writeLeetcodeFile(self.leetcodeEvents)
				else:
					self.leetcodeEvents = self.readLeetcodeFile()
			else:
				self.leetcodeEvents = self.readLeetcodeFile()
		except:
			self.leetcodeEvents = self.readLeetcodeFile()			

	def printLeetcodeEvents(self):
		print('---------------------------------------------------------------------------')
		print('                       LEETCODE EVENTS')
		print('---------------------------------------------------------------------------')
		for challenge in self.leetcodeEvents:
			print("\n",challenge['title'],
				"\n\t > ",challenge['start'],
				"\n\t > ",challenge['finish'],				
				"\n\t > ",challenge['url'],
				)
		print('---------------------------------------------------------------------------')

if __name__=="__main__":
	Leetcode().printLeetcodeEvents()



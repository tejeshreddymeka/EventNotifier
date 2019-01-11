import tkinter as tk 
from tkinter.scrolledtext import ScrolledText
import webbrowser
from datetime import datetime
import time


print("Starting Event Notifier .............")

	
from modules.ctftime import ctftime
from modules.hackerearth import Hackerearth
from modules.hackerrank import Hackerrank
from modules.codeforce import Codeforce
from modules.codechef import Codechef
from modules.leetcode import Leetcode

LARGE_FONT = {"Helvetica",10}

class Event():
	"""
		It represet each Event
	"""
	def __init__(self,eventType="None",event={}):
		self.eventType = eventType
		self.event = event
		self.epochTime = event['epochTime']
		self.triggered = 0

def openLink(event):
		ctfUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(ctfUrl)			

def popUp(triggeredEvents):
	root = tk.Tk()
	tk.Tk.iconbitmap(root,default="images\\EventNotifier.ico")
	tk.Tk.wm_title(root,"  Event Notifier App")

	container = tk.Frame(root,bg="#1a1a1a",highlightbackground="lightblue", highlightthickness=1)
	container.pack(side="top",fill="both",expand=True)
	header = tk.Label(container,text="EVENT NOTIFER",font=LARGE_FONT,fg="#00e6e6",bg="#0d0d0d")
	header.pack(side="top",fill="both",padx=2,pady=4,ipady=4)
	text = ScrolledText(container,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",width="60",
					cursor="arrow")
	text.pack(expand=True, fill='both')
	text.insert(tk.INSERT,"\n root",'red')
	text.insert(tk.INSERT," @ ",'white')
	text.insert(tk.INSERT,"Notifier")
	text.insert(tk.INSERT," ># ",'lightblue')
	text.insert(tk.INSERT," get  notifications ")

	for event in triggeredEvents:
		eventType = event.eventType
		text.insert(tk.INSERT,"\n\n\n [ >>>>>   ",'orange')
		text.insert(tk.INSERT,eventType,'white')
		text.insert(tk.INSERT,"   <<<<< ] \n",'orange')
		text.insert(tk.INSERT," ||\n ==> ",'pink')
		event = event.event
		text.insert(tk.INSERT," [+]  ",'orange')
		name = event['title']
		text.insert(tk.INSERT,name,'lightblue')
		if eventType == "CTF":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			endTime = event['finish']
			endTime = "Ends: "+ endTime  + "\n\t>  "
			ctfFormat = "Format: "+event['format'] + "\n\t>  "
			location = "Location: "+event['location'] + "\n\t>  "
			if len(event['location'].strip())==0:
				location = "Location: "+"Online" + "\n\t>  "
			weight = "Weight: "+str(event['weight']) + "\n\t>  "
			description = startTime + endTime + ctfFormat + location

			text.insert(tk.INSERT,description)
			ctftimeUrl = event['ctftime_url']
			ctfEventUrl = event['url']
			text.insert(tk.INSERT,"Event url: ")
			text.insert(tk.INSERT,ctfEventUrl,('link',ctfEventUrl))
			text.insert(tk.INSERT,"\n\t>  CTFtime url: ")
			text.insert(tk.INSERT,ctftimeUrl,('link',ctftimeUrl))
			text.insert(tk.INSERT,"\n")
		
		elif eventType == "HACKEREARTH":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			hackerearthFormat = "Format: "+event['format']
			description = startTime + hackerearthFormat
			text.insert(tk.INSERT,description)
			hackerearthUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,hackerearthUrl,('link',hackerearthUrl))
			text.insert(tk.INSERT,"\n")

		elif eventType == "HACKERRANK":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			description = startTime
			text.insert(tk.INSERT,description)
			hackerrankUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,hackerrankUrl,('link',hackerrankUrl))
			text.insert(tk.INSERT,"\n")


		elif eventType == "CODECHEF":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			text.insert(tk.INSERT,startTime)
			endTime = event['finish']
			endTime = "Ends: "+ endTime  + "\n\t>  "
			text.insert(tk.INSERT,endTime)
			codechefUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,codechefUrl,('link',codechefUrl))
			text.insert(tk.INSERT,"\n")

		elif eventType == "CODEFORCE":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			text.insert(tk.INSERT,startTime)
			duration = "\n\t>  Duration: " + event['duration']
			text.insert(tk.INSERT,duration)
			beforeStartTime = "\n\t>  Before start: " + event['beforeStart']
			text.insert(tk.INSERT,beforeStartTime)
			beforeRegTime = "\n\t>  Before registration: " + event['beforeReg']
			text.insert(tk.INSERT,beforeRegTime)
			codeforceUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,codeforceUrl,('link',codeforceUrl))
			text.insert(tk.INSERT,"\n")

		elif eventType == "LEETCODE":
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			text.insert(tk.INSERT,startTime)
			endTime = event['finish']
			endTime = "Ends: "+ endTime  + "\n\t>  "
			text.insert(tk.INSERT,endTime)
			codechefUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,codechefUrl,('link',codechefUrl))
			text.insert(tk.INSERT,"\n")


	text.tag_config('link',foreground="#3385ff")	
	text.tag_bind('link','<Button-1>',openLink)
	text.tag_config('lightblue',foreground="#00e6e6")
	text.tag_config('red',foreground="red")
	text.tag_config('white',foreground="white")
	text.tag_config('orange',foreground="#ff6600")
	text.tag_config('blue',foreground="#3385ff")
	text.tag_config('pink',foreground="#ff4dd2")
	text.config(state=tk.DISABLED)	


	root.mainloop()

def getEvents():
	print('retriving events......')
	events = []
	
	parameters = getParameters()
	if parameters['ctftime']==1:
		ctfEvents = ctftime().ctfEvents
		for ctfEvent in ctfEvents:
			events.append( Event("CTF",ctfEvent) )

	if parameters['hackerearth']==1:
		hackerearthEvents = Hackerearth().hackerearthEvents
		for hackerearthEvent in hackerearthEvents:
			events.append( Event("HACKEREARTH",hackerearthEvent) )

	if parameters['hackerrank']==1:
		hackerrankEvents = Hackerrank().hackerrankEvents
		for hackerrankEvent in hackerrankEvents:
			events.append( Event("HACKERRANK",hackerrankEvent) )

	if parameters['codechef']==1:
		codechefEvents = Codechef().codechefEvents
		for codechefEvent in codechefEvents:
			events.append( Event("CODECHEF",codechefEvent) )

	if parameters['codeforce']==1:
		codeforceEvents = Codeforce().codeforceEvents
		for codeforceEvent in codeforceEvents:
			events.append( Event("CODEFORCE",codeforceEvent) )
	
	if parameters['leetcode']==1:
		leetcodeEvents = Leetcode().leetcodeEvents
		for leetcodeEvent in leetcodeEvents:
			events.append( Event("LEETCODE",codeforceEvent) )
	
	#testing event ----
	# currentEpoch = datetime.now().timestamp()
	# tempEvent ={}
	# tempEvent['epochTime'] = str( int(currentEpoch) + 2*60)
	# tempEvent['title'] = "testing"
	# temp = Event("None",tempEvent)
	
	# events.append(temp)
	#-----------------	
	events.sort(key=lambda event: int(event.epochTime) )
	# for event in events:
	# 	from_fmt = "%Y-%m-%d %H:%M"
	# 	verfTime = time.strftime(from_fmt,time.localtime(event.epochTime))
	# 	print(verfTime)
	# 	print(event.epochTime,event.eventType)
	return events


def getParameters():
	parameters = {}
	with open("config/beforeEventNotifyInterval.conf",'r') as fp:
		parameters['beforeEventNotifyInterval'] = int(fp.read())  #seconds
	parameters['sleepInterval'] = 5*60
	parameters['retriveInterval'] = 15*60
	parameters['delta'] = 1*60

	with open("config/notificationSettings.conf",'r') as fp: 
		parameters['ctftime'] = int(fp.readline().strip())
		parameters['hackerearth'] = int(fp.readline().strip())
		parameters['hackerrank'] = int(fp.readline().strip())
		parameters['codechef'] = int(fp.readline().strip())
		parameters['codeforce'] = int(fp.readline().strip())
		parameters['leetcode'] = int(fp.readline().strip())
	return parameters

if __name__=="__main__":
	
	events = getEvents()	
	triggeredEvents = []
	currentEpoch = int(datetime.now().timestamp())
	

	prevRetrival = currentEpoch

	while(True):	
		triggeredEvents = []
		parameters = getParameters()
		beforeEventNotifyInterval = parameters['beforeEventNotifyInterval']
		sleepInterval = parameters['sleepInterval']
		retriveInterval = parameters['retriveInterval']
		delta = parameters['delta']

		currentEpoch = int(datetime.now().timestamp())
		if currentEpoch - prevRetrival >= retriveInterval:
			events = getEvents()
			currentEpoch = int(datetime.now().timestamp())
			prevRetrival = currentEpoch

		numEvents = len(events)
		
		if numEvents > 0:
			eventInd = 0
			while(events[eventInd].epochTime <= currentEpoch):
				if(events[eventInd].triggered<=1):				
					triggeredEvents.append(events[eventInd])
					events[eventInd].triggered+=1	
			
				eventInd+=1
			
			checkInd = eventInd

			while(events[eventInd].epochTime <= currentEpoch + beforeEventNotifyInterval):
				if(events[eventInd].triggered==0):				
					triggeredEvents.append(events[eventInd])
					events[eventInd].triggered+=1	
			
				eventInd+=1
			currentEpoch = int(datetime.now().timestamp())

			
			while(events[eventInd].epochTime >= currentEpoch - delta and events[eventInd].epochTime <= currentEpoch+ delta):
				triggeredEvents.append(events[eventInd])
				events[eventInd].triggered+=1	
				eventInd+=1	

			if(len(triggeredEvents)!=0):
				popUp(triggeredEvents)
			if(checkInd<numEvents):
				sInterval = events[checkInd].epochTime - currentEpoch - beforeEventNotifyInterval
				if(sInterval < 0):
					sInterval = events[checkInd].epochTime - currentEpoch
					if(sInterval < 0):
						sInterval = sleepInterval
			else:
				sInterval = sleepInterval
			if sInterval > retriveInterval:
				sInterval = retriveInterval
			print('sleeping for {}....In'.format(sInterval))
			time.sleep(sInterval)
		else:
			print('sleeping for {}....Out'.format(sleepInterval))
			time.sleep(sleepInterval)
			
	

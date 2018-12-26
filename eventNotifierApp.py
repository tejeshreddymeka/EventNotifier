import tkinter as tk 
from tkinter import ttk 
import webbrowser
from tkinter.scrolledtext import ScrolledText
import threading
import time
import os


from modules.ctftime import ctftime
from modules.hackerearth import Hackerearth
from modules.hackerrank import Hackerrank
from modules.codeforce import Codeforce
from modules.codechef import Codechef

#---------- to hide the console window

import win32gui, win32con

#-------------



LARGE_FONT = {"Helvetica",10}

class MyButton(tk.Button):
    
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self['foreground']
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


class EventNotifierApp(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.iconbitmap(self,default="images\\EventNotifier.ico")
		tk.Tk.wm_title(self,"  Event Notifier App")

		container = tk.Frame(self,bg="#0d0d0d",highlightbackground="lightgreen", highlightthickness=1,width=600, height=600)
		container.pack(side="top",fill="both",expand=True)

		sideFrame = tk.Frame(container,bg="#0d0d0d")
		sideFrame.grid(row=0,column=0,padx=10)
		mainFrame = tk.Frame(container, highlightbackground="lightblue", highlightthickness=1)
		mainFrame.grid(row=0,column=1,columnspan=10,rowspan=10)
		homeButton = MyButton(sideFrame,text="Home",command=lambda:self.showFrame(StartPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		homeButton.pack(side="top",pady=10,fill='both')
		ctfButton = MyButton(sideFrame,text="CTFtime",command=lambda:self.showFrame(CtfPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		ctfButton.pack(side="top",pady=10,fill='both')
		hackerearthButton = MyButton(sideFrame,text="   Hackerearth   ",command=lambda:self.showFrame(HackerearthPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		hackerearthButton.pack(side="top",pady=10,fill='both')
		codechefButton = MyButton(sideFrame,text="Codechef",command=lambda:self.showFrame(CodechefPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		codechefButton.pack(side="top",pady=10,fill='both')
		codeforceButton = MyButton(sideFrame,text="Codeforce",command=lambda:self.showFrame(CodeforcePage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		codeforceButton.pack(side="top",pady=10,fill='both')
		hackerrankButton = MyButton(sideFrame,text="Hackerrank",command=lambda:self.showFrame(HackerrankPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		hackerrankButton.pack(side="top",pady=10,fill='both')
		settingsButton = MyButton(sideFrame,text="Settings",command=lambda:self.showFrame(SettingsPage),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen", width=20,font=10)
		settingsButton.pack(side="top",pady=10,fill='both')
		
		self.frames = {}

		for F in (StartPage,
				CtfPage,
				HackerearthPage,
				HackerrankPage,
				CodeforcePage,
				CodechefPage,
				SettingsPage):
			frame = F(mainFrame,self)
			self.frames[F] = frame
			frame.grid(row=0,column=0,sticky="nsew")

		self.showFrame(StartPage)
	def showFrame(self,pageName):
		frame = self.frames[pageName]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent,highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		
		image1 = tk.Label(self,width=850, height=650)
		image1.EventNotifierImage = tk.PhotoImage(file="images\\EventNotifierImage.png")
		image1['image'] = image1.EventNotifierImage
		image1.pack(side="left",expand=False)
		

		
class CtfPage(tk.Frame):

	def __init__(self,parent,controller):
		ctfObj = ctftime()
		ctfEvents =  ctfObj.ctfEvents
		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		heading = tk.Label(self,text="""
============================================================================================
	CTF EVENTS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		text = ScrolledText(self,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",
					cursor="arrow")
		text.pack(expand=True, fill='both')
		text.insert(tk.INSERT,"\n root",'red')
		text.insert(tk.INSERT," @ ",'white')
		text.insert(tk.INSERT,"Notifier")
		text.insert(tk.INSERT," ># ",'lightblue')
		text.insert(tk.INSERT," get ctfevents ")

		for event in ctfEvents:
			text.insert(tk.INSERT,"\n\n [+]  ",'orange')
			name = event['title']
			text.insert(tk.INSERT,name,'lightblue')
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			endTime = event['finish']
			endTime = "Ends: "+endTime  + "\n\t>  "
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
		
		text.tag_config('link',foreground="#3385ff")	
		text.tag_bind('link','<Button-1>',self.openLink)
		text.tag_config('lightblue',foreground="#00e6e6")
		text.tag_config('red',foreground="red")
		text.tag_config('white',foreground="white")
		text.tag_config('orange',foreground="#ff6600")
		
		
		text.config(state=tk.DISABLED)

	def openLink(self,event):
		ctfUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(ctfUrl)			

class CodechefPage(tk.Frame):

	def __init__(self,parent,controller):
		codechefObj = Codechef()
		codechefEvents =  codechefObj.codechefEvents
		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		heading = tk.Label(self,text="""
============================================================================================
	CODECHEF EVENTS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		text = ScrolledText(self,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",
					cursor="arrow")
		text.pack(expand=True, fill='both')
		text.insert(tk.INSERT,"\n root",'red')
		text.insert(tk.INSERT," @ ",'white')
		text.insert(tk.INSERT,"Notifier")
		text.insert(tk.INSERT," ># ",'lightblue')
		text.insert(tk.INSERT," get codechefevents ")

		for event in codechefEvents:
			text.insert(tk.INSERT,"\n\n [+]  ",'orange')
			name = event['title']
			text.insert(tk.INSERT,name,'lightblue')
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			endTime = event['finish']
			endTime = "Ends: "+endTime  + "\n\t>  "
			description = startTime + endTime
			text.insert(tk.INSERT,description)
			text.insert(tk.INSERT,"Event url: ")
			text.insert(tk.INSERT,event['url'],('link',event['url']))
			
		
		text.tag_config('link',foreground="#3385ff")	
		text.tag_bind('link','<Button-1>',self.openLink)
		text.tag_config('lightblue',foreground="#00e6e6")
		text.tag_config('red',foreground="red")
		text.tag_config('white',foreground="white")
		text.tag_config('orange',foreground="#ff6600")
		
		
		text.config(state=tk.DISABLED)

	def openLink(self,event):
		eventUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(eventUrl)			

	
class HackerearthPage(tk.Frame):
	def __init__(self,parent,controller):
		hackerearthObj = Hackerearth()
		hackerearthEvents =  hackerearthObj.hackerearthEvents
		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		heading = tk.Label(self,text="""
============================================================================================
	HACKEREARTH EVENTS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		text = ScrolledText(self,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",
					cursor="arrow")
		text.pack(expand=True, fill='both')
		text.insert(tk.INSERT,"\n root",'red')
		text.insert(tk.INSERT," @ ",'white')
		text.insert(tk.INSERT,"Notifier")
		text.insert(tk.INSERT," ># ",'lightblue')
		text.insert(tk.INSERT," get hackerearthevents ")

		for event in hackerearthEvents:
			text.insert(tk.INSERT,"\n\n [+]  ",'orange')
			name = event['title']
			text.insert(tk.INSERT,name,'lightblue')
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime + "\n\t>  "
			hackerearthFormat = "Format: "+event['format']
			description = startTime + hackerearthFormat
			text.insert(tk.INSERT,description)
			hackerearthUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,hackerearthUrl,('link',hackerearthUrl))
			text.insert(tk.INSERT,"\n")
		
		text.tag_config('link',foreground="#3385ff")	
		text.tag_bind('link','<Button-1>',self.openLink)
		text.tag_config('lightblue',foreground="#00e6e6")
		text.tag_config('red',foreground="red")
		text.tag_config('white',foreground="white")
		text.tag_config('orange',foreground="#ff6600")
		
		
		text.config(state=tk.DISABLED)

	def openLink(self,event):
		hackerearthUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(hackerearthUrl)			

class HackerrankPage(tk.Frame):
	def __init__(self,parent,controller):
		hackerrankObj = Hackerrank()
		hackerrankEvents =  hackerrankObj.hackerrankEvents
		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		heading = tk.Label(self,text="""
============================================================================================
	HACKERRANK EVENTS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		text = ScrolledText(self,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",
					cursor="arrow")
		text.pack(expand=True, fill='both')
		text.insert(tk.INSERT,"\n root",'red')
		text.insert(tk.INSERT," @ ",'white')
		text.insert(tk.INSERT,"Notifier")
		text.insert(tk.INSERT," ># ",'lightblue')
		text.insert(tk.INSERT," get hackerrankevents ")

		for event in hackerrankEvents:
			text.insert(tk.INSERT,"\n\n [+]  ",'orange')
			name = event['title']
			text.insert(tk.INSERT,name,'lightblue')
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime
			description = startTime
			text.insert(tk.INSERT,description)
			hackerrankUrl = event['url']
			text.insert(tk.INSERT,"\n\t>  Event url: ")
			text.insert(tk.INSERT,hackerrankUrl,('link',hackerrankUrl))
			text.insert(tk.INSERT,"\n")
		
		text.tag_config('link',foreground="#3385ff")	
		text.tag_bind('link','<Button-1>',self.openLink)
		text.tag_config('lightblue',foreground="#00e6e6")
		text.tag_config('red',foreground="red")
		text.tag_config('white',foreground="white")
		text.tag_config('orange',foreground="#ff6600")
		
		
		text.config(state=tk.DISABLED)

	def openLink(self,event):
		hackerrankUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(hackerrankUrl)			


class CodeforcePage(tk.Frame):
	def __init__(self,parent,controller):
		codeforceObj = Codeforce()
		codeforceEvents =  codeforceObj.codeforceEvents
		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0)
		heading = tk.Label(self,text="""
============================================================================================
	CODEFORCE EVENTS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		text = ScrolledText(self,font=LARGE_FONT,fg="#00ff00",bg="#1a1a1a",
					cursor="arrow")
		text.pack(expand=True, fill='both')
		text.insert(tk.INSERT,"\n root",'red')
		text.insert(tk.INSERT," @ ",'white')
		text.insert(tk.INSERT,"Notifier")
		text.insert(tk.INSERT," ># ",'lightblue')
		text.insert(tk.INSERT," get codeforceevents ")

		for event in codeforceEvents:
			text.insert(tk.INSERT,"\n\n [+]  ",'orange')
			name = event['title']
			text.insert(tk.INSERT,name,'lightblue')
			startTime =  event['start']
			startTime = "\n\t>  " + "Starts: "+ startTime
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
		
		text.tag_config('link',foreground="#3385ff")	
		text.tag_bind('link','<Button-1>',self.openLink)
		text.tag_config('lightblue',foreground="#00e6e6")
		text.tag_config('red',foreground="red")
		text.tag_config('white',foreground="white")
		text.tag_config('orange',foreground="#ff6600")
		
		
		text.config(state=tk.DISABLED)

	def openLink(self,event):
		codeforceUrl = event.widget.tag_names(tk.CURRENT)[1]
		webbrowser.open_new(codeforceUrl)			



class SettingsPage(tk.Frame):

	def __init__(self,parent,controller):
		ctfObj = ctftime()
		ctfEvents =  ctfObj.ctfEvents

		parameters = self.getParameters()

		tk.Frame.__init__(self,parent, highlightbackground="lightblue", highlightcolor="lightblue", highlightthickness=1, width=720, height=500, bd= 0,bg="#1a1a1a")
		heading = tk.Label(self,text="""
============================================================================================
	SETTINGS
============================================================================================""",
			fg="#00e6e6",bg="#0d0d0d",font=LARGE_FONT)
		heading.pack(expand=False,fill="both")
		container = tk.Frame(self)
		container.pack(side="top",expand=False)
		beforeInvervalFrame = tk.Frame(container,bg="#1a1a1a")
		beforeInvervalFrame.pack(side="top",fill="both",ipady=40)
		label1 = tk.Label(beforeInvervalFrame,text="Notification Time before event: ",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		label1.pack(side="left",padx=10)
		self.beforeIntervaltext = tk.Text(beforeInvervalFrame,height=1,width=10,font=LARGE_FONT)
		self.beforeIntervaltext.insert(tk.INSERT,parameters['beforeEventNotifyInterval'])
		self.beforeIntervaltext.pack(side="left",padx=10)
		label2 = tk.Label(beforeInvervalFrame,text=" Seconds ",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		label2.pack(side="left",padx=10)
		
		labelNotify = tk.Label(container,text=">>>>>>      Notifications from Sites      <<<<<<",bg="#1a1a1a",fg="#00e6e6",font=20)
		labelNotify.pack(side="top",fill="x",ipady=10)
		
		ctftimeFrame = tk.Frame(container,bg="#1a1a1a")
		ctftimeFrame.pack(side="top",fill="both")
		self.ctftimeCheck = tk.IntVar()		
		self.ctftimeBox = tk.Checkbutton(ctftimeFrame,bg="#1a1a1a",variable=self.ctftimeCheck)
		if parameters['ctftime'] == 1:
			self.ctftimeBox.select()
		self.ctftimeBox.pack(side="left")

		ctftimeLabel = tk.Label(ctftimeFrame,text=" CTFtime",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		ctftimeLabel.pack(side="left",padx=5)
		
		hackerearthFrame = tk.Frame(container,bg="#1a1a1a")
		hackerearthFrame.pack(side="top",fill="both")
		self.hackerearthCheck = tk.IntVar()
		self.hackerearthBox = tk.Checkbutton(hackerearthFrame,bg="#1a1a1a",variable=self.hackerearthCheck)
		self.hackerearthBox.pack(side="left")
		if parameters['hackerearth'] == 1:
			self.hackerearthBox.select()
		hackerearthLabel = tk.Label(hackerearthFrame,text=" Hackerearth",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		hackerearthLabel.pack(side="left",padx=5)

		codechefFrame = tk.Frame(container,bg="#1a1a1a")
		codechefFrame.pack(side="top",fill="both")
		self.codechefCheck = tk.IntVar()
		self.codechefBox = tk.Checkbutton(codechefFrame,bg="#1a1a1a",variable=self.codechefCheck)
		self.codechefBox.pack(side="left")
		if parameters['codechef']==1:
			self.codechefBox.select()
		codechefLabel = tk.Label(codechefFrame,text=" Codechef",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		codechefLabel.pack(side="left",padx=5)

		codeforceFrame = tk.Frame(container,bg="#1a1a1a")
		codeforceFrame.pack(side="top",fill="both")
		self.codeforceCheck = tk.IntVar()
		self.codeforceBox = tk.Checkbutton(codeforceFrame,bg="#1a1a1a",variable=self.codeforceCheck)
		self.codeforceBox.pack(side="left")
		if parameters['codeforce']==1:
			self.codeforceBox.select()
		codeforceLabel = tk.Label(codeforceFrame,text=" Codeforce",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		codeforceLabel.pack(side="left",padx=5)

		hackerrankFrame = tk.Frame(container,bg="#1a1a1a")
		hackerrankFrame.pack(side="top",fill="both")
		self.hackerrankCheck = tk.IntVar()
		self.hackerrankBox = tk.Checkbutton(hackerrankFrame,bg="#1a1a1a",variable=self.hackerrankCheck)
		self.hackerrankBox.pack(side="left")
		if parameters['hackerrank']==1:
			self.hackerrankBox.select()
		hackerrankLabel = tk.Label(hackerrankFrame,text=" Hackerrank",bg="#1a1a1a",fg="#00e6e6",font=LARGE_FONT)
		hackerrankLabel.pack(side="left",padx=5)


		saveButton = MyButton(self,text="Save",command=lambda: self.saveSettings(),fg='#00e6e6',bg="#333333",activebackground="#595959",activeforeground="lightgreen",relief="groove",font=LARGE_FONT)
		saveButton.pack(side="top",expand=False,ipady=2,ipadx=4)


		self.infolabel = tk.Label(self,text="",bg="#333333",relief="groove",font=LARGE_FONT)
		
		
	def saveSettings(self):
		parameters = {}
		parameters['ctftime'] = self.ctftimeCheck.get()
		parameters['hackerearth'] = self.hackerearthCheck.get()
		parameters['hackerrank'] = self.hackerrankCheck.get()
		parameters['codechef'] = self.codechefCheck.get()
		parameters['codeforce'] = self.codeforceCheck.get()
		try:
			parameters['beforeEventNotifyInterval'] = int(self.beforeIntervaltext.get('1.0','end-1c').strip())
			self.infolabel['text'] = "Settings have been saved!	"
			self.infolabel['foreground'] = '#00e6e6'
			self.infolabel.pack(side="top",expand=False,ipady=2,ipadx=4,pady=40)
		except:
			self.infolabel['text'] = "Invalid values were entered !	"
			self.infolabel['foreground'] = 'red'
			return
		self.saveParameters(parameters)



	def saveParameters(self,parameters):
		with open("config/beforeEventNotifyInterval.conf",'w') as fp:
			fp.write(str(parameters['beforeEventNotifyInterval']))
		with open("config/notificationSettings.conf",'w') as fp: 
			fp.write(str(parameters['ctftime'])+"\n")
			fp.write(str(parameters['hackerearth'])+"\n")
			fp.write(str(parameters['hackerrank'])+"\n")
			fp.write(str(parameters['codechef'])+"\n")
			fp.write(str(parameters['codeforce'])+"\n")

		
	def getParameters(self):
		parameters = {}
		with open("config/beforeEventNotifyInterval.conf",'r') as fp:
			parameters['beforeEventNotifyInterval'] = int(fp.read())  #seconds
		with open("config/notificationSettings.conf",'r') as fp: 
			parameters['ctftime'] = int(fp.readline().strip())
			parameters['hackerearth'] = int(fp.readline().strip())
			parameters['hackerrank'] = int(fp.readline().strip())
			parameters['codechef'] = int(fp.readline().strip())
			parameters['codeforce'] = int(fp.readline().strip())
		return parameters

def showAnimation():

	logo = r"""
                 ____
                /  __|         _____           _
                | |_  __    __|  _  | /\____  | |_
                |  _| \ \  / /| |/_/  \  _  \ |  _|
                | |__  \ \/ / | |___  | | | | | |__
                |____|  \__/  |_____| |_| |_| |____|
     ____  _       _     _  ____  _  _____ __   __
    |    || | ___ | |_  |_||  __||_||  _  |\ \./ /
    | /\ || || _ ||  _|  _ | |_   _ | |/_/  \ | /
    | || \/ |||_||| |__ | ||  _| | || |___  / | \
    |_||____||___||____||_||_|   |_||_____||_____|

	"""


	colors = ['0b','02','03','0b','04','06','09','0a','0b','0c','0d','0e']
	curColor =  0
	for ind in range(len(logo)):
		if logo[ind]=='\n':
			os.system("color "+str(colors[curColor%len(colors)]))
			curColor+=1
		print(logo[ind],end="")
		time.sleep(0.007)
	time.sleep(1)
	os.system('color 0d')
	print("                          ---> By  TEJESHREDDY MEKA.")
	time.sleep(1)
	os.system('color 06')
	print('\n\n\t[+] Launching Event Notifier Application.....')
	time.sleep(1)
	os.system('color 0a')
	print('\n\t[+] Retriving data from websites......')
	time.sleep(1)
	os.system('color 0d')
	print("\n\t[+] We will remind you if any competetion  starts.")
	time.sleep(1)
	os.system('color 0e')
	print('\n\t[+] Have a Nice day.............')
	os.system('color 0b')



if __name__=="__main__":
	

	thread = threading.Thread(target=showAnimation)
	thread.start()

	
	app = EventNotifierApp()
	app.mainloop()
	thread.join()

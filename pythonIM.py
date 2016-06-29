import socket
import Tkinter
import time
s = socket.socket()
c = socket.socket()
userNum = 0


def assignIPs():			#Assigns the correct server/client IPs
	global serverHost, serverPort, clientHost, clientPort, waitTime
	#Assign server/client IPs	
	if userNum == 1:
		serverHost = '192.168.20.157'		#Change IPs depending on use
		serverPort = 12345
		clientHost = '192.168.20.156'
		clientPort = 12346
		waitTime = 2.5
	else:
		serverHost = '192.168.20.156'
		serverPort = 12346
		clientHost = '192.168.20.157'
		clientPort = 12345
		waitTime = 5
def assignUser1():
	global userNum
	userNum = 1
	print userNum
	assignIPs()
def assignUser2():
	global userNum
	userNum = 2
	print userNum
	assignIPs()
def newEntry(): #Gets text from field
	global message;
	message = field.get()
	field.delete( 0, len(message))
def startServer():
	s.bind((serverHost, serverPort))   		
	s.listen(5)							#Listens for connection
def acceptConnection():
	oc, addr = s.accept()			#Accepts connection
def connectClient():
	c.connect((clientHost, clientPort))		#Connects to other client
def whileLoop():
	while True:
		if userNum == 1:
			oc.send(("User 1: " + message + " "), userNum)		#Sends Message
			print "User 2:" , c.recv(1024)									#Receives Message
		else:
			print "User 1:" , c.recv(1024)									#Receives Message
			oc.send(("User 2: " + message + " "), userNum)		#Sends Message


selector = Tkinter.Tk()
label1 = Tkinter.Label(text = "Select Which User You Are"); label1.pack(padx=5, pady=10, side="left")			#Label Of which user number
button1 = Tkinter.Button(text = "User 1", command = assignUser1); button1.pack(padx=5, pady=10, side="left")			#User1 Button
button2 = Tkinter.Button(text = "User 2", command = assignUser2); button2.pack(padx=5, pady=10, side="left")			#User2 Button
field = Tkinter.Entry(bd = 5); field.pack(side = 'bottom')			#Entry Field
button3 = Tkinter.Button(text = "Submit Data", command = newEntry); button3.pack(side = 'bottom')			#Assigns field to var
button4 = Tkinter.Button(text = "Start Server", command = startServer); button4.pack(padx=5, pady=10, side="right") 			#Starts TCP Server
button5 = Tkinter.Button(text = "Connect to Client", command = connectClient); button5.pack(padx=5, pady=10, side="right") 			#Starts TCP Server
button6 = Tkinter.Button(text = "Start While Loop", command = whileLoop); button6.pack(padx=5, pady=10, side = "right")
button7 = Tkinter.Button(text = "Connection Accept", command = acceptConnection); button7.pack(padx=5, pady=10, side = "right")

selector.mainloop()


#messages = ['']





	
	
	
	




"""
pythonIM Notes:
Use  'ps aux' in terminal to find current processes if pythonIM is still running
Currently only allows one message to be send
Deletes last character of one sided message

Changes:
-Creating a full GUI experience

Problem: Getting all the steps to run in order for a solid connection. Need to figure out how to start a while loop
"""

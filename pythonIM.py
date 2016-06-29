import socket
import Tkinter
import time
s = socket.socket()
c = socket.socket()
userNum = 0

def assignUser1():
	global userNum
	userNum = 1
	print userNum
	selector.destroy()
def assignUser2():
	global userNum
	userNum = 2
	print userNum
	selector.destroy()
	

selector = Tkinter.Tk()
label1 = Tkinter.Label(text = "Select Which User You Are"); label1.pack(padx=5, pady=10, side="left")
button1 = Tkinter.Button(text = "User 1", command = assignUser1); button1.pack(padx=5, pady=10, side="left")
button2 = Tkinter.Button(text = "User 2", command = assignUser2); button2.pack(padx=5, pady=10, side="left")
selector.mainloop()

#userNum = input("Are you user 1 or 2: ")
messages = ['']


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


	
	
	
	
	
s.bind((serverHost, serverPort))   		
s.listen(5)							#Listens for connection
print "Please wait..."
time.sleep(waitTime)					#Waits for other connection to be open
c.connect((clientHost, clientPort))		#Connects to other client
oc, addr = s.accept()			#Accepts connection
	

while True:
	if userNum == 1:
		oc.send((raw_input("User 1: ") + " "), userNum)		#Sends Message
		print "User 2:" , c.recv(1024)									#Receives Message
	else:
		print "User 1:" , c.recv(1024)									#Receives Message
		oc.send((raw_input("User 2: ") + " "), userNum)		#Sends Message
 
 






"""
pythonIM Notes:
Use  'ps aux' in terminal to find current processes if pythonIM is still running
Currently only allows one message to be send
Deletes last character of one sided message

Changes:
- User Selector Created
"""

import socket
import Tkinter
import time
s = socket.socket()
c = socket.socket()

userNum = input("Are you user 1 or 2: ")
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

screen = Tkinter.Tk()
printuserNum = Tkinter.Label(text = ("User Number:" , userNum)); printuserNum.pack()
printIP = Tkinter.Label(text = ("IP address:", serverHost)); printIP.pack()
label1 = Tkinter.Label(text = messages[0]); label1.pack()
label2 = Tkinter.Label(text = messages[0]); label2.pack()
label3 = Tkinter.Label(text = messages[0]); label3.pack()
label4 = Tkinter.Label(text = messages[0]); label4.pack()
label5 = Tkinter.Label(text = messages[0]); label5.pack()
label6 = Tkinter.Label(text = messages[0]); label6.pack()
label7 = Tkinter.Label(text = messages[0]); label7.pack()
label8 = Tkinter.Label(text = messages[0]); label8.pack()
label9 = Tkinter.Label(text = messages[0]); label9.pack()
screen.mainloop()
	
	
	
	
	
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
-
"""

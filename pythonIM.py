import socket
import time
s = socket.socket()
c = socket.socket()

userNum = input("Are you user 1 or 2: ")

#Assign server/client IPs
if userNum == 1:
	serverHost = '192.168.20.157'
	serverPort = 12345
	clientHost = '192.168.20.156'
	clientPort = 12346
	waitTime = 5
else:
	serverHost = '192.168.20.156'
	serverPort = 12346
	clientHost = '192.168.20.157'
	clientPort = 12345
	waitTime = 10

s.bind((serverHost, serverPort))
s.listen(5)
print "Wait period..."
time.sleep(waitTime)
c.connect((clientHost, clientPort))

while True:
	oc, addr = s.accept()
	oc.send(raw_input("Message Please: "), userNum)
	print c.recv(1024)








"""
#Connects to server
s = socket.socket()
serverHost = '192.168.20.150'
serverPort = 12345
s.connect((serverHost, serverPort))
s.recv(1024)


c = socket.socket()
clientHost = '192.168.20.156'
clientPort = 12346
c.bind((clientHost, clientPort)) 
c.listen(5)
while True
	newText = raw_input("What would you like to send: ")
	c.send(newText
	
	c, addr = s.accept()
	print 'Got connection from', addr
	c.send('Thank you for connecting, fam')
	print "c is:", c
	c.close()
"""


#Use  'ps aux' in terminal to find current processes if pythonIM is still running
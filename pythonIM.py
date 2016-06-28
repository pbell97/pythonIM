"""
pythonIM Notes:
Use  'ps aux' in terminal to find current processes if pythonIM is still running
Currently only allows one message to be send
Deletes last character of one sided message
"""

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







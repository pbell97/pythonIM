import socket


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
	c.send(newText)
import socket

#Initial Connection
s = socket.socket()
host = '192.168.20.150'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
	c, addr = s.accept()
	c.send('Thank you for connecting, fam')
	print "DONE"
	


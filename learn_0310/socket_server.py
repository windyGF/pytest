import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
while 1:
	c,addr = s.accept()
	print('got connection from', addr)
	c.send(b'Thx for your connecting')
	c.close()


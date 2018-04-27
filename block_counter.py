import socket
import time


now = time.time()
future = now+30
while True:
	if time.time() == future:
		print("its the future")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect(("localhost", 8888))

		str_recv = s.recv(1024)

		print(str(str_recv))

	
		str_send="MAKE A BLOCK"
		s.send(bytes(str_send, 'utf-8'))
		str_recv = s.recv(1024)
		print(str(str_recv))
		s.close()

		#build another block in 120 seconds
		future = time.time() + 30


	
		#now=time.time()
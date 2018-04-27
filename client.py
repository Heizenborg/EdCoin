import socket
import hashlib as hasher
import time
import sys


def build_transaction(author, transaction):
	return str(author + ":" + transaction)

def add_courses():
	checker = True
	courses = ""
	while checker:
		course_title = input("Enter Course Title of 1 to quit...")
		if course_title == "1":
			return courses
		else:	
			courses += course_title + ","



user = 'jdoe'

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost", 8888))

	str_recv = s.recv(1024)

	print(str(str_recv))

	message = input("Enter your message ")

	if "build" in message:
		courses = add_courses()

		print("COURSES: ",courses)

		str_send = user + ":build:" + courses

		s.send(bytes(str_send, 'utf-8'))

		str_recv = s.recv(1024)

		print(str(str_recv))
		s.close()

	elif "exit" in message:
		print("exiting...")
		str_send = build_transaction(user, "exit")
		s.send(bytes(str_send, 'utf-8'))
		
		str_recv = s.recv(1024)
		s.close()
		sys.exit()

	else:
		str_send = build_transaction(user, message)
		s.send(bytes(str_send, 'utf-8'))
		
		str_recv = s.recv(1024)
		print(str(str_recv))
		s.close()


	

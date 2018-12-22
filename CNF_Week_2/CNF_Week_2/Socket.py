import socket
import csv

def Main():
	s = socket.socket()
	print("socket successfully created")
	print("socket binded to s")
	s.listen(s)
	print("socket is listening")
	while True:
		c, addr = s.accept()
		print("got connection from", addr)
		c.send("Thank you for connecting")
		c.close()

def attendance(info):
	host = 10.10.8.244
	post = 12345
	s = socket.socket()
	s.connect((host,port))
	message = "send info"
	while True:
		s.send(message.encode('attendance'))
		info = s.recv(1024)
		print("received from the server:", str(data.decode('attendance')))
		key = input('Do you want to continue (Y/N) :')
		if key == y:
			continue
		else:
		    break
	s.close()	 

if __name__ == '__main__':
	main()	   	
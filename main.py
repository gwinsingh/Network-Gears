import os

print "Network Interactive Tools - Version 1.0\nThe purpose of this app is to provide its users a multipurpose network utility.\nThis project will provide combined functionality of web information extractor, packet analyzer, reverse shell and web spider in an intuitive graphical user interface."
print "Select one of the Functionalities:\n1. Web Crawler\n2. WebInfo Utility\n3. Reverse Shell\n4. Packet Sniffer\nEnter 'exit/quit to close'"

moveon = True

def webcrawler():
	print "Welcome to Web Crawler"
	st = "python spidy/main.py"
	os.system(st)

def webinfo():
	print "Welcome to Web Info Utility"
	st = "python webinfo/main.py"
	os.system(st)

def reverseshell():
	print "Welcome to Reverse Shell"
	st = "python3 reverseshell/multiserver.py"
	os.system(st)

def sniffer():
	print "Welcome to Packet Sniffer"
	st = "sudo python3 sniffer/sniffer.py"
	os.system(st)

while moveon:
	print "Select one of the Functionalities: 1. Web Crawler 2. WebInfo Utility 3. Reverse Shell 4. Packet Sniffer\nEnter 'exit/quit to close'"
	print "NetworkTools >",
	inp = str(raw_input())
	# inp = int(inp1)
	if inp == "exit" or inp == "quit":
		moveon = False
	elif inp == '1':
		webcrawler()
	elif inp == '2':
		webinfo()
	elif inp == '3':
		reverseshell()
	elif inp == '4':
		sniffer()
	else:
		print "\nInvalid Input. Try Again.\n"
	pass
print "\nExiting . .\n"


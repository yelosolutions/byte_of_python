#!/usr/bin/python3
"""Demonstrates the use of try ... finally in exceptions
"""
import sys
import time

f = None
try:
	f = open('poem.txt')
	
	while True:
		line = f.readline()

		if len(line) == 0:
			break
		print(line, end=" ")
		
		sys.stdout.flush()
		
		print("Now press ctrl-c ")
		
		time.sleep(2)

except IOError:
	print("File must be missing")
except KeyboardInterrupt:
	print("You have terminated the program")
finally:
	if f:	
		f.close()
	print('Cleaning up: Closed the file')

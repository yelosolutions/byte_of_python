#!/usr/bin/python3
"""Demonstrate the how flush works during output and \
how to use the sys.stdout.flush() function
"""
import time
import sys


for i in range(10):
	print(i, end=' ')
	sys.stdout.flush()
	time.sleep(1)

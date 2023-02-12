#!/usr/bin/python3
"""Demostrating how to use flush works \
to write everything on the terminal from the buffer
"""
import sys
import time


for i in range(10):
	print(i, end=' ', flush=True)
	time.sleep(1)

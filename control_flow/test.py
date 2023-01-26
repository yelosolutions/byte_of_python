#!/usr/bin/python3
import random

name = input('Please enter your name:' )
def lucky_bastard():
	number = random.randint(0, 34)
	if number == 7:
		message = 'its your lucky day!'
		print(message)
	print(f'{name}, unfortunately your number is: {number}')	

lucky_bastard()

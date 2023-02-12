#!/usr/bin/python3
"""
Demonstrating how to create a custom exception class \
, use try...except...else and flush function 
"""
import sys
import time


class ShortInputException(Exception):
	"""A custom exception class, inherits from the Exception class"""
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast 

try:
	def reverse(word):
		word = word[:-1]

	def is_palindrome(wordi):
		wordi == reverse(wordi)
	
	message = input(' Write something: ') 
	
	if message == is_palindrome:
		print('Wow your input is a palindrome!')
	
	if len(message) < 3:
		raise ShortInputException(len(message), 3)

except EOFError:
	print('EOF, really?')

except KeyboardInterrupt:
	print('You have just terminated the program')

except ShortInputException as ex:
	print('Your input is {} characters long but we expected atleast {} characters\
lond'.format(ex.length, ex.atleast))

else:
	print('Your input is: ', message, end=' ', flush=True)
	time.sleep(5)

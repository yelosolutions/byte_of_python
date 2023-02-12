#!/usr/bin/python3
"""
Also raise exceptions
"""


class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something: ')
	if len(text) < 3:
		raise ShortInputException(len(text), 3)
except KeyboardInterrupt:
	print('Program terminated')
except EOFError:
	print('Why did you call EOF on me?')
except ShortInputException as ex:
	print(f'ShortInputException: The word you have entered has {ex.length} letters,\
			 we expect {ex.atleast}')
else:
	print('No exception was raised')


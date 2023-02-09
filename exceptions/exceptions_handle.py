#!/usr/bin/python3
"""Exceptions occur wen exceptional situations pccor in a program
"""


try:
	text = input('Enter something: ')
except EOFError:
	print('Why did you \'EOF\' me?')
except KeyboardInterrupt:
	print('Program terminated')
else:
	print(f'this is what you\'ve entered: {text}')

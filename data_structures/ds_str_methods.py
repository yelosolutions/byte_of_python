#!/usr/bin/python3
"""
Methods of string (('') an object of class str)
"""
word = str(input('Enter a wise phrase: '))
if word.find('nig') != -1:
	print('Wueh we!')
if 'nig' in word:
	print(f'Profanity!')

name = 'Yelosolutions'

if name.startswith('Yelo'):
	print('\nYes the name starts with "Yelo"')

if 'a' in name:
	print('Yes, a is in name')
else:
	print('No')

if 'sol' in name:
	print('Yes the \'sol\' is part of the name')

delimiter = '.'
mylist = ['Kenya', 'Wakanda', 'Uganda', 'Tz']
print(delimiter.join(mylist))

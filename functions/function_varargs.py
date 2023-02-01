#!/usr/bin/python3
'''funtion with variable parameters/arguments
'''
def details(a, *bs, **phonebook):
	print('a is: ', a)
	
	for i in bs:
		print('This isn\'t a keyworded argument => ', i)
	for name,  number in phonebook.items():
		print(f'{name}: {number}')

details(12, 98, 3, 434, 3, jane=701221321, kamaa=712673214)

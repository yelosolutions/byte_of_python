#!/usr/bin/python3
'''
Demonstrating the use of break
'''
running = True
quit = 'exit'

while running:
	something = input('Write something: ')
	if something == quit:
		break
	print(f'You\'ve entered {len(something)} letters')
print('Done')

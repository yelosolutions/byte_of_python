#!/usr/bin/python3
'''
Demonstrating the use of continue
'''

running = True
quit = 'exit'

while running:
	s = input('Enter something: ')
	if s == quit:
		print('Too soon! Come back later')
		break
	elif len(s) < 3:
		print('Too small, keep typing buddy')
		continue
	else:
		print(f'You\'ve entered {len(s)} letters')
print('Done')

#!/usr/bin/python3

'''
Prompts user to guess a number
'''

number = 5
running = True

while running:
	guess = int(input('Enter a number: '))
	if guess == number:
		print('Wow! How did you guess that?\n You must be lucky!')
		running = False
	elif guess > number:
		print('You almost got it, it\'s a little lower (:')
	else:
		print('Shoot! Just a little higher(:')
else:
	print('Done')		

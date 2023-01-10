#!/usr/bin/python3
'''
 Prompts the user to guess a number
'''
number = 7
guess = int(input('Guess a number: '))

if guess == number:
	print('Congrats! How did you do that')
	print('(but no prizes!)')
elif guess < number:
	print('Sorry, the lucky number is a little higher')
else:
	print('The lucky number is a little lower')
print('Done')


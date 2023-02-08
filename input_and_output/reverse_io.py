#!/usr/bin/python3
"""
A script that prompts a user to enter a string then
determines if its a palindrome
"""
def reverse(text):
	"""Reverses a text
	"""
	return text[::-1]

def is_palindrome(text):
	"""Returns the reverse of a text"""
	return text == reverse(text)
		

something = input('Write something: ')
forbidden = (' ', ',', '.', '?', '!')

for character in something:
	if character in forbidden:
		''.join(something)

 
if is_palindrome(something):
	print(f'Yes \'{something}\' is palindrome')
else:
	print(f'Sorry \'{something}\' is not a palindrome')


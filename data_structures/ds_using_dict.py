#!/usr/bin/python3
"""
Demonstrating dictionaries
"""
ab = {
'Swaroop':'swaroop@swaroopch.com',
'Matsumoto':'matz@ruby-lang.org', 
'Larry':'larry@wall.org',
'Spammer':'spammer@hotmail.com'
}

print('Swaroop\'s address is', ab['Swaroop'])

del ab['Spammer']

print(f"\nThere are {len(ab)} contacts in the address-book\n")
for key, value in ab.items():
	print(f"Contact {key} at {value}")

ab['Guido'] = 'guido@python.org'

print('\nGuido\'s address is', ab['Guido'])

#!/usr/bin/python3
"""
Demostrates how to raise excepions using a custom class
"""


class ShortWordException(Exception):
	"""A custom class that inherits from the esception class"""
	def __init__(self, length, atleast):
		self.length = length
		self.atleast =	atleast

try:
	word = input("Enter something: ")

	if len(word) < 3:
		raise ShortWordException(len(word), 3)
except EOFError:
	print("\nWhy did you give me an EOF?")

except	ShortWordException as  ex:
	print(f"Your input is {ex.length} long, but we expect {ex.atleast} long letters")

except KeyboardInterrupt:
	print("You have terminated the program") 
	
else:
	print(f"The word that you have entered is {len(word)} letters long")
	

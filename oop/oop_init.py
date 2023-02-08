#!/usr/bin/python3
"""
The __init__ method
"""


class Person:
	def __init__(self, name):
		self.name = name
 
	def say_hi(self):
		print('Hey, how are you?', self.name)
p = Person('Jay')
p.say_hi()

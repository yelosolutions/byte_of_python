#!/usr/bin/python3
"""
Robot like conversation implementation
"""


class Robot:
	"""Represents a robot"""
	#class variable, number of robots is 0
	population = 0

	def __init__(self, name):
		"""Initializes the data."""
		self.name = name
		print(f'(Initializing  {self.name})')
		
		#when this is created, population is increased by 1
		Robot.population += 1

	def say_hi(self):
		"""Greeting by the robot"""
		print('Greetings, my masters call me', self.name)
	
	@classmethod
	def how_many(cls):
		"""Prints the current population"""
		print(f'We have {cls.population} robots.')

	def die(self):
		"""Death of a robot """
		print(f'{self.name} is being destroyed!')
		Robot.population -= 1
		if Robot.population == 0:
			print('{} was the last one.'.format(self.name))
		else:
			print('There are still {:d} robots working.'.format(Robot.population))
		


droid1 = Robot('R2-D2')
droid1.say_hi()
droid1.how_many()

droid2 = Robot('C-3P0')
droid2.say_hi()
droid2.how_many()

print('\nRobots can do some work here\n')
print('Robots have finished their work. So let\'s destroy them.')

droid1.die()
droid2.die()

Robot.how_many()
print(Robot.__doc__)

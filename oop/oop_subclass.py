#!/usr/bin/python3
"""Inheritance demostration"""


class School_Member:
	"""Represents a member of a school"""	
	def __init__(self, name, age):
		self.age = age
		self.name = name
		print(f'(Initialized SchoolMember: {self.name})')

	def tell(self):
		"""Tell details"""
		print('Name:"{}" Age: "{}"'.format(self.name, self.age), end='')


class Teacher(School_Member):
	"""Represents a teacher"""
	def __init__(self, name, age, salary):
		School_Member.__init__(self, name, age)
		self.salary = salary
		print(f'(Initialized Teacher: {self.name})')

	def tell(self):
		School_Member.tell(self)
		print(f'Salary: "{self.salary}"')

class Student(School_Member):
	"""Represents a student"""
	def __init__(self, name, age, marks):
		School_Member.__init__(self, name, age)
		self.marks = marks
		print(f'(Initialized Student: {self.name})')
	
	def tell(self):
		School_Member.tell(self)
		print(f'Marks: "{self.marks}"')

t = Teacher('Mrs. Kinuthia', 34, 30000)
s = Student('Odiel', 23, 56)

print()

members = [t, s]
for member in members:
	member.tell()

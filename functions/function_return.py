#!/usr/bin/python3
'''working with the return statement
'''
def maximum(a, b):
	'''
	Prints the maximum number between the two

	Numbers must be integers
	'''
	a = int(a)
	b = int(b)
	if a > b:
		return a
	elif a == b:
	       	return 'The two are equal'
	else:
		return b

print(maximum(10, 10.0005))
print(maximum.__doc__)
help(maximum)

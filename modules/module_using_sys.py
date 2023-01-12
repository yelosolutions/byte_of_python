#!/usr/bin/python3

import sys

print('The following are the list of cmd line arguments: ')
for i in sys.argv:
	print(i)
print(f'And they are {len(sys.argv)} of them')
print(sys.path)

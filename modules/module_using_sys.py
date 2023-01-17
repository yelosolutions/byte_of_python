#!/usr/bin/python3
'''
implimenting the functionality of a module using sys
'''
import sys


def print_args():
    print('The command line arguments are: ')
    for i in sys.argv:
        print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
print_args()

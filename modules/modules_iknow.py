#!/usr/bin/python3
'''
print the list of cmd line argument variables and the sys path
'''
import sys
import os


def print_args():
    print(f'This is the third cmd line argument: {sys.argv[2]}')

print(f'And this is the PYTHONPATH: {sys.path}')
print('()You must be lucky!')
print('\n This is the path to the current directory :', os.getcwd())
print_args()

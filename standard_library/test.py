#!/usr/bin/python3
"""Demostrate the use of getenv function of the os module\
to get the value of environment variable keys
"""
import os

key = 'HOME'
value = os.getenv(key)

print('The value of \'HOME\' is: ', value )

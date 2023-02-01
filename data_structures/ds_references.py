#!/usr/bin/python3
"""
Demostrating how references are used
"""
print('Simple Assignment')
shoplist = ['apples', 'carrots', 'mangoes', 'bananas']
mylist = shoplist
del shoplist[0]
print('This is shoplist', shoplist)
print('This is mylist', mylist)
print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
print('This is mylist', mylist)
print('This is shoplist', shoplist)

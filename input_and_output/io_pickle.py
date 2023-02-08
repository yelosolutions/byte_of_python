#!/usr/bin/python3
"""storing a variable using the pickle module
"""
import pickle


shoplistfile = 'shoplist.data'
shoplist = ['Maccoffee', 'Toffa', 'Mandunya', 'Mcheti']

#write to the file using open
f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f)

f.close()

del shoplist

f = open(shoplistfile, 'rb')

storedlist = pickle.load(f)
print(storedlist)
f.close()

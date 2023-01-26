#!/usr/bin/python3
"""
Lists demostration
"""
shoplist = ['apple', 'mango', 'carrot', 'banana']
print(f'I have {len(shoplist)} items to purchase.')
print(f'These items are:', end=' ')
for item in shoplist:
	print(item, end=' ')
print('\nI also have to buy rice')
shoplist.append('rice')
print('My shopping list is now:', shoplist)
print('I will sort my list now')
shoplist.sort()
print(f'Sorted shopping list is {shoplist}')
print(f'The first item I bought was {shoplist[0]}')
print('I bought the apple')
del(shoplist[0])
print(f'My shopping list is now {shoplist}')

#!/usr/bin/python3
"""
Demostrating tuples
"""
zoo = ('python', 'elephant', 'penguin')
print(f'Number of animals in the zoo is: {len(zoo)}')
new_zoo = 'monkey' ,'camel' , zoo
print(f'Number of cages in new zoo are {len(new_zoo)}')
print(f'All animals in zoo are: {new_zoo}')
print(f'Animals brought from old zoo are {zoo}')
print(f'Last animal brought from old zoo is {new_zoo[2][2]}')
print('Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))

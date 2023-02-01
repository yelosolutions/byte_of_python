#!/usr/bin/python3
"""
Demonstrating the use of sets
"""
countries = set(['Kenya', 'Uganda', 'Wakanda'])
countries_new = countries.copy()
countries_new.add('Congo')
print(countries_new)
countries_new.add('Tz')
print(countries_new)

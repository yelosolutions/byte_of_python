#!/usr/bin/python3
"""
Implementing  a class diagram of an online shop ordering system
"""
class Customer:
	def __init__(self, name, phone, email, address):
		"""
		Refers to own Class, represents a Customer 
		"""
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address
		
		def set_address

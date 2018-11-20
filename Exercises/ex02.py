#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Concatenating two lists in Python
# List comprehensions


# Using + operator
# Using extend

list_a = ['a','b','c','d','e','f']
list_b = [1,2,3,4,5]

print( list_a + list_b)

list_a.extend(list_b)  					# concatenated list is not present in list_c
print( list_a)									# In the above example, extends concatenates the list_b into list_a


numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]

print( list(n**2 for n in numbers) )	# list comprehensions
print( squares)

print ( list( x**2 for x in numbers if x==2) , " this is my number 2")
# Fuction with loop can be written in one line
# let's check if lambda can be written this way

print( list( map ( lambda x: x**2 , [1,2,3,4] )))		# map object
print( list( n**2 for n in [1,2,3,4] if n==2 ) ) 		# Generator object, list comprehensions

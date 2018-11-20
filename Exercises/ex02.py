#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Concatenating two lists in Python


# Using + operator
# Using extend

list_a = ['a','b','c','d','e','f']
list_b = [1,2,3,4,5]

print( list_a + list_b)

list_a.extend(list_b)  					# concatenated list is not present in list_c
print( list_a)									# In the above example, extends concatenates the list_b into list_a
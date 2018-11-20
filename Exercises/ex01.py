#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# lambda, map and filter in Python


def add(x,y):				# Defining function
	return x+y
print(add(3,2))

addl = lambda x,y: x+y 		# Defining lambda function
print(addl(5,7))


def minus(x,y):					# Defining function
	return x-y
print(minus(8,5))
print(list(map(minus, [4,3,4,9,9,9,9,9,9],[9,1,3,3,3] )) )  
# Using map function Takes inputs and iteratively until input is exausted

# Iterating over a dictionary using map and lambda
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(map(lambda x: x['name'], dict_a)))
print(list(map(lambda x: x['points'], dict_a)))
print(list(map(lambda x: x['points']+99 , dict_a)))


# Filter
# filter function expects two arguments, function_object and an iterable. 
# function_object returns a boolean value. function_object is called for each element of the iterable 
# and filter returns only those element for which the function_object returns true.

print(list(filter(lambda x: x['name'] == 'java' , dict_a )))

print(list(filter(lambda x: x==10 , map(lambda x: x['points'], dict_a) )))
#-----list->filter-->function=10---->list_of_points_using_map_and_lambda









# Traceback (most recent call last):
#   File "ex01.py", line 22, in <module>
#     print( map (minus, [9,8,7,6] [4,3,2,1] ) )
# TypeError: list indices must be integers or slices, not tuple

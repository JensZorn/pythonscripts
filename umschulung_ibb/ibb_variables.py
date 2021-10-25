#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 
#######################################################################################
#                             <°))))><
#
#               Types of variables and accessing them
#
#               by Jens Zorn
#
#               - variables do not need to be declared
#               - assigning values to them automatically declares them (incl. type)
#               - assignment operator is =
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################

# assignment
a = 1
# multiple assignment
a = b = c = 1
a, b, c = 1, 2, 3


# standard data tyoes
# numbers
# int
a = 1
# long

# float
a = 1.11
# complex

# strings
a = "Hey there!"

print (a)
print (a[0])
print (a[2:5])
print (a[2:])
print (a * 2)
print (a + "TEST")

# lists
a = ['element1', 'element2', 'element3', 2, 2.2]
b = ['no', 'yes', True]

print (a)
print (a[0])
print (a[1:3]) 
print (a[2:]) 
print (b * 2) 
print (a + b)

# tuples
The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example 
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple               # Prints the complete tuple
print tuple[0]            # Prints first element of the tuple
print tuple[1:3]          # Prints elements of the tuple starting from 2nd till 3rd 
print tuple[2:]           # Prints elements of the tuple starting from 3rd element
print tinytuple * 2       # Prints the contents of the tuple twice
print tuple + tinytuple   # Prints concatenated tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list


# dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

# data type conversion
1 	

int(x [,base])

Converts x to an integer. base specifies the base if x is a string.
2 	

long(x [,base] )

Converts x to a long integer. base specifies the base if x is a string.
3 	

float(x)

Converts x to a floating-point number.
4 	

complex(real [,imag])

Creates a complex number.
5 	

str(x)

Converts object x to a string representation.
6 	

repr(x)

Converts object x to an expression string.
7 	

eval(str)

Evaluates a string and returns an object.
8 	

tuple(s)

Converts s to a tuple.
9 	

list(s)

Converts s to a list.
10 	

set(s)

Converts s to a set.
11 	

dict(d)

Creates a dictionary. d must be a sequence of (key,value) tuples.
12 	

frozenset(s)

Converts s to a frozen set.
13 	

chr(x)

Converts an integer to a character.
14 	

unichr(x)

Converts an integer to a Unicode character.
15 	

ord(x)

Converts a single character to its integer value.
16 	

hex(x)

Converts an integer to a hexadecimal string.
17 	

oct(x)

Converts an integer to an octal string.
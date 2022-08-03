# Python Operators

# Two Types

"""
# Arithmetic

+ - * /
+ adding two variables together.
- subtracts
* multiply
/ divide
** exponent


# Comparative

> greater than
< less than
== is equal to
!= not equal to
>= greater than or equal to
<= less than or equal to

"""

a = 7
b = 2
print(a)
print(b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)

greeting = "HelloWorld"

# what options are available in python's builtin library
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.isdigit())
print(greeting.__contains__("Hello"))
print(greeting.endswith("d"))


### Concatenuation and Casting

""
first_name = "James"
last_name = "Bond"
middle_name = "007"
age = 47
print(f"{first_name} {middle_name} {last_name} {age}")
print(first_name + " " + middle_name + " " + last_name + " " + str(age))
""
### String Indexing

""" 

Hello World!
01234567891011

NB: Indexing begins with 0 in python.

# print only `world` in a print statement using slicing 
# print 4th letter from left to right - use correct indexing for all statements
# print 7 letter from right to left
# print 6 letter from left to right

print(greeting[:10])
print(greeting[4])
print(greeting[-7])
print(greeting[6])

"""


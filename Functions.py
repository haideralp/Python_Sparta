# What is a function ?
# Why do we need it -
# Dry = DO NOT REPEAT Yourself
# Syntax def function_name():
# you need to call function always

# 1 def  function()
# 2 def function();
# 3 def  function
# 4 def function(): correct

# Procedural and OPP programming
"""""
def greet_user():
    print("Welcome")

greet_user()
"""


# greet the use with their name
# prompt the use to enter their name
# display a welcome message together with their name.

def greet_user(name):  # True
    print("welcome Dear" + name)


greet_user("Haider")


# create a function that takes 2 args as int
# add both values and display the result
""""
def add_num(a,b):
    sum:(a + b)
# Specifying variables
a = 2
b = 4
print("The sum is,add_num(a+b)")
"""
"""""
def add_num(a , b):  #function for addition
    sum=a+b
    return sum #return value
# Specifying variables

a=25  #variable declaration
b=55
print("The sum is", add_num(a, b)) # calling for function to print the sum value

SRK example
def add(num1, num2):
    #print(num1,num2)
    return (num1 + num2)
print(add(4,2))
"""
# Create basic calculator with 4 functions
# sub - multiple - divide -%
# display a message with desired outcome using return statement or print ()
# follow best practices of naming convention - sudo coding - commenting.

# Simple basic calculator

# This function subtracts two numbers
def subtract(a, b):
    return a - b

# This function multiplies two numbers
def multiply(a, b):
    return a * b

# This function divides two numbers
def divide(a, b):
    return a / b
This function expresses percentage
def percentage(a, b):
    return a % b

print("Select operation.")
print("1.Subtract")
print("3.Multiply")
print("4."%") 
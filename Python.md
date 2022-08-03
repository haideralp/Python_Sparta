# Python Operators

# Two Types

## Arithmetic

- >  Key Operators : + - * /  
- > (+ adding two variables together)
- > (subtract two variables)
- > (* multiply)
- > (/ divide)
- > (** exponential)

## Comparative

- >  greater than
- > < less than
- > == is equal to
- > != not equal to
- > = greater than or equal to
- > <= less than or equal to

``` python
a = 7
b = 2
print(a)
print(b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)

greeting = "HelloWorld"

# What options are available in python's builtin library: 

print(greeting)
print(greeting.isalpha())
print(greeting.islower())
```

# String Concatenuation and Casting

```
first_name = "James"
last_name = "Bond"
middle_name = "007"
age = 47

print(first_name + " " + middle_name + " " + last_name + " " + str(age))
or
print(f"{first_name} {middle_name} {last_name} {age}")
```

# String Indexing
 
```
Hello World!
01234567891011

NB: Indexing begins with 0 in python.

# print only `world` in a print statement using slicing 
# print 4th letter from left to right - use correct indexing for all statements
# print 7 letter from right to left
# print 6 letter from left to right

print(greeting[:6]:-1])
print(greeting[4])
print(greeting[-7])
print(greeting[6])
```

``` python

Task - User Input Details

print ("Welcome")

first_name =input("first name"+" ")
middle_name =input ("middle name"+ " ")
last_name =input("last name"+" ")
full_name: str =input(first_name.capitalize()+""+middle_name.capitalize()+""+ last_name.capitalize())
print(full_name)

print("Your full name is...")

print("Please enter your age in years")
age =int(input("age"+" "))
print(full_name + " " +"is"+" "+str(age)+" "+"years old")

print("Enter your first line of address")
house_number = int(input('house_number'+" "))
street_name = str(input('street_name'+" "))
print("please enter your postcode")
postcode = input("postcode"+" ")
full_address = str(input((house_number()+" " +street_name()+" "+postcode))
print ("full_address")

print("please add your contact number")
contact_number = int(input())
print(contact_number.isdigit())

print("Please enter your salary in sterling (£) per year")
salary = input()
print(salary.isdigit())
```

# Creating a Gitignore File
  -  Initialise creating a text file in the main (root) directory, then add files that are to be exempted:
    ![](C:\Users\haide\PycharmProjects\user_details\gitignore.PNG)

# Definition of Ready (DOR)

    - Are the techincal resources available to complete the task ? - Yes
    - Are all the sufficient details there to commence the task ? - Yes
    - Can the task be completed within the time allocated ? - Yes
    - Is sufficient knowledge been covered in course to complete this task ? Yes 
    
# Definition of Done (DOD)

    -  Has a repository on github with name user_details been done ? - Yes
    -  Has a new Project on Pycharm named user_details created ? - Yes
    -  Has a README.md file been added with compelete documentation for the task ? - Yes
    -  Is creating gitgnore file explained and how to ignore depenndecies when pushing to GitHub ? Yes
    -  Are the concepts of concaentuation and casting explaind ? Yes 
    -  Is the information above available to see on GitHub ? Yes 

``` python
print("Data Collections Coding Begins!")

shopping_list = ["bat","milk","bread"]
              #    0       1      2   (in lists first item is index 0 then move forwards)
print(shopping_list)

# find out the type of shopping list
## find out the len of shopping list

print ("Length of shopping list", len(shopping_list))
print("Type of list",type(shopping_list))

# How to add to your shopping list
shopping_list.append("oreos")  # append() adds an item at the end of the list
print(shopping_list)

# How to delete an item from our shopping list
shopping_list.remove("milk")
print(shopping_list)

# find out item to replace an item from the list and replace bat with 'milk'

mixed_list = [1,2,3,"one","two","three"]
#             0 1 2   3     4       5
print(mixed_list)

# print 2 & 3 from the above list
print(mixed_list[1]) #outcome would be 2
print (mixed_list[3]) #outcome would be 3
print (mixed_list[1:3]) #outcome would be 2,3
```
# Data Collections

## Lists, Tuples & Dict

##### Lists
# What are lists ?
# correct syntax [] (use these create list in python)
# lists are mutable (can be changed)
# indexing same concept applies

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

# Pick an item and find out how to replace it from the list and replace bat with 'milk'

mixed_list = [1,2,3,"one","two","three"]
#             0 1 2   3     4       5
print(mixed_list)

# print 2 & 3 from the above list
print(mixed_list[1]) #outcome would be 2
print (mixed_list[3]) #outcome would be 3
print (mixed_list[1:3]) #outcome would be 2,3


# Tuple
# Why do we need Tuple ?
# Lists []  are mutable Vs Tuples () are immutable
# Syntax for tuple ()
# What the cases?
essential = ("city","DOB", "place of birth")
#               0      1        2
#print(essential)
#print(type(essential))
#print (essential[1])
#essential[0] = "town" #Immutable   ( cannot be changed)
#print(essential) #what would be the outcome error

# essential ()
# essential []
# essential {}

#code runs top to bottom. Pycharm tells you error line / syntax.

# what is a dict {} ?
# Dictionary can have all data types (integers strings, floats and boolean)
# Dict work as "Key": "Value" pair
devops_student_1= {
    "key": "value",
    "name": "James",
    "stream": "tech",
    "completed_lessons": 3, #int
    "completed_lessons_names": ["lists","operations","builtin methods"]
}

# print(devops_student_1)
print(devops_student_1.keys())
print(devops_student_1.values())
print(devops_student_1)
print(type(devops_student_1))
print(devops_student_1["name"])

""""
#Find out how to delete in item from dict and delete operations
del devops_student_1
completed_lessons_names= {"lists","operations","builtin methods"}
del completed_lessons_names =["operations"]

#Find out how to change complete lesson from 3 to 2.
completed_lessons = {3}
dict.update(completed_lessons) =[3]


del(devops_student_1["stream"])
devops_student_1["completed_lessons"] = 2
devops_student_1["completed_lessons_names"][1] = "sparta skills"
print(devops_student_1)
"""

# Control Flow

#ifm elif, else statements - conditional statements.

weather = "dry" # True or False   #can use and / or

if  weather == "sunny":
     print("Let's do a BBQ") #executes this line if sunny

elif weather == "dry":
     print("getting there")
else:
     print("hope for the best") #this will be executed if isn't sunny.



#sudo coding
#write in simple terms what is required
#use coding language you machine understand.
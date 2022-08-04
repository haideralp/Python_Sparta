# if elif and else

# loops - for and while loops
# not to repeat yourself
# loops helps us to ITERATE through data collections - DATA

# let's create a list to use for a loop iterate through it
"""
shopping_list = ['fruits', 'milk', 'cream', 'bread']
print(shopping_list)

# print each item of the list as a list
# fruits
# milk
# cream
# bread

print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])

"""
""""
shopping_list = ['fruits', 'milk', 'cream', 'bread']
for item in shopping_list:

    print(item)   # indented due to for being a block of code    / # Anything in orange is key word
    # does the list have bread
    # if bread is found in the list stio the programme
    if item == 'milk':
        break            # break is a key work  # continue - continue look key word

# create a dictionary with 6 key value pairs
# ise for look to iterate through it
# print only keys
# print only values
# print key with matching value
"""
"""
# Defining dictionary - with  key:value pairs
my_dict = {
    'name': 'Maximus',
    'age': 28,
    'height': 176,
    'fav_sport': 'boxing',
    'fav_colour': 'black',
    'fav_destination': 'dubai',
}
print(my_dict.keys())  # only keys from dict are printed
print(my_dict.values())  # only values from dict printed

for item in my_dict:      # for iterative loop of printing items in dict
    print(item)

print(my_dict.keys())  # only keys from dict are printed

print(my_dict.values())  # only values from dict printed

for key, value in my_dict.items():   # loop printing matching key with value
    print(key,value)
"""
"""
# use case of multiple conditions

# create a list with int values 1-4

data_list = [1,2,3,4]

# iterate through list using for loop
for number in data_list

# find 3 and print if found
    if number == 3:
        print('found 3')
# or else list number greater than 3 print gone too far
    elif number >3:
        print ('gone too far')
# other print to soon
    else:
        print('too soon')
"""

# While loop?
# while loops are mostly used as a monitor rather than handling items

number = 0
# iterate while number is less than 10
while number < 10:
    # print the number with message stating it's working
    print(f"it's working--> {number}")
    # add +1 in each iteration
    number += 1
# iterations - does this 10 times.


age = input("Please Enter your age")
# print a message stating your age is whatever the input user entered
print(f"your age is {age}")

# while use enters anything but digit but continue to prompt
# print message back to user

user_prompt = True

while user_prompt:
    age = (input("Please Enter your age"))
    if age.isdigit():
        if int(age) > 177:
            print("You are too old")
        else:
            user_prompt = False  # stop prompting the use
    else:
        print("Please enter your numbers only")
print(f"your age is {age}")

# using the above the use case also check if the user age is less than 177 years
# in ordere to do that you may need to use casting - in other wordds convert age into int
# before you end the while loop.
# from filename import package (once module is made)
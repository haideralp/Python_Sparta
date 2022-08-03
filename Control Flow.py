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

my_dict = {'name':'Maximus','age': 28 ,'height': 176,'fav_sport':'boxing','fav_colour':' black','fav_destination':'dubai'}
print(my_dict)
print(my_dict.keys())  # only keys printed here
print(my_dict.values())  # only values print here
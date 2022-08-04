# Python library, Modules and pacakages
# syntax - key word/s

# how to use them
import os
import random
# import random (everything from this module)
print(random.random()) # generates a random number everytime you run a programme

from random import random

import math

num_float = 12.56

 # user requirement was to round the figure
 # if amount was.50 or above round it upwards
 # if amount was .49 or less downwards
 # we have builtin method that help us meet the first user story
 # Go to python to search what the function does.

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi) # value of pi.

## Modules
# They help us communicate with your local host. Pick up info and utilise it like we want to.
"""""
import os
import math, datetime, sys

# find out the current location
worin_dir = os.getcwd()
print(worin_dir)
print(datetime.datetime.now())

print(os.cpu_count())
print(os.path)
print(sys.path) # linux - absolute path
"""

import Os_Info
print(os_Info.operating_system_information())
class Os_Info:
    def operating_system_information():
     print(os.cpu_count())

    operating_system_information()

#print(os.uname()) # only works Mac and linux

# if os is == "windows"
# else do it

#make into a function to make it resusable
#put function inside class and import class somwhere else
#call the function
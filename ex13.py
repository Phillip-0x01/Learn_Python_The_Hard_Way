from sys import argv

"""
# Script 1
script, first, second, third = argv

print("This script is called:", script)
print("The first variable is: ", first)
print("The second variable is: ", second)
print("The third variable is: ", third)
"""

# Script 2
script, name, age = argv

# Note - you don't need to use all of the unpacked variables...
# print("This script is: ", script)
print("Your name is: ", name)
print("Your age is: ", age)

# Printing a line with previously input variables, then ask for a new value (weight)
print(name + ", we know you are " + age + ", but what is your wight? ")
weight = input()

# Then print everything out
print("So {}, you are {} years old and weight {}".format(name, age, weight))

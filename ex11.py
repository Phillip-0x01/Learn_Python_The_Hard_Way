print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So, you're {} old, {} tall, and {} heavy.\n\n".format(age, height, weight))

"""
Note: raw_input() was eliminated from Python 3.2

"""

print("Pick a random number", end=' ')
num1 = input()
print("Give me another random number", end=' ')
num2 = input()

num3 = int(num1) + int(num2)
print("The numbers you gave me were {} and {}.  When I add them I get {}".format(num1, num2, num3))
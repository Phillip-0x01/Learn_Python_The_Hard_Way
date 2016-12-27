# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
#
# print("The numbers: ")
#
#
# for num in numbers:
#     print(num)


# STUDY DRILLS
start = 1
stop = 8
increment = 2
numbers = []


def add_numbers(i, max_i, i_add):
    while i < max_i:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += i_add
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    return numbers


numbers = add_numbers(start, stop, increment)
print("The numbers: ")

for num in numbers:
    print(num)

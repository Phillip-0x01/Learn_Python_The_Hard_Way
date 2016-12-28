ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list.  Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop is going to remove the last item from more_stuff and assign it to next_one
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # next_one then gets appended to the end of stuff
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy - using a negative counts backwards starting with 1 (as opposed to 0)
print(stuff.pop())
print(' '.join(stuff))  # what? cool! - joins each list item with a space and print the entire thing to the console
print('#'.join(stuff[3:5]))  # super stellar! - joins items 3 & 4 with a hash tag 

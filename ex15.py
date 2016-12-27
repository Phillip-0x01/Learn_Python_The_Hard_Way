from sys import argv

# name of the file to be opened is passed in when running the script
script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())
txt.close()

# name of the file to be opened is passed in through terminal
print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

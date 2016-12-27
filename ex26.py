# First: all of the print functions need to be corrected for Python3
# Second: need to add an extra blank line between functions to ensure proper spacing


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


# Error 1: missing colon after function name
def print_first_word(words):
    """Prints the first word after popping it off."""
    # Error 17: pop is spelled wrong
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    # Error 2: mission close parenthesis after -1
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
# Error 3: replace string single quotes with double quotes
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

# Error 4: explanation spelled wrong in poem string below
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

# Error 5: last number in calculation the 'five' variable should be 6, not 5
five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    # Error 6: flipped forward slash to backslash below
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# Error 7: removed double equal sign below, which is used for evaluation not assignment
# Error 8: changed dash to underscore in variable 'start_point' below
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
# Error 9: changed jeans to beans below
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

# Refactored line below - technically not an error
start_point /= 10

print("We can also do that this way:")
# Error 9: changed crabapples to crates in string below
# Error 10: corrected spelling of start_point variable
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

# Error 11: spelling errors in string below (god -> good, weight -> wait), and tab removed
sentence = "All good things come to those who wait."

# Error 12: ex25 was never imported (assuming the above code was placed in a separate file). For this example I'm
#           not going to break up the code into separate files, so I will just remove 'ex25' from the function name
words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
# Error 13: removing dot in front of function call below
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
# Error 14: print below is missing a 't'
print(sorted_words)
# Error 15: f missing in the word 'first' below
print_first_and_last(sentence)
# Error 16: line of code below should not be indented, 'and' and 'sentence' are spelled wrong
print_first_and_last_sorted(sentence)

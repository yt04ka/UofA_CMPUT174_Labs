# This is Chalkboard Lab (Part 2 of lab 1)
# Written by Roman Kobryn

# Function that gets the phrase and the number, I use split() to make it easier to interact for user
phrase, number = input('Please enter the phrase and number of times to write it using space in between ').split()

# I use while cycle to write down the phrases on the chalkboard,
# so I need a counter to write the correct amount of phrases
counter = 0

# Here I convert number to the int type, otherwise the cycle would not work
number = int(number)

# The while cycle
while counter != number:
    # end=" " is used to write everything in one line with space after the phrase
    print(phrase, end=" ")
    counter = counter + 1

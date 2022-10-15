# This is temperature Lab (Part 4 of lab 1)
# Written by Roman Kobryn

# Getting the code
print("Please input the code of the episode")
print("format of the code is 'S33_E20_Marge the Meanie'")
code = input("Input here > ")

# Slicing our string to input season number, episode and the name into the output
season = code[1: 3]
episode = code[5: 7]
name_of_the_episode = code[8:]

# Output itself
print(f"Season {season}, Episode {episode}: {name_of_the_episode} (The Simpsons)")

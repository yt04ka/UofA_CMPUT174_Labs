"""
This Is part 4 of lab 2
Written by Kobryn Roman
22 September 2022
"""

name, age = input("Please input name and age of your character, using space in between > ").split()

age = int(age)
if age <= 0:
    print("Invalid age")
    exit()
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
younger_names = []
older_names = []
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
for index in range(len(names)):
    if ages[index] < age:
        older_names.append(names[index])
    else:
        younger_names.append(names[index])

print(f"{name} is younger than {younger_names} and older than {older_names}")

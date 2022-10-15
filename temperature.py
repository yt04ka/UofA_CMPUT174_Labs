# This is temperature Lab (Part 3 of lab 1)
# Written by Roman Kobryn

# This is the place to enter the temperature in Canada, int() converts str to thr int type
temperature = int(input('Homer, enter the temperature in Canada here: '))

# Temperature is converted from Celsius to Fahrenheit, int is used to get rid of the decimals
fahrenheit_temperature = int((temperature * 9 / 5) + 32)

# Output for Homer
print(f"{temperature} degrees in Canada would be {fahrenheit_temperature} degrees in Springfield. D'oh!")

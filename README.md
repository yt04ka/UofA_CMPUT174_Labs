# UofA_CMPUT174_Labs
These are the solutions to the Python labs from CMPUT 174 course (UAlberta)


Lab_1

    (1) What to do:
    Ask the user to enter the tasty thing (What is the tasty thing?)
    Print Mmm... and the name of the tasty thing



    (2) What to do:
    Ask the user to enter the phrase and the number of times to repeat it
    Print the repeated phrase (don't forget about an extra space after each one!)



    (3) What to do?
    Ask the user to enter the temperature in Canada (in degrees Celsius)
    Convert it to degrees Fahrenheit, rounded to the nearest whole number.
    Print the result exactly as shown below in the example test cases.

    Use the following formula:
    F = (C * 9 / 5) + 32
    where F = degrees Fahrenheit, and C = degrees Celsius
    
    
    
    (4) Ask the user to enter the episode name in the initial format
    Convert it to the new format
    Print the converted episode name
    
Lab_2

    What to do:
    1. Ask the user for a name and age of a character.
    2. Print out a message displaying the character's age and 
    listing the characters who are older than the given character (print nothing if there are none)
    3. Print out a message displaying the character's age and 
    listing the characters who are younger than the given character (print nothing if there are none)
    
    If the entered age is negative, print "Invalid age."

    (There are hardcoded names and age of 8 persons, all the comparisons of our character are made with this list)
    We may not use dictionaries 



Lab_3

    What to do:
    1. Read data from klingon-english.txt
    2. Ask the user to choose a Klingon consonant they want to practice with. 
    Ask again if the user’s answer is not a valid Klingon consonant, until the user enters a valid consonant.
    3. Find a Klingon word that starts with the chosen consonant 
    (the text file contains only one word that starts with any given consonant, so you don’t need to use the random library)
    4. Ask the user to translate the chosen word into Klingon
    5. Print Correct if the user’s answer is correct
    6. Print Sorry, you’re wrong! if the user’s answer is wrong
    7. If the answer is incorrect, show the first hint: the first and last characters 
    of the correct Klingon word. When showing a hint, replace all other characters with a star (*)
    8. If the answer is still incorrect, show the second hint: 
    the first and the last characters plus an extra random character of the correct Klingon word.
    9. Print The correct answer is ... if all three user’s answers are wrong



Lab_4

    What to do:
    Your program must try to decipher a given message with the following ciphers and combinations:

    Caesar cipher
    Atbash cipher
    Combined: first apply Caesar cipher, then Atbash cipher
    Combined: first apply Atbash cipher, then Caesar cipher
    A1Z26 cipher
    Combined: first apply A1Z26 cipher, then Caesar cipher
    Combined: first apply A1Z26 cipher, then Atbash cipher
    Combined: first apply A1Z26 cipher, then Atbash cipher, then Caesar cipher
    Combined: first apply A1Z26 cipher, then Caesar cipher, then Atbash cipher


Lab_5

    What to do:
    1. Implement the read_spells() and get_random_spell() functions.
    2. Read spells from the text file (spells.txt)
    3. Display the header
    4. Display the instructions (read the instructions from instructions.txt)
    5. Choose a random spell
    6. Get the user’s input and compare it with the chosen spell
    7. If the user typed the spell correctly, display Correct! Otherwise, display: Incorrect! The spell was chosen_spell
    8. You need to implement the display_header() and display_instructions(), get_user_input(), and display_feedback() functions.
    9. Implement the play_again() function that would ask the user if they want to play again.
    10. Add a game loop to your main() function. After each attempt, your program should call the play_again() function:
    a) If the user wants to continue, show another spell
    b) Otherwise, print the final score and quit.
    11. Add scoring functionality to your main() function:
    a) For each correct answer, add 10 points to the score and print the score
    b) For each incorrect answer, subtract 5 points from the score and print the score
    The total score can be negative.
    12. Implement the new get_target_time() function to calculate the target time (TTT) using the formula above.
    13. Finally, implement the calculate_points() function to calculate the score using the approach above.





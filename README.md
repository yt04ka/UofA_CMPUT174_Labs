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

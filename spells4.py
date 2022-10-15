"""
    This is part 4 of lab 5 (simplified, full of things that could
    be done easier and in better way because of the requirements)
    Written by Roman Kobryn
    This program allows user to practice in typing spells and grades user
    depending on speed and accuracy of his typing
"""

import random
import time


def display_header() -> None:
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """

    print(f"\n{'#' * 60} \nHarry Potter Typing Trainer \n{'#' * 60}\n")


def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    # could be written as a line of code in main
    print(f"{open('instructions.txt', 'r').read()}\n")


def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """

    # also a line of code
    return [line.strip() for line in open(filename, "r").read()]


def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """

    # still a line of code
    return spells[random.randint(0, len(spells))]


def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """

    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time


def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """

    # one more function that could be a line of code
    return len(spell) * 0.3


def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """

    targeted_total_time = get_target_time(spell)
    delta = 0
    if user_input.lower() == spell.lower():
        if user_time <= targeted_total_time:
            delta += 10
        elif user_time <= targeted_total_time * 1.5:
            delta += 6
        elif user_time <= targeted_total_time * 2:
            delta += 3
        else:
            delta += 1
    else:
        delta -= 5
    # is it better morally to use global, up
    calculate_points.overall_score += delta
    globals().update()
    return calculate_points.overall_score


calculate_points.overall_score = 0


def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """

    choice = input(f"\nDo you want to continue the game?\n"
                   f"Press 'y' if You want to continue the game, "
                   f"if you want to end the game and see your score press 'n'\n\n"
                   f"(y/n)? > ")
    flag = the_choice(choice)

    return flag


def the_choice(choice: str) -> bool:
    """
    returns bool variable depending on pressed key
    """
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        print(f"\nYour input was incorrect. Please try again")
        choice = input(f"(y/n)? > ")
        the_choice(choice)


def continue_playing(flag: bool, spells: list[str], score: int) -> None:
    """
    Checks return of the play_again() and continues the game or ends it
    """
    if flag:
        spell = get_random_spell(spells)
        calculate_points(spell, *get_user_input(spell))
        continue_playing(play_again(), spells, score)
    else:
        results(score)


def results(score: int):
    """
    Ends program, printing the score
    """
    # finally, the last function that could be a line of code
    exit(print(f"\nYour score is {score}. \nSee you next time!"))


def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    spell = get_random_spell(spells)
    calculate_points(spell, *get_user_input(spell))
    continue_playing(play_again(), spells, calculate_points.overall_score)


if __name__ == '__main__':
    main()

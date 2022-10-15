"""
    This is part 4 of lab 4
    Written by Roman Kobryn
    This program allows user to practice in typing spells and grades user
    depending on speed and accuracy of hia typing
"""

import random
import time


def user_input(spell: str) -> tuple[str, float]:
    """
    This function gets the input from user and the time that user was typing it
    :param spell: spell from the list of spells
    :return: input_spell: spell, total_time: amount of time that user was inputting the spell
    """

    time_start = time.time()
    input_spell = input(f"Type the following spell: {spell} \n > ")
    time_end = time.time()
    total_time = round(time_end - time_start, 2)

    return input_spell, total_time


def spell_check(spell: str, overall_score: int, input_spell: str, total_time: float) -> tuple[None, int]:
    """
    This function is used to check the spelling of the spell and calculate the overall score
    :param spell: spell from the list
    :param overall_score: overall score
    :param input_spell: inputted spell
    :param total_time: time spent on imputing the spell
    :return: overall_score: overall score
    """

    targeted_total_time = len(spell) * 0.3
    if spell.lower() == input_spell.lower():
        overall_score = score_calculator(total_time, targeted_total_time, overall_score)
        return print(f"\nCorrect!"), overall_score
    else:
        overall_score -= 5
        return print(f"\nIncorrect!"), overall_score


def score_calculator(total_time: float, targeted_total_time: float, overall_score: int) -> int:
    """
    This function is used to calculate score of this spell and ad dit to overall score
    :param total_time: time that was spent on inputting the spell
    :param targeted_total_time: estimated time to write the spell
    :param overall_score: overall score
    :return: overall_score: overall score
    """

    if total_time <= targeted_total_time:
        overall_score += 10
    elif total_time <= targeted_total_time * 1.5:
        overall_score += 6
    elif total_time <= targeted_total_time * 2:
        overall_score += 3
    else:
        overall_score += 1

    return overall_score


def play_again(spells: list, overall_score: int) -> None:
    """
    This function is used to continue practicing or to exit the program
    :param spells: list of spells
    :param overall_score: overall score
    :return: None
    """

    choice = input(f"\nDo you want to continue the game?\n"
                   f"Press 'y' if You want to continue the game, "
                   f"if you want to end the game and see your score press 'n'\n\n"
                   f"(y/n)? > ")
    the_choice(choice, spells, overall_score)


def the_choice(choice: str, spells: list, overall_score: int) -> None:
    """
    This function is used to continue the program or end it and print results
    :param choice: string that shows what user wants to do
    :param spells: list of spells
    :param overall_score: overall score
    :return: None
    """

    if choice == "y":
        cycle(spells, overall_score)
    elif choice == "n":
        exit(print(f"\nYour score is {overall_score}. \nSee you next time!"))
    else:
        print(f"\nYour input was incorrect. Please try again")
        choice = input(f"(y/n)? > ")
        the_choice(choice, spells, overall_score)


def cycle(spells: list, overall_score: int) -> None:
    """
    This function is used to continue typing practice
    :param spells: list of spells
    :param overall_score: overall score
    :return: None
    """

    spell = spells[random.randint(0, len(spells))]
    overall_score = spell_check(spell, overall_score, *user_input(spell))[1]
    play_again(spells, overall_score)


def main() -> None:
    """
    Main function of the program
    :return: None
    """

    overall_score = 0

    print(f"\n{'#' * 60} \nHarry Potter Typing Trainer \n{'#' * 60}\n")
    print(f"{open('instructions.txt', 'r').read()}\n")

    spells = [line.strip() for line in open("spells.txt", "r").read()]
    spell = spells[random.randint(0, len(spells))]
    overall_score = spell_check(spell, overall_score, *user_input(spell))[1]
    play_again(spells, overall_score)


if __name__ == '__main__':
    main()

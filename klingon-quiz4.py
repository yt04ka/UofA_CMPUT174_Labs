"""
    This is part 4 of lab 3
    Written by Roman Kobryn
    This program allows user to practice Klingon language by choosing a consonant and trying to guess the translation
"""

import random

klingon_consonants = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y", "'"]
dictionary = open("klingon-english.txt", "r")


def input_character() -> str:
    """
        This function gets the character from the user
        :return: consonant: character
    """
    consonant = input("Please input the Consonant you would like to practice with > ")
    if consonant not in klingon_consonants:
        consonant = input("Your character is incorrect. Please try again > ")
        if consonant not in klingon_consonants:
            exit(print("Try learning consonants of Klingon first, then come back to practice"))
    return consonant


def word_search(consonant: str) -> tuple[str, str]:
    """
       This function searches for the word to train and translation in the file
       :param consonant: consonant to search for
       :return: tuple of word to train and translation
    """

    for line in dictionary:
        if consonant in line[0:2]:
            word_to_train, translation = line.split("|")
            return word_to_train, translation.strip()
    else:
        exit(print("There is no such consonant in the dictionary. Please try again"))


def word_guessing(word_to_train: str, translation: str) -> None:
    """
        This function is used for guessing the word
        :param word_to_train: word to train
        :param translation: translation of the word
        :return: None
    """

    attempt = input(f"Try to guess how {translation} is written in Klingon > ")
    if attempt == word_to_train:
        print(f"Well done! The translation of {translation} is {word_to_train}")
    else:
        print(f"Wrong guess( The first and last characters are {word_to_train[0]} and {word_to_train[-1]}")
        attempt = input("Try to guess once more > ")
        if attempt == word_to_train:
            print(f"Well done! The translation of {translation} is {word_to_train}")
        else:
            second_hint(word_to_train)
            attempt = input("This is your last chance to guess the word right. Please input > ")
            if attempt == word_to_train:
                print("Well done! Soon you'll master the Klingon")
            else:
                exit(print(f"You are out of attempts and hints. The translation of {translation} is {word_to_train}"))


def second_hint(word_to_train: str) -> None:
    """
        This function creates a hint for the user - first, last and random symbol
        inside the word to train are revealed, rest is shown like "*"
        :param word_to_train: word to train
        :return: None
    """
    i = len(word_to_train)
    random_consonant_position = random.randint(1, i - 2)

    result = [word_to_train[i] if i in (0, len(word_to_train) - 1, random_consonant_position) else "*" for i in
              range(len(word_to_train))]

    result = "".join(result)
    print(f"Wrong guess again! You have only one more attempt.'Hint - the word should look like {result}'")


def main() -> None:
    """
       Main function of the program
    """
    word_guessing(
        *word_search(
            input_character()
        )
    )


if __name__ == '__main__':
    main()

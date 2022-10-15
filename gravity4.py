"""
    This is part 4 of lab 4
    Written by Roman Kobryn
    This program allows user to decrypt a message using 3 different decryption ways -
    Caesar's cipher with step of 3 to the left (d->a),(e->b)...
    Atbash cipher (a->z),(b->y)...
    A1Z26 cipher (1->a)(2->b)...
"""

# Constants which could be named meaningfully to use further in the code
LETTER_MIN_ORD = ord('a')
LETTER_MAX_ORD = ord('z')
NUMBER_MIN_ORD = ord('0')
NUMBER_MAX_ORD = ord('9')

CAESAR_SHIFT = 3
ALPHABET_LENGTH = 26

ATBASH_CONSTANT = 219

A1Z26_CONSTANT = 96


def get_data() -> str:
    """
        This function is used to get encrypted message from the keyboard
        :return: cipher: string which contains the message
    """

    cipher = input("Please input encrypted message to decrypt it here > ")
    return cipher


def caesar_decipher_symbol(symbol: str) -> str:
    """
        This function decrypts symbol using Caesar's cipher with shift of 3 characters to the left,
        if the symbol was a,b or c it adds to the symbol length of the alphabet, so function chr()
        returns proper letter from the ASCII table
        :param: symbol: encrypted symbol
        :return: decrypted_symbol: decrypted symbol
    """

    symbol_code = ord(symbol)

    decrypted_symbol = chr(
        symbol_code - CAESAR_SHIFT
    )

    if ord(decrypted_symbol) < LETTER_MIN_ORD:
        decrypted_symbol = chr(ord(decrypted_symbol) + ALPHABET_LENGTH)

    return decrypted_symbol


def atbash_decipher_symbol(symbol: str) -> str:
    """
        This function decrypts a symbol using atbash cipher
        :param: symbol:
        :return: decrypted_symbol: decrypted symbol
    """

    symbol_code = ord(symbol)

    decrypted_symbol = chr(
        ATBASH_CONSTANT - symbol_code
    )

    return decrypted_symbol


def caesar_cipher(cipher: str) -> str:
    """
        This function decrypts a message using caesar_decipher_symbol() for every element of the message,
        if symbol is not a lowercase letter of English alphabet is stays same
        :param: cipher: encrypted message
        :return: decrypted_message: decrypted message
    """

    decrypted_message = "".join(
        caesar_decipher_symbol(character)
        if LETTER_MIN_ORD <= ord(character) <= LETTER_MAX_ORD else character
        for character in cipher
    )

    return decrypted_message


def atbash_cipher(cipher: str) -> str:
    """
        This function decrypts a message using atbash_decipher_symbol() for every element of the message,
        if symbol is not a lowercase letter of English alphabet is stays same
        :param: cipher: encrypted message
        :return: decrypted_atbash: decrypted message
    """

    decrypted_message = "".join(
        atbash_decipher_symbol(character)
        if LETTER_MIN_ORD <= ord(character) <= LETTER_MAX_ORD else character
        for character in cipher
    )
    return decrypted_message


def a1z26_cipher(cipher: str) -> str:
    """
        This function is used to decrypt a cipher using a1z26 method
        :param: cipher: encrypted message
        :return: decrypted_atbash: decrypted message
    """

    """
            This section of code goes through the parameter and splits it by " " (space) then it splits every element 
            of the resulting list by "-". After it converts every number to the corresponding letter in 
            English alphabet and adds it to the decrypted_a1z26 string, and if there are symbols after 
            the letter it adds them to the decrypted string without changing
    """

    decrypted_a1z26 = ''
    encrypted_words_a1z26 = cipher.split(' ')

    for word in encrypted_words_a1z26:
        encrypted_a1z26 = str(word).split('-')

        for index in encrypted_a1z26:
            """
            This block of code runs through every element of the encrypted_a1z26 list and tries to decrypt them,
            I use Try,Catch block because we could have statement like fun!, and n! will be shown in a1z26 as
            "14!", and int(index) will not be able to process it, so we catch ValueError, and we have if block
            to check whether we have 2 digit number or 1, or even we do not have digits there (I assume that special 
            symbols can't be typed before the number here, in that case it will just give us this element of list
            as it is(!14! will remain unchanged))
            After checking the number of digits I have every case covered in if statements, so it will work any time
            (I strongly assume that - is not the symbol that will be used in the text)
            Also in case that we have number that is bigger than 26, it will stay as number
            """
            try:
                if 1 <= int(index) <= ALPHABET_LENGTH:
                    decrypted_a1z26 += chr(int(index) + A1Z26_CONSTANT)

                else:
                    decrypted_a1z26 += index

            except ValueError:
                if len(index) > 2:
                    if NUMBER_MIN_ORD <= ord(index[0]) <= NUMBER_MAX_ORD:
                        if NUMBER_MIN_ORD <= ord(index[1]) <= NUMBER_MAX_ORD:
                            decrypted_a1z26 += (chr(int(index[0:2]) + A1Z26_CONSTANT))
                            decrypted_a1z26 += (index[2:])

                        else:
                            decrypted_a1z26 += (chr(int(index[0:1]) + A1Z26_CONSTANT))
                            decrypted_a1z26 += (index[1:])

                    else:
                        decrypted_a1z26 += index
                else:
                    if NUMBER_MIN_ORD <= ord(index[0]) <= NUMBER_MAX_ORD:
                        decrypted_a1z26 += (chr(int(index[0:1]) + A1Z26_CONSTANT))
                        decrypted_a1z26 += (index[1:])

                    else:
                        decrypted_a1z26 += index

        decrypted_a1z26 += ' '

    return decrypted_a1z26


def main() -> None:
    """
        Main function of the program
        Prints decrypted message using 8 different combinations of 3 different decrypting methods
        :return: None
    """
    cipher = get_data()

    decrypted_message = caesar_cipher(cipher)
    print(f"Caesar cipher: {decrypted_message}")

    decrypted_message = atbash_cipher(cipher)
    print(f"Atbash cipher: {decrypted_message}")

    decrypted_message = caesar_cipher(
        atbash_cipher(cipher)
    )
    print(f"Combined: 1) Atbash; 2) Caesar cipher: {decrypted_message}")

    decrypted_message = atbash_cipher(
                            caesar_cipher(cipher)
                        )
    print(f"Combined: 1) Caesar; 2) Atbash cipher: {decrypted_message}")

    decrypted_message = atbash_cipher(
        a1z26_cipher(cipher)
    )
    print(f"Combined: 1) A1Z26; 2) Atbash cipher: {decrypted_message}")

    decrypted_message = caesar_cipher(
        a1z26_cipher(cipher)
    )
    print(f"Combined: 1) A1Z26; 2) Caesar cipher: {decrypted_message}")

    decrypted_message = caesar_cipher(
                            atbash_cipher(
                                a1z26_cipher(cipher)
                            )
                        )

    print(f"Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: {decrypted_message}")

    decrypted_message = atbash_cipher(
                            caesar_cipher(
                                a1z26_cipher(cipher)
                            )
                        )
    print(f"Combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: {decrypted_message}")


if __name__ == '__main__':
    main()

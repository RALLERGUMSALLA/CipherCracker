from helpers.alphabet import ALPHABET
from helpers.validation import character_verification

'''
Caeser cypher shifts all letters a specific amount down the alphabet line which loops
'''
def brute_force_caesar():
    gap = len(ALPHABET)

    print("Input Caesar Cipher to Brute-Force")
    word = input()
    result = ""

    valid, invalid_char = character_verification(
        word,
        allow_letters=True,
        allow_digits=True,
        allow_whitespace=True,
        allowed_characters=".,!?'-"
    )

    if not valid:
        print(f"Invalid character {invalid_char} found")
        return

    for i in range(gap):
        result = ""

        for character in word:

            # Preserve non-letters
            if not character.isalpha():
                result += character
                continue

            index = ALPHABET.index(character.lower())
            new_index = (index + i) % len(ALPHABET)

            result += ALPHABET[new_index]

        print(f"Gap = {i} - {result}")
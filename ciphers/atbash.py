from helpers.alphabet import ALPHABET
from helpers.validation import character_verification

'''
Atbash cipher reverses the alphabet index, so;
a = 25
b = 24
'''
def atbash_cipher():
    print("Input Atbash Cipher Solve")
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
    for character in word:
        # Preserve non-letters
        if not character.isalpha():
            result += character
            continue
        else:
            index = ALPHABET.index(character.lower())
            new_index = len(ALPHABET) - 1 - index
            result += ALPHABET[new_index]
            # print(f"{result} + {new_index} + {index}")
    return print(result)
from helpers.alphabet import BACONIAN_ALPHABET
from helpers.validation import character_verification

BACONIAN_DECODE = {
    value: key
    for key, value in BACONIAN_ALPHABET.items()
}


def decode_bacon():
    print("Input Baconian Code to Decode")
    bacon_code = input().upper()

    valid, invalid_char = character_verification(
        bacon_code,
        allow_letters=True,
        allow_whitespace=True
    )

    if not valid:
        print(f"Invalid character {invalid_char} found")
        return

    for code in bacon_code.split():

        if code in BACONIAN_DECODE:
            print(BACONIAN_DECODE[code], end="")
        else:
            print(f"\nInvalid Baconian code {code} found")
            return

    print()


def encode_bacon():
    print("Input Text to Encode in Baconian Code")
    text = input().upper()

    valid, invalid_char = character_verification(
        text,
        allow_letters=True,
        allow_whitespace=True
    )

    if not valid:
        print(f"Invalid character {invalid_char} found")
        return

    for character in text:

        if character.isspace():
            print("/", end=" ")
            continue

        if character in BACONIAN_ALPHABET:
            print(BACONIAN_ALPHABET[character], end=" ")
        else:
            print(f"\nInvalid character {character} found")
            return

    print()
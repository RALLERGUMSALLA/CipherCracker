from helpers.alphabet import morse_dict
from helpers.validation import character_verification

def decode_morse():
    print("Input Morse Code to Decode")
    morse_code = input()

    valid, invalid_char = character_verification(
        morse_code,
        allow_letters=False,
        allow_digits=False,
        allow_whitespace=True,
        allowed_characters=".-/"
    )

    if not valid:
        print(f"Invalid character {invalid_char} found")
        return
    
    for character in morse_code.split(" "):
        if character == "":
            print(" ", end="")
            continue
        elif character in morse_dict:
            print(morse_dict[character], end="")
        else:
            print(f"Invalid Morse Code {character} found")
            return
        
def encode_morse():
    print("Input Text to Encode in Morse Code")
    text = input()

    valid, invalid_char = character_verification(
        text,
        allow_letters=True,
        allow_digits=True,
        allow_whitespace=True,
        allowed_characters=".,!?'-"
    )

    if not valid:
        print(f"Invalid character {invalid_char} found")
        return
    
    for character in text:
        if character == " ":
            print("/", end=" ")
            continue
        elif character.upper() in morse_dict.values():
            morse_code = list(morse_dict.keys())[list(morse_dict.values()).index(character.upper())]
            print(morse_code, end=" ")
        else:
            print(f"Invalid character {character} found")
            return
def character_verification(
    text,
    allow_letters=False,
    allow_digits=False,
    allow_whitespace=False,
    allowed_characters=""
):
    for character in text:
        if allow_whitespace and character.isspace():
            continue
        if allow_letters and character.isalpha():
            continue
        if allow_digits and character.isdigit():
            continue
        if character in allowed_characters:
            continue
        return False, character

    return True, None


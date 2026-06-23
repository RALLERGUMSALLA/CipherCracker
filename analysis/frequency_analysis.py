from helpers.validation import character_verification

def frequency_analysis_tool():
    text = input("Enter text: ")
    percentages = {}
    counts = {}

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
    else:
        text = text.lower()
        clean = text.replace(" ", "")
        
    for character in clean:
        counts[character] = counts.get(character, 0) + 1
    for character in counts:
        percentages[character] = counts[character] / len(clean) * 100
    for character, frequency in sorted(
        percentages.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(
            f"Letter: {character}, "
            f"Count: {counts[character]}, "
            f"Frequency: {frequency:.2f}%"
        )

    

    
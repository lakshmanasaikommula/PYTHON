n = input()

for character in n:
    if character.upper() == character:
        if not character.isdigit():
            print(character)
            break
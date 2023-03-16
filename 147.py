word = input()

first_space_index = 0
for char in word:
    if char == " ":
        break
    first_space_index = first_space_index + 1

upper_case_word = word[:first_space_index].upper()
new_word = upper_case_word + word[first_space_index:]

print(new_word)


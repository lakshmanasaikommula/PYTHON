password = input()

contains_digit = False

for char in password:
    is_digit = char.isdigit()
    if is_digit:
        contains_digit = True

if contains_digit:
    print("Valid passsword")
else:
    print("not a valid password")
p = input()
is_digits = False
is_upper = False
is_lower = False

for i in p:
    if i == i.isdigit():
        is_digits = True
    elif i == i.isupper():
        is_upper = True
    elif i == i.islower():
        is_lower = True

result = (is_digits+is_lower+is_upper)

if result:
    print("valid")
else:
    print("not")
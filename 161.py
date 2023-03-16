#subsequence

a = input()
b = input()

b_index = 0
b_lenght = len(b)
for char in a:
    if char == b[b_index]:
        b_index += 1
        if b_index == b_lenght:
            break

if b_index == b_lenght:
    print("Yes")
else:
    print("No")
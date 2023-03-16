a = input()
a = a.lower()
d = []
e = []

for i in a:

    if (i.isdigit()) or (i.isalpha()):
        if i not in d:
            d.append(i)
    else:
        e.append(i)
# print(e)
# print(d)
for i in d:
    print(i, a.count(i))
print("spacial_characters", len(e))
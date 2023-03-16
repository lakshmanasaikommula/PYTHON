a=input()

new=' '
for char in a:
    if char ==" ":
        new += char
        continue
    else:
        asci=ord(char)
        new_num1= asci+1
        new = new + chr(new_num1)
print(new)
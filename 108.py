string = input().lower()

flag=0
j=-1
for i in string:
    if i != string[j]:
        flag=1
        break
    j = j-1
if flag==1:
    print(string,' = ',"Not A Palindrome")
else:
    print(string,' = ',"Palindrome")

''' this lesson is to printing pyraminds with alphabits so
we need to know the ASCII Codes for the alphabits which are

A-Z = 65-90
a-z = 97-122
0-9 = 48-57 '''


n = 5
p=65
for i in range(n+1):
    for j in range(i):
        print(chr(p), end=' ')
        p+=1
    print()
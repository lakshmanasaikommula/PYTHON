s = input()

vowels = ['a','e','i','o','u','A','E','I','O','U']

for i in s:
    for j in vowels:
        if i==j:
            s = s.replace(j,'')
print(s)
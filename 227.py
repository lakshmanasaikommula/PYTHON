'''In a given word print the count of characters which are not vowels (ignore, upper or lower)
Ex:
Input: Hello
Output:H=1,l=2'''

n = str(input()).lower()

vowels =['a','e','i','o','u']

for i in n:
    for j in vowels:
        if i==j:
            print(i,'= vowels')
        elif i!=j:
            print(i,'= not a vowels')
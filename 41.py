#string repetation

string = input()
s = int(input())
word =' '
for i in string:
    word = word + (s * i)
print(word)

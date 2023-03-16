n = 'no lemon no melon!'
word=''
for i in n:
    if i!= "'" and i!= ' ' and i!= '!':
        word = word + i
print(word)
reversed_word = word[::-1]

if word == reversed_word:
    print("palinfrome")
else:
    print("n")
n = 'no lemon no, melon'

word=''

for i in n:
    if i != "'" and i.isspace() == False:
        word =  i.lower() +word
reversed_word=(word[::-1])

if word == reversed_word:
    print('Palindrome')
else:
    print('Not a palindrome')




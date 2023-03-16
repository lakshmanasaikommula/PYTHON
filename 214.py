'''Write a code to print constant count and vowel count.
Input: rajar
output:r=2 j=1 vowel=2
'''

word = 'rajar'
vowel=0
for char in range(len(word)):
    if word[char] == 'a' or word[char] == 'e' or word[char] == 'i' or word[char] == 'o' or word[char] == 'u':
        vowel= vowel+1
    else:
        print(word[char], '=', word.count(word[char]),end=' ')

print('vowel','=',vowel,end=' ')

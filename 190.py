


s = 'sai'

vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in s:
    for j in vowels:
        if i==j:
            count = count+1
print(count)








'''def count_the_vowels(word):
    count = 0
    for letter in word:
        is_a = letter == 'a'
        is_e = letter == 'e'
        is_i = letter == 'i'
        is_o = letter == 'o'
        is_u = letter == 'u'
        is_vowel = ((((is_a or is_e)or is_i) or is_o) or is_u)
        if is_vowel:
            count += 1
    return count
    # Complete this function


word = input()
result = count_the_vowels(word)
print(result)'''
# Call the count_the_vowels function
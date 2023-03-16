a = "hello aliens hows your day..."

word = a.split()

reversed_word = []

for i in word:
    reversed_word = reversed_word + [i[::-1]]
print(reversed_word)
result = ' '.join(reversed_word)
print(result)
#acronyms
word = input().split()
print(word)

result = ''

for w in word:
    result = result + w[0] +'. '
    result = result[:-1]
    print(result[0:-1])




'''result = ''
for w in input().split():
    result += w[0] + '. '
    result = result[:-1]
print(result[0:-1])'''
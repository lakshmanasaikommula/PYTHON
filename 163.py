#hypen letters
string = 'kommula lakshmana sai'

length = len(string)

a = string[0]

for i in range(1,length):
    a = a + '-' + string[i]
print(a)
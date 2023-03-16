# charecter frequency

word = 'lakshmana sai kommula'

string=''

for char in word:
    if char not in string:
        if char != ' ':
            print(char, '=', word.count(char),end=', ')
    string = string + char

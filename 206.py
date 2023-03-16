# number frequency

a = 'raja11223labs'
b = ''
others=0
for i in a:
    if i not in b:
        if i.isdigit():
            print(i,'=',a.count(i),end=', ')
        else:
            others = others +1

    b = b+i
print('others = ',others)


'''alphabets = special = 0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        print('""',string[i],'""','=', string.count(string[i]), end=', ')
    else:
        special = special + 1
print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Special Characters in this String :  ", special)'''
'''Write a program to print first non repeating character of a string
Example:
Input :  amazon
Output : m'''

string = 'amazon'
alphabets = ''

for i in range(len(string)):
    if(string[i].isalpha()):
        if string.count(string[i]) == 1:
            print(string[i])
            break

'''Print the non repeating characters from the string
Example:
Input= “daddy”
Output= “ay”'''

a = 'daddy'

for i in range(len(a)):
    if a.count(a[i]) ==1:
        print(a[i],end='')



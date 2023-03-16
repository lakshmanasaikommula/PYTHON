'''Write a program to print the frequency of these characters b, f, j, p, v in a given string and also print the total count of these characters. (Ignore the character cases, it can be lower or upper case) The function will take 1 parameter which will be a String (you do not have to write code to get the input parameter from the user). You can also choose to take a character array as input parameter, instead of string, if you like
int frequencyOfCharacters(String input) {
// TODO:
}
Example:
Input: rajasoftwarelabs Output: b=1, f=1, j=1, Total=3
Input: Buffet Output: b=1, f=2, Total=3'''

a = 'rajasoftwarelabs'

for i in range(len(a)):
    if (a[i]) == 'b' or (a[i])=='f' or (a[i]) == 'j' or (a[i]) == 'p' or (a[i]) == 'v':
        print(a[i],'=',a.count(a[i]),end=', ')

print('total')


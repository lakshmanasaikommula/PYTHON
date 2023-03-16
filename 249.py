'''Write a function that takes an array of numbers as input parameter and prints the numbers that have
remainder of 4 when divided by 5.
Example:
Input: [19,10,44,3,11,129] Output: 19 44 129
Input: [13,4] Output: 4'''

arr=[19,10,44,3,11,129]

for i in arr:
    if i%5==4:
        print(i,end=' ')

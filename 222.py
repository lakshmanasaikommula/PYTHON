'''Check whether the given number is in the fibonacci series or not.
Example:
Input1= 8 - Search number
Input2= 0,1,1,2,3,5,8,13- Fibonacci series
Output= Yes the given number is in the fibonacci series'''

n = int(input())

a = 0
b = 1
result =' '
for i in range(n):
    sum = a+b
    a=b
    b =sum
    result = result + str(sum)

for i in result:
    if i == str(n):
        print("yes")
        break
else:
    print('no')
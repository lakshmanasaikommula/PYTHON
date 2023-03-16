'''Write the programme for Fibonacci numbers in given input?
Example:
Input= 8
Output= 0,1,1,2,3,5,8,13'''

n = int(input())

a = 0
print(a)
b=1
print(b)
sum=0
for i in range(2,n):
    sum = a+b
    a = b
    b = sum
    print(sum,end=',')
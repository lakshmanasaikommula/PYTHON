#Fibonacci series
n = int(input())

a =0
print(a,end=' ')
b =1
print(b,end=' ')
for i in range(2,n):
    next =a+b
    a=b
    b=next
    print(next,end=' ')


'''a = int(input('firstnumber:'))
b = int(input('secondnumber:'))
n = int(input('NumberOfElements:'))

print(a,b, end=" ")
while (n-2):
    c = a+b
    a = b
    b = c
    print(c,end=" ")
    n=n-1'''
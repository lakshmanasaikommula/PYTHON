n = int(input())

a =0
print(a)

b =1
print(b)

for i in range(2,n):
    next = a+b
    print(next,end='')
    a=b
    b = next

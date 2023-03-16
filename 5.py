#printing pyramids

n = 5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('1',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

print('----------------------')
for i in range(n):
    for j in range(i+2):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('1',end=' ')
    for j in range(i,n-2):
        print('*',end=' ')
    print()













'''n = (2*num)-2
for i in range(0,num):
    for j in range(0,n): #nested loops
        print(end="  ")
    n = n-1
    for j in range(0,i+1):
        print('* ', end ="  ")
    print(" ")'''

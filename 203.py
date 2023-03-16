a ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

l = int(input())

for i in range(l):
    for j in a:
        print(j*i,end=' ')
    print()


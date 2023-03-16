n =10

for i in range(n):
    for j in range(n):
        if ((j==0) or (i==0) or j==n-1-i):
            print("* ",end='  ')
        else:
            print('  ',end='  ')
    print()

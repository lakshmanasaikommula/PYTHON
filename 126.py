n = 5

for i in range(n):
    for j in range(i, n):
        print('  ', end='  ')

    for j in range(i):
        if (i == n - 1 or j == 0):
            print('* ', end='  ')
        else:
            print('  ', end='  ')
    for j in range(i + 1):
        if (i == n - 1 or j == i):
            print('* ', end='  ')
        else:
            print('  ', end='  ')
    print()
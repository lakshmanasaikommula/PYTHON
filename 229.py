'''Write a function that takes input as an integer number and prints the closest prime integer to that number. The closest prime can be greater or smaller than the passed input integer. If there are equi-distant prime-numbers, print both
Example:
Input= 4
Output= 3
Example:
Input=5
Output= 3,7'''


def prime(n):
    isprime = True
    if n < 2:
        isprime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                isprime = False
                break
    return isprime


n = 4
flag, i = True, 1

if prime(n):
    print('Closest prime number =', n)
else:
    while flag:
        if prime(n + i) and prime(n - i):
            print(n - i, 'and', n + i, 'are closest prime numbers')
            flag = False
        elif prime(n - i):
            print('Closest prime number =', n - i)
            flag = False
        elif prime(n + i):
            print('Closest prime number =', n + i)
            flag = False
        i += 1
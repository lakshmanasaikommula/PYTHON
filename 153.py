#sum of non primes

n = int(input())

is_primes =[]

for i in range(n):
    read = int(input())
    is_primes.append(read)

non_primes = []

for num in is_primes:
    if num==2 or num==3:
        pass
    else:
        for i in range(2,num):
            if num%i ==0:
                non_primes.append(num)
                break
print('sum = ',sum(non_primes))
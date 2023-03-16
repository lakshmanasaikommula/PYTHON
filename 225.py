'''Print sum of non prime numbers in a given array
Example:
Input= [4,2,5,7,1]
Output= 2+5+7= 14'''

a = [4,2,5,7,1]

primes=[]
non_primes=[]
for i in a:
    for j in range(2,int(i)):
        if int(i)%j ==0:
            non_primes.append(i)
        print(non_primes)
else:
    primes.append(i)
    print(primes)
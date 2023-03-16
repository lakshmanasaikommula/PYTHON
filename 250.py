'''Print the sum of non prime
numbers in the given input?'''

arr = [1,89,3,4]
primes=[]
non_primes=[]
for i in range(len(arr)):
    for i in range(2,int(arr[i])):
        if i%2==0:
            non_primes.append(i)
else:
    primes.append(i)

print(primes)
print(non_primes)

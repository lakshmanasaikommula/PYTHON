n = int(input())
k = int(input())
factors = []
for i in range(n):
    if (n % (i+1)) == 0:
        factors.append(i+1)
if k > len(factors):
    print(1)
else:
    print(factors[-k])
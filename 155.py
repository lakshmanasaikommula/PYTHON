# sum of harmonic
n = int(input())

sum=0

for i in range(1,n+1):
    sum = sum + 1/i
print(round(sum,2))
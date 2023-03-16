n = int(input())

num='2'

total = 0

for i in range(1,n+1):
    term = num * i
    total = total + int(term)
print(total,end=' ')
#reverse number order

n = int(input())
l=[]

for i in range(n):
    a =input()
    l+=[a]
for j in range(n):
    print(l[n-j-1])

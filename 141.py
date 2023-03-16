m = int(input())
n = int(input())

if m>n:
    small_num=n
else:
    small_num = m

gcd=0

for i in range(1,small_num+1):
    if (m%i)==0 and (n%i)==0:
        gcd = i
print(gcd)
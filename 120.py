n = int(input())

length = len(str(n))

sum= 0

for i in str(n):
    sum = sum+ (int(i)**length)
print(sum)

if n==sum:
    print(n,' = ','Its an Armstrong Number')
else:
    print(n,' = ','Its Not an Armstrong Number')
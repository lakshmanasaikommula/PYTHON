n = int(input())
m=n
sum=0; m = n*n
while m!=0:
    d=m%10
    sum = sum+d
    m = m//10

if sum ==n:
    print("Neon Number")
else:
    print("Not a Neon Number")
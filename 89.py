n = int(input())
m=n
sum=0; prod=1
while m!=0:
    d=m%10
    sum = sum+d; prod = prod *d
    m = m//10

if sum ==prod:
    print("Spy Number")
else:
    print("Not a Spy Number")
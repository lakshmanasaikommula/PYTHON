#prime or not
n = int(input())

if n==1:
    print("Prime")
elif n==2:
    print("Prime")

for i in range(2,n+1):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("Prime")
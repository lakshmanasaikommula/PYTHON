n = int(input())

fact=0
for i in range(1,n):
    if n%i == 0:
        if(i*(i+1)==n):
            fact = i

if fact != 0:
    print("Pronic Number")
else:
    print("Not a Pronic Number")
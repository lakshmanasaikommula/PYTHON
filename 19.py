#prime number

n = int(input())

for i in range(2,n):
    if n%i == 0:
        print("Its not a prime number")
        break
else:
    print("Its a prime number")



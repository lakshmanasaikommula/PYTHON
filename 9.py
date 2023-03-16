#prime Number

num = int(input('enter a number: '))

for i in range(2,num):
    if num%i ==0:
        print("Its not a prime number")
        break
else:
    print("its a prime number")


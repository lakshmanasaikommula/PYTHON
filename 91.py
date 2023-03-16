n = int(input())
m=n
sum=0
while m!=0:
    d=m%10
    sum = sum+d
    m = m//10

if m%sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
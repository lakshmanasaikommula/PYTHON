n = int(input())
m=n
count = 0
while m!=0:
    d=m%10
    if d ==0: count += 1
    m = m//10

if count>0:
    print("DUCK Number")
else:
    print("Not a DOCK Number")
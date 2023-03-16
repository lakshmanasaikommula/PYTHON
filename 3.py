#armstrong number or not

n = int(input())

l = len(str(n))
result=0
for i in str(n):
    result = result + int(i) ** int(l)
print(result)

if n == result:
    print(n,' = ',"Its an Armstrong Number")
else:
    print(n,' = ',"Its not an Armstrong Number")


'''num = int(input('Enter a Number: '))
counter = 0
count = num
while count>0:
    c = count%10
    counter += c ** 3
    count //=10
if num==counter:
    print("Armstrong Number")
else:
    print("Its not Armstrong Number")'''

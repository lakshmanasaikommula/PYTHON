n =153

length = len(str(n))

temp = n

result =0

for i in str(n):
    digit = temp%10
    result = result + (digit**length)
    temp = temp//10
if n ==result:
    print("Armstrong")
else:
    print("Not")
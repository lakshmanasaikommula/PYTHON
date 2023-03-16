#armstrong
A = int(input())
B = int(input())
count = 0
for num in range(A, B + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + ( digit ** order)
        temp = temp// 10
    if num == sum:
        print(num,end=" ")
        count += 1
if count == 0:
    print("-1")
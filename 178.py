a = input().split(',')
b = input().split(',')

print(reversed(a))

print(a)
reverse_b = b[::-1]
print(reverse_b)

for i in range(len(a)):
    order1 = a[i]
    order2 = reverse_b[i]
    print(str(order1) +' '+ str(order2))
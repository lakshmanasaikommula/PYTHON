#list squares in asc order

list_a = input().split(",")
print(list_a)
list_x = []

for num in list_a:
    list_x += [int(num) ** 2]

list_x = sorted(list_x)
print(list_x)
#greater then n in a new list

list_a = [2,3,4,5,6,7,8,33,44,555,-11,33,-675,-2233,44,44,22]
n = int(input())

list_b = []

for i in list_a:
    if int(i)>n:
        list_b.append(i)
print(list_b)
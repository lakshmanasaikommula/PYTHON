# find second smallest

list1 = [4, 6, 3, 94, 9,4,4,3]

a = set(list1)
print(a)

list1.remove(min(a))
print(min(a))
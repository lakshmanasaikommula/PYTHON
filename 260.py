'''Finding second largest number in array without sorting'''

arr=[22,34,55,22,44,22]

a = set(arr)

a.remove(max(a))

print(max(a))


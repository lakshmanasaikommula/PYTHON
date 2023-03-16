n = int(input())
numbers = input()


list = numbers.split(" ")

for i in range(len(list)):
    list[i] = int(list[i])
count = int(n/-2)
print(list[count:])
def square(n):
    return n*n

num = [3,5,4,6,7,8]
result = map(square,num)
square_list = list(result)
print(square_list)

numbers = list(map(int, input().split()))
print(numbers)

def is_positive_number(num):
   return num > 0
list_a = [1, -2, 3, -4]
positive_nums = filter(is_positive_number, list_a)
print(list(positive_nums))


from functools import reduce
def sum_of_num(a, b):
   return a+b
list_a = [1, 2, 3, 4]
sum_of_list = reduce(sum_of_num, list_a)
print(sum_of_list)

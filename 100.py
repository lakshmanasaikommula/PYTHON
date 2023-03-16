import sys

my_list = [i for i in range(1000)]
print(sum(my_list))
print(sys.getsizeof(my_list), 'bytes')
print("---------------------")
my_tup = (i for i in range(2000))
print(sum(my_tup))
print(sys.getsizeof(my_tup), "bytes")
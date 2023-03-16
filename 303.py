from functools import reduce
#Here we talk about reduce
# we have to know reduce is a module so we need to import the module

def is_even(n):
    return n%2 ==0
nums =[2,3,4,1,5,6,3,4,7,8]
result = list(filter(is_even,nums))
print(result)
result1 = list(filter(lambda n:n%2==0, nums))
print(result1)

def sum_list_values(a,b):
    return a+b

result2 = list(map(lambda n:n*2, result1))
print(result2)

'''here we can use reduce to sum all the list of values
reduce also takes 2 arguments function logic and sequence'''

result3 = reduce(sum_list_values,result2)
print(result3)
sum = reduce(lambda a,b:a+b,result2)
print(sum)

z = [1,2,3,4,5,6]
y = reduce(lambda m,n:m+n,z)
print(y)



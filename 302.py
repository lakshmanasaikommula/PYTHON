from functools import reduce
reduce(lambda a,b: a+b,[23,21,45,98])

tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup))
print(newtuple)
# Here we discuss about the map
'''So below code filters the required values so now we are adding some maths to map the elements
map also takes function and iterable'''
def is_even(n):
    return n%2 ==0
nums =[2,3,4,1,5,6,3,4,7,8]
result = list(filter(is_even,nums))
print(result)
result1 = list(filter(lambda n:n%2==0, nums))
print(result1)

result2 = list(map(lambda n:n*2, result1))
print(result2)


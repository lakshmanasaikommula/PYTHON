# Here we can explain about the filter property
y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))
'''filter takes 2 arguments first one is function & second one is iterable '''
def is_even(n):
    return n%2 ==0
nums =[2,3,4,1,5,6,3,4,7,8]
result = list(filter(is_even,nums))
print(result)
result1 = list(filter(lambda n:n%2==0, nums))
print(result1)


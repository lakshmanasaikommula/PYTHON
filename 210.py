# maximum largest span

a = [1,9,6,3,1,5,4,9,2,5,1]
print('LIST = ',a)
print(max(a))
b = tuple(a)
print('TUPLE = ',b)
c = set(b)
print('SET = ',c)
d = dict.fromkeys(a,c)
print('DICT = ',d)

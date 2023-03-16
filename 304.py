#Here we talk about the enumerator

'''Sequence of index and items of values when looping over an object like list'''

a = ['ram','ram','sai', 'kiran', 'maran', 'aran', 'varun','hari','vari','mari','hari','mari','vari']

b = list(enumerate(a))
print(b)

for i,j in enumerate(a):
    print(i,j)

'''to seperate and store the duplicate index positions'''

charecter_map = {i:[] for i in set(a)}
print(charecter_map)
#use enumurate to the store the index of each occurance

for i, j in enumerate(a):
    charecter_map[j].append(i)

print(charecter_map)
with open('102.py','r') as e:
    var = e.read()

s = lambda x:x*x
print(s(3))
print(s(9))

l = [1,2,344,55,55,55,23,6]
k = filter(lambda x: x%2==0,l)
print(list(k))
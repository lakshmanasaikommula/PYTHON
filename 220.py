'''Given an string with dot(.) separated .print alternative words with ""xyz"" in between of them
Example:
Input: "i.will.learn.python.easily"
Output: "i.xyz.learn.xyz.easily.xyz"'''

n = 'i.will.learn.python.easily'
a = n.split('.')

xyz0 = []

for i in range(0, len(a), 2):
    xyz0.append((a[i]))

for i in range(1, len(a), 2):
    xyz = i * 'xyz.'

xyz1 = xyz.split('.')

print(xyz0)
print(xyz1)









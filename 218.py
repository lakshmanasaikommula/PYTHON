'''Reverse the alternative words in dot separated string without using inbuilt functions
Example:
Input=  i.like.this.programme.very.much
Output= i.ekil.this.emmargorp.very.hcum'''

n = 'i.ekil.this.emmargorp.very.hcum'
a = n.split('.')

reverse = []
for i in range(len(a)-1,-1,-2):
    reverse.append(a[i])
aa=[]
for j in reverse:
    final = (j[::-1])
    aa.append(final)

bb=[]
for j in range(0,len(a),2):
    bb.append(a[j])
print(bb)
aa1 = aa[::-1]
print(aa1)

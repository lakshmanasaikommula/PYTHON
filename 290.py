s="lakk221sh34m2n#$*"
l=""
count=0
d={}
for i  in s:
if i not in l and i.isalnum() :
  d[i]=s.count(i)
  l+=i
for x,z in d.items():
print(x,z)
for i in s:
if not(i.isalnum()):
  count+=1
print("Totals: ",count)
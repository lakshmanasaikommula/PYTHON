s="happy to do more challenges"
s1=""
s2=""
print(s[::-1])
print(30*"-")
for i in s:
s1=i+s1
print(s1)
print(30*"-")
print(s2.join(reversed(s)))
'''Implement a method to perform basic string compression using the counts of repeated characters.
E.g.; the string aabcccccaaa would become a2b1c5a3.
If “compressed” string is not smaller than the original string,
your method should return the original string. Assume string has only lowercase letters (a-z).
For “aabcccccaaa” input, your method will return “a2b1c5a3” but for “abcd” input,
your method will return “abcd”'''
import re

a = "aabcccccaaa"
len_a = len(a)
aa=[]
string=''
for i in a:
    if i not in string:
        aa.append((i,a.count(i)))
    string = string + i

bb=' '.join(map(str,aa))
bb = re.sub("[()]","",bb)
bb = bb.replace(' ','')
bb= bb.replace(',','')
bb = bb.replace("'","")
print(bb)
print(len(bb))
print(type(bb))




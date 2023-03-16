'''Write a function that takes input as string.The function should remove the alternate words in the string.Words are separated by dots".".(Avoid using inbuilt functions)
Example:
Input= i.like.this.programme.very.much
Output= ii.this.very
'''

n = 'i.like.this.programme.very.much'
a = n.split('.')

for i in range(0,len(a),2):
    result = '.'+a[i]
    print(result,end='')




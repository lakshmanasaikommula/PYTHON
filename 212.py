# devisible by 7 remainder would be 3

a = [7,17,5,45]
result=[]
for i in a:
    if i%7==3:
        result.append(i)
print(result)
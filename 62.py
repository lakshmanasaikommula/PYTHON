a = [float,int,'string',1,2,3,4,5,6,7]

for i in a:
    if type(i) == int and int(i)>2:
        print(i,end=' ')
print()
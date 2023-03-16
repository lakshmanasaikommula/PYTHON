import random
for i in range(100,1000):
   for i in range(100,1000):
    x=random.randint(100,1000)
    y=random.randint(100,1000)
    z=random.randint(100,1000)
    add=x+y+z
    x1=str(x)
    y1=str(y)
    z1=str(z)
    digit=x1[1]+y1[1]+z1[1]
    if add==int(digit):
     print(x,y,z)
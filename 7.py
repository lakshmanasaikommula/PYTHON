#printing pyramids

num = 10
n = (2*num)-2
for i in range(0,num):
    for j in range(0,n):
        print(end=" ")
    n = n-1
    for j in range(0,i+1):
        print('* ', end ="  ")
    print("  ")

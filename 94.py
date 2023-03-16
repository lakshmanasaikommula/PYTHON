def feb(n):
    a =0
    print(a,end=' ')
    b=1
    print(b,end=' ')
    for i in range(2,n):
        c=a+b
        a =b
        b=c
        print(c,end=' ')
feb(10)


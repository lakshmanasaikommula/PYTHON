#fibonacci series

def fibonacci(n1,n2):
    for i in range(2,10):
        sum = n1+n2
        print(sum)
        n1 = n2
        n2 = sum
fibonacci(0,1)


#prime or not

def number1(n):
    if n%2 ==0:
        print(n,' = ','its a EVEN number')
    else:
        print(n,' = ','its a ODD number')
res = [number1(i) for i in range(2,101)]
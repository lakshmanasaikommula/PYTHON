a =int(input())
b = int(input())

for i in range(a,b+1):
    length = len(str(i))
    temp=i
    result=0
    while temp>0:
        digit = temp%10
        result = result + (digit ** length)
        temp=temp//10
        if i ==result:
            print(i,' = ',"armstrong")
            break
        else:
            print(i,' =  ',"Not a armstong")
            break
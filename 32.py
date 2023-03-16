n = int(input())
for i in str(n):
    if int(n)==0:
        print(0)
        break
    elif int(n)%9==0:
        print(9)
        break
    else:
        print(n%9)
        break







'''n = int(input())
result =0
for i in str(n):
    result = result + int(i)
print(result)

print(999%9)'''







'''def digsum(n):
    if (n==0):
        return 0
    if (n%9 == 0):
        return 9
    else:
        return (n%9)
print(digsum(7546))
print(22//10)'''
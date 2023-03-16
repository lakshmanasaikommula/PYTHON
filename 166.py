N = int(input())


for i in range(0,N):
    print(' '*(N-i-1)+'/'+' '*(2*i)+'\\')
for i in range(0,N):
    print(' '*(i)+'\\'+' '*(2*(N-i-1))+'/')
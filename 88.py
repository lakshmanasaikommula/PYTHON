n = int(input())
n = str(n)
palindrome_number =''
for i in range(len(str(n))-1,0,-1):
    palindrome_number = (str(n[i]))
    print(palindrome_number,end='')
    print(str(n)==(palindrome_number,end=''))

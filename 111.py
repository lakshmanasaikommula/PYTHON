def palin(s):
    for i in range(1,int(len(s)//2)):
        if s[i] != s[len(s)-i-1]:
            return False
        return True

s = input().lower()

if palin(s):
    print(s,' = ', 'Is Palindrome')
else:
    print(s,' = ','Its not a palindrome')

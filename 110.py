def is_palindrome(s):
    length = len(s)
    if length<2:
        return True
    elif s[0] == s[length-1]:
        return is_palindrome(s[1:length-1])
    else:
        return False

s = input().lower()

result = is_palindrome(s)

if result:
    print(s,' = ', 'Its A Palindrome')
else:
    print(s,' = ','Its Not A Palindrome' )

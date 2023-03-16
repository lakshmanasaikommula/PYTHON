def is_palindrome(s):
    reverse = ''.join(reversed(s))
    if (s==reverse):
        return True
    else:
        return False

s = input().lower()

result = is_palindrome(s)
if result:
    print(s,' = ', 'Its A Palindrome')
else:
    print(s,' = ', "Not A Palindrome")
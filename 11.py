#palindrome or not a palindrome

def is_palindrome(num):
    data = (num[::-1])
    if data == num:
        return ("Its a Palindrome")

    else:
        return ("Its not a Palindrome")

print(is_palindrome("maalayalaam"))
'''Count the number of digits in a number
Example:
Input= 3245
Output= 4'''


def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# Driver Code
n = 345289467
print("Number of digits : % d" % (countDigit(n)))
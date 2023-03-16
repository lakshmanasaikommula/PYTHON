'''Given an array of integers, find the total number of numbers which are powers of  in that list (3**1=3, 3**2=,9)
Example:
Input= [3,5,27,15]
Output= [3,27]'''


def isPower_of_Three(n):
    if (n <= 0):
        return False
    if (n % 3 == 0):
        return isPower_of_Three(n // 3)
    if (n == 1):
        return True
    return False


# Driver code
num1 = 243
if (isPower_of_Three(num1)):
    print("Yes")
else:
    print("No")

num2 = 6
if (isPower_of_Three(num2)):
    print("Yes")
else:
    print("No")


# This code is contributed by shivanisinghss2110


# Python program to check if a number is power
# of 3 or not.

# Returns true if n is power of 3, else false
def check(n):
    """ The maximum power of 3 value that
    integer can hold is 1162261467 ( 3^19 ) ."""
    return 1162261467 % n == 0


# Driver code
n = 9
if (check(n)):
    print("Yes")
else:
    print("No")

# This code is contributed by Sachin Bisht
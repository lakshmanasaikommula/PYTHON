def sum_of_squares(m,n):
    total = 0
    for i in range(m,n+1):
        total = total + (i**2)
    return total

m = 2
n = 10

print(sum_of_squares(m,n))
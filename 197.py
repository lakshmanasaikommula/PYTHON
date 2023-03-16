def sum_digits(num):
    result = 0
    for i in num:
        result = result + int(i)
    return (result%9)

num = input()
print(sum_digits(num))
n = 10
n = int(n)

for numbers in range(2, n + 1):
    factors = 0
    for i in range(2, numbers):
        if numbers % i == 0:
            factors += 1

    if factors == 0:
        print(numbers)
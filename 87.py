n = int(input())
m = n
sum = 0
while m != 0:
    d = m % 10
    sum = sum * 10 + d
    m = m // 10

if sum == n:
    print("Palondrome Number")
else:
    print("Not a Palindrome Number")
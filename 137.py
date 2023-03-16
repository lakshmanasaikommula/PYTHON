n = 100

sum_even = 0
sum_odd = 0

for i in range(1,n+1):
    if n%i ==0:
        sum_even += i
    else:
        sum_odd +=i
    print("sum_even= ",sum_even)
    print("sum_odd= ",sum_odd)
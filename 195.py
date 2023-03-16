def digits(s):
    nums=[]
    for i in s:
        if i.isdigit():
            nums.append(int(i))
    return nums
s = "l1j3h36ms8sn"

print(digits(s))
print(sum(digits(s)))
print(min(digits(s)))
print(max(digits(s)))











'''def get_digits(str_1):
    digits_list = []
    for char in str_1:
        if char.isdigit():
            digits_list += [int(char)]
    return digits_list'''


'''str_1 = input()
digits = get_digits(str_1)
sum_of_digits = sum(digits)
print(sum_of_digits)
min_of_digits = min(digits)
print(min_of_digits)
max_of_digits = max(digits)
print(max_of_digits)'''
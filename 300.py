def positive_numbers(num):
    return num>0
list_a = [1,-2,3,4]

positive_nums = filter(positive_numbers,list_a)
print(list(positive_numbers))
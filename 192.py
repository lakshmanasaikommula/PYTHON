n = input()
nums_list = n.split(",")

lengh_of_nums_list = len(nums_list)
for i in range(lengh_of_nums_list):
    nums_list[i] = int(nums_list[i])

nums_list = sorted(nums_list)
largest_number = nums_list[-1]
print(largest_number)
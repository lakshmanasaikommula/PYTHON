n = input()
k = int(input())
nums_list = n.split(",")

lengh_of_nums_list = len(nums_list)
for i in range(lengh_of_nums_list):
    nums_list[i] = int(nums_list[i])

nums_list = sorted(nums_list)
kth_largest_number = nums_list[-k]
print(kth_largest_number)
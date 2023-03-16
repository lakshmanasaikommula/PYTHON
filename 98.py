from collections import Counter

my_list = [1,2,3,4,5,3,3,3,3,3,2,3,45,5,5,5,5,5,5,5,5,5,5,7,8,9,9,9]

counter = Counter(my_list)


most_common = counter.most_common(1)
print(most_common)
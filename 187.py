def get_list(a):
    numbers_list = []
    len_a = len(a)
    for i in range(len_a):
        numbers_list.append(int(a[i])**2)
    return numbers_list

a = input().split(',')
print(get_list(a))



'''def get_list(string_a):
    list_a = string_a.split(',')
    len_list_a = len(list_a)
    for i in range(len_list_a):
        list_a[i] = int(list_a[i])**2
    return list_a


string_a = input()
numbers_list = get_list(string_a)
print(numbers_list)'''
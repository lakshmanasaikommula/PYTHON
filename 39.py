my_list = [-23,-34,0,2,3,1,4,7,8]
my_list = sorted(my_list)
print(my_list)
new_list = []

while my_list:
    min = my_list[0]
    for x in my_list:
        if x<min:
            min = x
    new_list.append(min)
    my_list.remove(min)
print(new_list)


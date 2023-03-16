list_x = list(input())
dict_a = {
'A' : 1,
'B' : 2,
'C' : 3
}
sum = 0;
l = len(list_x);
list_z = [];
list_y = [];
for i in range(l):
    if i+1<l:
        if list_x[i]==list_x[i+1]:
            list_z.append(list_x[i])
        else:
            list_y.append(list_x[i])
    elif i+1==l:
        list_y.append(list_x[i])



print(list_y)
print(list_z)
for item in list_y:
    if item in dict_a.keys():
        sum+=dict_a[item];
print(sum);
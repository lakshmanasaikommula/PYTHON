string = "lakshmana"
for i in string:
    print(i, ' is a alphabet')
print('-------------------------')

list1 = ['sai',22,'suri',34,'mari',55]
for i in list1:
    if type(i) == str:
        print(i, ' is an item')
print("-------------------------")

tuple1 = ('ahajya',1,'amajya',1,'kalyan',3)
for i in tuple1:
    if type(i) == int:
        print(i, ' is also an num')
print('-------------------------------')

dict1 = {
    'shahera': 1,
    'divya': 2,
    'ahajya': 3,
    'kalyan': 4
}
for key in dict1.keys():
    print(key, ' is a key')
print("-----------------------")
for value in dict1.values():
    print(value, ' is a value')
print('------------------------')
for key,value in dict1.items():
    print(key, ' is a key and  ' + str(value), ' is a value')
print("-------------------------")


set1 = {'aha',2,'prime',3,'netflix',4}
for i in set1:
    print(i)
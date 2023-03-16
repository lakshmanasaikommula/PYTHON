numbers = []
letters = []

list1 = ['ahajya',1234,'amajya','shahera',653626,'divya','kalyan',8277262,928727]

for i in list1:
    if type(i) == str:
        letters.append(i)
    elif type(i) == int:
        numbers.append(i)

print("list of strings: ",letters)
print("list of numbers: ",numbers)

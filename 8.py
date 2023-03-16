#leap year
# it occurs in every four years
#in which feb has 29 days
# 2000 is a leap year and ofter 2000
#2004
#2008
#2012
#2016
#2020

y = int(input('Enter a Year: '))
print(364%4)
if y%400 ==0:
    print("Leap Year")
elif y%4 ==0:
    print("Leap Year")
elif y%100==0:
    print("Its Not a Leap year")
else:
    print("Its not a Leap Year")








n = 'iam.ccbp.trainee'

a = n.split('.')
reverse=''
for i in a:
    reverse =  i +'.'+ reverse
print(reverse[0:-1])
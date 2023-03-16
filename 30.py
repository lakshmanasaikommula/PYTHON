# function to check string is
# palindrome or not
'''n = input().lower()
for i in range(0,int(len(n)/2)):
    if n[i] != n[len(n)-i-1]:
        print(False)
        break
print(True)

if n ==True:
    print("p")
else:
    print("n")'''

def isPalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
s = "maaalaayatyaalaaam"
if isPalindrome(s):
    print("Yes")
else:
    print("No")
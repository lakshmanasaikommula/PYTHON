n = input().lower()

l = len(n)

for i in range(0,int((len(n)/2))):
    if n[i] != n[len(n)-i-1] and n[i]!=' ':
        print("Not a Palindrome")
        break
else:
    print("Its a Palindrome")


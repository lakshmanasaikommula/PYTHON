def palin(s):
    s = s.lower()
    length = len(s)
    if length<2:
        return True
    elif s[0] == s[length-1]:
        return palin(s[1:(length-1)])
    else:
        return False
s = input()

result = palin(s)

if result:
    print("Its palin")
else:
    print("not")
# zeros first



s = '010101101001011'

zeros = []
others = []
for i in s:
    if i == '0':
        zeros.append(i)
    else:
        others.append(i)

print(''.join(zeros + others))
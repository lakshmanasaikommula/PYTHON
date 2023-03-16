name = 'LAKSHMAN '
result =''
for char in name:
    asci=ord(char)
    new = asci+1
    result = result+chr(new)
print(result)
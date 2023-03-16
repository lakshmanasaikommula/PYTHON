def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
         print(counts)
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
         return c
   return None

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCC'))
#The input will be a single line containing a string s.
inputString=input()
vowels=0
consonants=0
inputString=inputString.lower()
for l in inputString:
 #check if the letter of the string is vowel
    if(l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' ):
        vowels+=1
    else:
 #check if the letter of the string is consonant
        if l != ' ' and l.isdigit()==False:
            consonants+=1
#The first line of output should contain no of Vowels in the given string
print(str(vowels))
#The second line of output should contain no of Consonants in the given string
print(str(consonants))
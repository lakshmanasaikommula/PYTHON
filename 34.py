def reverseSentence(s):
    words = s.split(' ')
    reverse_s = ''.join(reversed(words))
    return reverse_s

if __name__ == "__main__":
    sentence = input()
    print(reverseSentence(sentence))
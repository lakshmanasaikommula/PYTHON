'''Print the largest consecutive 1 in given string
Example:
Input = 0000110111
Output= 3'''



def maxConsecutive1(input):
    return max(map(len,input.split('0')))

if __name__ == "__main__":
	input = '000010111'
	print(maxConsecutive1(input))
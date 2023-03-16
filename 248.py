'''Write a function that takes an array of integers as input and prints the second-maximum difference between any two elements from an array.
Example:
int arr[]={14, 12, 70, 15, 95, 65, 22, 30};
First max-difference = 95-12=83
Second max-difference = 95 -14 = 81
So output should be 81'''

arr=[14,12,70,15,95,65,22,30]
arr.sort()
print(arr)
print('First max-difference', arr[-1]-arr[0])
print('Second max-difference', arr[-1]-arr[1])

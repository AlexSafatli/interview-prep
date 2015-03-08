# Implementation of the binary search algorithm.

def binarySearch(arr,key):
	# Assumes the array is already sorted.
	lower = 0
	upper = len(arr)-1
	middle = (lower+upper)/2
	while (arr[middle] != key and lower <= upper):
		if (key < arr[middle]):   upper = middle-1
		elif (key > arr[middle]): lower = middle+1
		middle = (lower+upper)/2
	if (lower <= upper): # key was found
		return middle
	else: return -1 # was not found

if __name__ == '__main__':
	arr = [0,1,2,3,4,5,6,7,8,21,25,28]
	print arr[binarySearch(arr,25)] # should print 25
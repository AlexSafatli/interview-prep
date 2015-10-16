# Mergesort implementation of the classical recursive sorting algorithm. O(nlgn)

def mergesort(arr):

	# If a single element, array already sorted.
	if (len(arr) > 1):
		middle = (len(arr))//2
		left = arr[:middle]
		right = arr[middle:]
		mergesort(left) # First half.
		mergesort(right) # Second half.
		merge(arr,left,right) # Merge them.

def merge(arr,left,right):

	# Set up arrays, populate them.
	lenLeft  = len(left)
	lenRight = len(right)

	# Sort.
	i,j,k = 0,0,0
	while (i < lenLeft and j < lenRight):
		if (left[i] <= right[j]):
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while (i < lenLeft):
		arr[k] = left[i]
		i += 1
		k += 1
	while (j < lenRight):
		arr[k] = right[j]
		j += 1
		k += 1

if __name__ == '__main__':
	array = [0,2,4,1,7,9,2,3]
	mergesort(array)
	print array
	




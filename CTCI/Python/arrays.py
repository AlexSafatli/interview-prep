from random import sample

def removeDuplicateCharacters(string):
	bitvector = 0 # No tracked characters.
	chars = list(string)
	pos = 0
	length = len(string)
	while (pos < length):
		# Get character at this position.
		char = ord(chars[pos]) - ord('a')
		# See if that character has been seen before.
		if (bitvector & (1 << char)):
			# Has been seen before. Duplicate.
			chars[pos] = '' # Clear this character entry.
		else: bitvector |= (1 << char) # Track it.
		pos += 1
	return ''.join(chars)

def areAnagrams(string1,string2):
	charsCaught = dict()
	for char in string1:
		if char in charsCaught:
			charsCaught[char] += 1
		else: charsCaught[char] = 1
	for char in string2:
		if not char in charsCaught or charsCaught[char] == 0:
			return False
		else: charsCaught[char] -= 1
	for val in charsCaught.values():
		if val != 0: return False
	return True	

def transposeSquareMatrixInplace(mat):
	if len(mat) < 1:
		raise Exception("Empty matrix.")
	elif len(mat[0]) < 1:
		raise Exception("Empty row in matrix.")
	N = len(mat[0])
	# Only consider upper triangle.
	for n in xrange(0,N-1):
		for m in xrange(n+1,N):
			# Swap the elements at [m][n] and [n][m].
			temp = mat[m][n]
			mat[m][n] = mat[n][m]
			mat[n][m] = temp

# Rotating matrices.
# - Rotate by +90: transpose, reverse rows.
# - Rotate by -90: transpose, reverse columns.

if __name__ == '__main__':
	# If not imported.
	testString = 'carradio'
	testOutput = 'cardio'
	print 'Test String: %s' % (testString)
	print 'Should Be: %s' % (testOutput)
	removed = removeDuplicateCharacters(testString)
	print 'Is Actually: %s' % (removed)
	print 'Passed: %s' % (str(removed == testOutput))
	print '-' * 30
	testStringB = ''.join(sample(list(testString),len(testString)))
	print 'Test String A: %s' % (testString)
	print 'Test String B: %s' % (testStringB)
	print 'Anagrams: %s' % (str(areAnagrams(testString,testStringB)))
	print 'Test String A: %s' % (testString)
	print 'Test String B: door'
	print 'Anagrams: %s' % (str(areAnagrams(testString,'door')))
	mat = [[0,1,2],[5,4,3],[9,2,1]]
	print 'Matrix: %s' % (str(mat))
	transposeSquareMatrixInplace(mat)
	print 'Transposed: %s' % (str(mat))
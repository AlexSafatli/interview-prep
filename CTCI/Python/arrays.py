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
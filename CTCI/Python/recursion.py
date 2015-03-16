# 8.2 Number of Robot Paths: C(N-1,2N-2) for an NxN grid.
# 8.2.2 (pg 170) *

# 8.3 All subsets of a set.

def allSubsetsOfASet(S,index):
	# For n>1, find the set of subsets of 1,...,n-1 and make two copies of it. 
	# For one of them, add n to each subset. Then take the union of the two copies.
	if (index == len(S)):
		return [[]]
	else:
		allSubsets = allSubsetsOfASet(S,index+1)
		current = S[index] # to have be identical to bin function, make this S[len(S)-index-1]
		subsets = list()
		for subset in allSubsets:
			new = list()
			new.extend(subset)
			new.append(current)
			subsets.append(new)
		allSubsets.extend(subsets)
		return allSubsets

def allSubsetsOfASetBin(S):
	# Assume S is a list.
	allSubsets = list()
	maxInt = (1 << len(S)) # 2^N where N is size of S
	i = 0 # generate all binary numbers starting with 0
	while (i < maxInt):
		k = i
		index = 0
		subset = []
		while (k > 0):
			if ((k & 1) > 0): subset.append(S[index])
			k >>= 1
			index += 1
		allSubsets.append(subset)
		i += 1
	return allSubsets

def test_allSubsets():
	s = [0,3,2,5,8]
	print allSubsetsOfASetBin(s)
	print allSubsetsOfASet(s,0)

# 8.4 All permutations of a sequence -- see Algorithms notes (1, p. 17).

def allPermutations(prefix,S):
	allPerms = list()
	if len(S) == 1: # Base Case
		allPerms.append(prefix+S)
	else:
		for ele in S:
			s = list()
			s.extend(S)
			s.remove(ele)
			allPerms.extend(allPermutations(prefix+[ele],s))
	return allPerms

def test_allPermutations():
	s = 'Dark'
	print allPermutations([],s)

if __name__ == '__main__':
	test_allSubsets()
	test_allPermutations()
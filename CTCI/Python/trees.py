# Review: http://en.wikipedia.org/wiki/Binary_search_tree --> Insertion ***

# (Binary) Tree Traversals: (1) In-Order, (2) Pre-Order, (3) Post-Order
# Graph Traversals: (1) Depth First Search, (2) Breadth First Search
# Check if tree is balanced: (maxDepth - minDepth <= 1)

from linked_lists import linkedList

class node(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def getData(self): return self.data
	def getLeft(self): return self.left
	def getRight(self): return self.right
	def setData(self,d):  self.data = d
	def setLeft(self,n):  self.left = n
	def setRight(self,n): self.right = n

class binarySearchTree(object):
	def __init__(self):
		self.root = None
	def getRoot(self): return self.root
	def setRoot(self,n):
		self.root = n
	@staticmethod
	def _insert(nodePtr,i):
		next = None
		if (nodePtr == None):
			raise AssertionError("Need non-None pointer.")
		elif (i > nodePtr.getData()):
			# Insert right.
			if (nodePtr.getRight() == None):
				# Found empty spot.
				nodePtr.setRight(node(i))
			else: next = nodePtr.getRight()
		else:
			if (nodePtr.getLeft() == None):
				# Found empty spot.
				nodePtr.setLeft(node(i))
			else: next = nodePtr.getLeft()
		if (next != None):
			binarySearchTree._insert(next,i)
	def insert(self,i):
		if (self.root == None):
			self.root = node(i)
		else: binarySearchTree._insert(self.root,i)

# 4.3, Minimal Height BST

def getMidPtOfArrayAsNode(arr,start,end):
	if (end < start): return None
	mid = (end+start)/2
	cur = node(arr[mid])
	cur.setLeft(getMidPtOfArrayAsNode(arr,start,mid-1))
	cur.setRight(getMidPtOfArrayAsNode(arr,mid+1,end))
	return cur

# 4.4, Linked List a la Level Order Traversal

def getLevelOrderOfTree(tr):
	level = 0
	levelList = list()
	#TODO

if __name__ == '__main__':
	b = binarySearchTree()
	b.setRoot(getMidPtOfArrayAsNode(range(2,7),0,5-1))
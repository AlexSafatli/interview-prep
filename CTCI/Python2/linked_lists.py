class node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
	def getData(self): return self.data
	def setData(self,d): self.data = d
	def getNext(self): return self.next
	def setNext(self,n): self.next = n

class linkedList(object):
	head = None
	size = 0
	def __str__(self):
		string = ''
		cursor = self.head
		if cursor != None:
			while (cursor.getNext() != None):
				string += str(cursor.getData()) + ' -> '
				cursor = cursor.getNext()
			string += str(cursor.getData())
		return string
	def __len__(self): return self.size
	def getHead(self): return self.head
	def setHead(self,h): self.head = h
	def getTail(self):
		if (self.head == None): return None
		cursor = self.head
		while (cursor.getNext() != None):
			cursor = cursor.getNext()
		return cursor
	def appendToTail(self,data):
		n = node(data)
		self.appendNodeToTail(n)
		return n
	def appendToHead(self,data):
		n = node(data)
		self.appendNodeToHead(n)
	def appendNodeToTail(self,n):
		# Check to see if head exists.
		if (self.head == None):
			# Nothing in list. Make this the head.
			self.head = n
		else:
			cursor = self.getTail()
			cursor.setNext(n)
		self.size += 1
	def appendNodeToHead(self,n):
		# Check to see if head exists.
		if (self.head != None):
			cursor = self.head
			n.setNext(cursor)
		self.head = n
		self.size += 1
	def deleteNode(self,n):
		# @REP DeleteNode on InterviewCake
		cursor = self.head
		if cursor != None:
			if cursor == n:
				self.head = cursor.getNext()
				self.size -= 1
				return
			while (cursor.getNext() != None):
				if (cursor.getNext() == n):
					cursor.setNext(cursor.getNext().getNext())
					self.size -= 1
					return
				cursor = cursor.getNext()
		raise Exception('Node not found in list.')
	def removeDuplicates(self):
		cursor = self.head
		prev = None
		if cursor == None: return
		dups = dict()
		while (cursor != None):
			if (cursor.getData() in dups):
				# Delete the current node (duplicate).
				# Should never happen if prev is None.
				prev.setNext(cursor.getNext())
				self.size -= 1
			else:
				dups[cursor.getData()] = True
				prev = cursor
			cursor = cursor.getNext()

class adder(object):
	def __init__(self,numA,numB):
		self.numA = numA
		self.numB = numB
		self.listA = linkedList()
		self.listB = linkedList()
		for digit in reversed(str(self.numA)):
			self.listA.appendToTail(digit)
		for digit in reversed(str(self.numB)):
			self.listB.appendToTail(digit)

	@staticmethod
	def _add(a,b,carry):

		''' Add values and keep track of carry. '''

		if (a == None and b == None): return None
		
		# Make new node.
		result = node(carry)
		ans = carry

		# Check either nodes.
		if (a != None): ans += int(a.getData())
		if (b != None): ans += int(b.getData())
		result.setData(ans%10)

		# Recurse.
		next = adder._add(a.getNext() if a != None else None,
			b.getNext() if b != None else None,ans/10)
		result.setNext(next)
		return result

	def add(self):

		''' Add the two numbers together. Return a linked list. '''

		ans   = linkedList()
		ptrA  = self.listA.getHead()
		ptrB  = self.listB.getHead()

		# Is one of the lists empty?
		if (ptrA == None):   return self.listB
		elif (ptrB == None): return self.listA

		# Perform the addition, set head.
		ans.setHead(adder._add(ptrA,ptrB,0))

		return ans


# NOT IMPLEMENTED
# ---------------
# 2.2, keep two pointers n distance apart and increment them together.
# 2.3, delete a node in place (copy data of next node into current node, delete that one).
# 2.4, think of an adder. ***
# 2.5, two pointers moving at different speeds.

if __name__ == '__main__':
	l = linkedList()
	l.appendToTail('door')
	n = l.appendToTail('car')
	l.appendToTail('boo')
	l.appendToTail('vee')
	l.deleteNode(n)
	l.appendToTail('boo')
	l.appendToTail('boo')
	l.removeDuplicates()
	print '='*30 + '\n' + str(l) + '\n' + '='*30
	a = adder(120,29)
	print str(a.add()) + '\n' + '='*30

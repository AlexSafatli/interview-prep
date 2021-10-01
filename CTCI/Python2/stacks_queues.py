from linked_lists import linkedList, node

class stack(object):
	def __init__(self):
		self.container = linkedList()
	def pop(self):
		# Is empty?
		if (not self.isEmpty()):
			top = self.container.getHead()
			data = top.getData()
			self.container.deleteNode(top)
			return data
		return None
	def push(self,data):
		add = node(data)
		add.setNext(self.container.getHead())
		self.container.appendNodeToHead(add)
	def peek(self):
		return self.container.getHead().getData()
	def isEmpty(self):
		return (len(self.container) == 0)
	def __str__(self): return str(self.container)

# 3.1, Divide the array into 3 parts of equal size. Stack grows in those (limited) spaces.
#  [0,n/3)
#  [n/3,2n/3)
#  [2n/3,n)
# Assumes: no knowledge of space usage. Cannot use any extra space (resizable array?).
# 3.2, Have nodes keep track of min, or Stack class keep track on addition/deletion (problem here is on deletion).
# 3.3, Rollover, see solution. *
# 3.4, Towers of Hanoi (see separate file).

class queue(object):
	def __init__(self):
		self.container = linkedList()
	def enqueue(self,data):
		self.container.appendToTail(data)
	def dequeue(self):
		head = self.container.getHead()
		self.container.deleteNode(head)
		return head.getData()
	def __str__(self): return str(self.container)

if __name__ == '__main__':
	s = stack()
	s.push('Door')
	s.push('Car')
	print s.pop()
	print s
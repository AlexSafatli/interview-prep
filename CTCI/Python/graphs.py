from stacks_queues import stack

class graph(object):
	def __init__(self):
		self.adj = dict()
		self.next = 0
		self.size = 0
	def getNeighbors(self,i):
		if (not i in self.adj):
			raise IndexError("No vertex %d in graph." % (i))
		return self.adj[i]
	def getEdgesFor(self,i):
		if (not i in self.adj):
			raise IndexError("No vertex %d in graph." % (i))
		return [(i,j) for j in self.adj[i]]
	def addEdge(self,i,j):
		if (not i in self.adj):
			raise IndexError("No vertex %d in graph." % (i))
		elif (not j in self.adj):
			raise IndexError("No vertex %d in graph." % (j))
		self.adj[i].append(j)
	def removeEdge(self,i,j):
		if (not i in self.adj):
			raise IndexError("No vertex %d in graph." % (i))
		elif (not j in self.adj):
			raise IndexError("No vertex %d in graph." % (j))
		if (j in self.adj[i]): self.adj[i].remove(j)
		if (i in self.adj[j]): self.adj[j].remove(i)
	def newVertex(self):
		self.adj[self.next] = list()
		self.size += 1
		self.next += 1
		return self.next
	def removeVertex(self,i):
		if (not i in self.adj):
			raise IndexError("No vertex %d in graph." % (i))
		self.size -= 1
		for edge in self.getEdgesFor(i):
			a,b = edge
			self.removeEdge(a,b)
		del self.adj[i]
	def hasPath(self,i,j):
		toSearch = stack()
		searched = list()
		toSearch.push(i)
		while (not toSearch.isEmpty()):
			cur = toSearch.pop()
			for ne in self.getNeighbors(cur):
				if (ne == j): return True
				elif (not ne in searched):
					toSearch.push(ne)
			searched.append(cur)
		return False

if __name__ == '__main__':
	g = graph()
	g.newVertex()
	g.newVertex()
	g.newVertex()
	g.newVertex()
	g.newVertex()
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(0,2)
	g.addEdge(3,2)
	g.addEdge(2,4)
	print g.hasPath(0,4)
	print g.hasPath(0,3)
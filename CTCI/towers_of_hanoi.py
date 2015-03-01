from stacks_queues import stack

class HanoiTower(object):
	label = None
	disks = None
	def __init__(self,label):
		self.label = label
		self.disks = stack()
	def getLabel(self):
		return self.label
	def addDisk(self,num):
		if (not self.disks.isEmpty() and self.disks.peek() <= num):
			raise AsseritionError("Disk must be placed on larger disk.")
		self.disks.push(num)
	def removeTopDisk(self):
		return (self.disks.pop())
	def moveTopDiskTo(self,dest):
		disk = self.removeTopDisk()
		dest.addDisk(disk)
		print 'Moved %d from %d to %d.' % (disk,self.label,dest.label)
	def moveDisksTo(self,N,dest,interm):
		if (N > 0):
			self.moveDisksTo(N-1,interm,dest)
			self.moveTopDiskTo(dest)
			interm.moveDisksTo(N-1,dest,self)
	def __str__(self): return str(self.disks)

if __name__ == '__main__':
	# Test the problem.
	N = 5
	towers = list()
	for x in xrange(0,3): towers.append(HanoiTower(x))
	for x in xrange(N-1,-1,-1): towers[0].addDisk(x)
	towers[0].moveDisksTo(N,towers[2],towers[1])

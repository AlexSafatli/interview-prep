COLUMN=0
ROW=1
DIAG=2
RDIAG=3

# 19.2 (pg. 266)
class ticTacToeBoard(object):
	def __init__(self):
		self.state = [[None,None,None],[None,None,None],[None,None,None]]
	def set(self,i,j,symb):
		self.state[i][j] = symb
	def get(self,i,j):
		if (i < 0 or i >= 3): return None
		elif (j < 0 or j >= 3): return None
		return self.state[i][j]
	def __getitem__(self,i):
		return self.state[i]
	def checkSets(self,dir=None):
		if (dir == COLUMN):
			for i in xrange(0,3):
				piece = self.state[0][i]
				if (piece == None): return False
				if (all([piece == self.state[x][i] for x in xrange(1,3)])):
					return True
			return False
		elif (dir == ROW):
			for i in xrange(0,3):
				piece = self.state[i][0]
				if (piece == None): return False
				if (all([piece == self.state[i][x] for x in xrange(1,3)])):
					return True
			return False
		elif (dir == DIAG):
			piece = self.state[0][0]
			if (piece == None): return False
			for i in xrange(1,3):
				if self.state[i][i] != piece:
					return False
			return True
		elif (dir == RDIAG):
			piece = self.state[0][2]
			if (piece == None): return False
			for i in xrange(1,3):
				if self.state[i][2-i] != piece:
					return False
			return True
	def isWon(self):
		# Determine if there is a won game state.
		for dir in [COLUMN,ROW,DIAG,RDIAG]:
			if (self.checkSets(dir)):
				return True
		return False
	def __str__(self):
		return '\n'.join([str(row) for row in self.state])

if __name__ == "__main__":
	board = ticTacToeBoard()
	board.set(0,0,'x')
	board.set(1,1,'x')
	board.set(2,2,'o')
	board.set(0,1,'o')
	board.set(0,2,'o')
	board.set(2,1,'x')
	print board
	print 'isWon:',board.isWon()
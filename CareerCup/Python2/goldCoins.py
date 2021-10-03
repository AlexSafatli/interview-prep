# http://www.dsalgo.com/2013/02/gold-coins-in-pots-game.html

def numberOfCoins(pots):
	outcomes = [[None for x in xrange(0,len(pots))] for y in xrange(0,len(pots))]
	return maxCoins(pots,0,len(pots)-1,outcomes)

def maxCoins(pots,lo,up,f):
	if (lo > up): return 0
	if (f[lo][up] != None): return f[lo][up]
	F = lambda i,j: maxCoins(pots,i,j,f)
	start = pots[lo] + min([F(lo+2,up),F(lo+1,up-1)])
	end = pots[up] + min([F(lo,up-2),F(lo+1,up-1)])
	f[lo][up] = max([start,end])
	return f[lo][up]

if __name__ == '__main__':
	goldPots = [12,32,4,23,6,42,16,3,85,23,4,7,3,5,45,34,2,1]
	print numberOfCoins(goldPots)
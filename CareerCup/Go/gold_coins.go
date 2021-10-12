// http://www.dsalgo.com/2013/02/gold-coins-in-pots-game.html
package main
import "fmt"

func min(a int, b int) int {
	if (a < b) { 
		return a
	}
	return b
}

func max(a int, b int) int {
	if (a > b) {
		return a
	}
	return b
}

func numberOfCoins(pots *[18]int) int {
	var outcomes [18][18]int
	for i := range outcomes {
		for j := range outcomes[i] {
			outcomes[i][j] = -1
		}
	}
	return maxCoins(pots,0,17,&outcomes)
}

func maxCoins(pots *[18]int, lo int, up int, f *[18][18]int) int {
	if (lo > up) {
		return 0
	}
	if (f[lo][up] >= 0) {
		return f[lo][up]
	}
	F := func(i int, j int) int { return maxCoins(pots,i,j,f) }
	start := pots[lo] + min(F(lo+2,up),F(lo+1,up-1))
	end := pots[up] + min(F(lo,up-2),F(lo+1,up-1))
	f[lo][up] = max(start,end)
	return f[lo][up]
}

func main() {
	goldPots := [...]int{12,32,4,23,6,42,16,3,85,23,4,7,3,5,45,34,2,1}
	fmt.Println(numberOfCoins(&goldPots))
}
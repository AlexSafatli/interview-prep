package main

import (
	"fmt"
)

const inf = int(^uint(0)>>1) - 1

func coinChange(coins []int, amount int) int {
	var dp []int
	dp = make([]int, amount+1)
	dp[0] = 0
	for i := 1; i <= amount; i++ {
		dp[i] = inf
		for _, j := range coins {
			if i >= j {
				dp[i] = min(dp[i-j]+1, dp[i])
			}
		}
	}
	if dp[amount] != inf {
		return dp[amount]
	}
	return -1
}

/* Main (Test) */
func main() {
	coins1 := []int{1, 2, 5}
	coins2 := []int{2}
	coins3 := []int{1}
	fmt.Println(coinChange(coins1, 11) == 3)
	fmt.Println(coinChange(coins2, 3) == -1)
	fmt.Println(coinChange(coins3, 0) == 0)
}

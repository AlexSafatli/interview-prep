package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func maxProduct(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	maxP, minP, ans := nums[0], nums[0], nums[0]
	for i := 1; i < n; i++ {
		if nums[i] < 0 {
			maxP, minP = minP, maxP
		}
		maxP = max(nums[i], maxP*nums[i])
		minP = min(nums[i], minP*nums[i])
		ans = max(ans, maxP)
	}
	return ans
}

/* Test */
func printMaxProductAns(nums []int, exp int) {
	for _, f := range []func([]int) int{maxProduct} {
		start := time.Now()
		ans := f(nums)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printMaxProductAns([]int{2, 3, -2, 4}, 6)
	printMaxProductAns([]int{-2, 0, -1}, 0)
	printMaxProductAns([]int{-2, 0, -1, 7, 2, -5, -7}, 490)
	printMaxProductAns([]int{1}, 1)
	printMaxProductAns([]int{}, 0)
}

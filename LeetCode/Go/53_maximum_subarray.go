package main

import (
	"fmt"
	"math"
	"reflect"
	"runtime"
	"time"
)

// Kadane's algorithm (https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)
func maxSubArray(nums []int) int {
	bestSum := -math.MaxInt
	currSum := 0
	for _, n := range nums {
		currSum = max(n, currSum+n)
		bestSum = max(bestSum, currSum)
	}
	return bestSum
}

/* Test */
func printMaxSubArrayAns(nums []int, exp int) {
	for _, f := range []func([]int) int{maxSubArray} {
		start := time.Now()
		ans := f(nums)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printMaxSubArrayAns([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6)
	printMaxSubArrayAns([]int{1}, 1)
	printMaxSubArrayAns([]int{5, 4, -1, 7, 8}, 23)
}

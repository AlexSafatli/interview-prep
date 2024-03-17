package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func removeDuplicates(nums []int) int {
	var i, j int // two pointers to track duplicates and leave rest of array
	n := len(nums)
	for j = 1; j < n; j++ {
		if nums[j] != nums[i] {
			i++
			nums[i] = nums[j]
		}
	}

	return i + 1
}

/* Test */
func printRemoveDuplicatesAns(nums []int, exp int) {
	for _, f := range []func([]int) int{removeDuplicates} {
		start := time.Now()
		ans := f(nums)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printRemoveDuplicatesAns([]int{1, 1, 2}, 2)
	printRemoveDuplicatesAns([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 5)
}

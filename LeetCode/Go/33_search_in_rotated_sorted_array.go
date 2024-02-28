package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

// Binary search, most intuitive solution
func search(nums []int, target int) int {
	var l, r, mid int
	r = len(nums) - 1
	for l <= r {
		mid = (l + r) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target < nums[mid] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[r] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		}
	}
	return -1
}

/* Test */
func printSearchAns(nums []int, target, exp int) {
	for _, f := range []func([]int, int) int{search} {
		start := time.Now()
		ans := f(nums, target)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printSearchAns([]int{4, 5, 6, 7, 0, 1, 2}, 0, 4)
	printSearchAns([]int{4, 5, 6, 7, 0, 1, 2}, 3, -1)
	printSearchAns([]int{1}, 0, -1)
}

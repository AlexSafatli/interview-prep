package main

import (
	"fmt"
	"math"
	"reflect"
	"runtime"
	"time"
)

// Binary search, most intuitive solution
func findMin(nums []int) int {
	var l, r, mid uint
	r = uint(len(nums)) - 1
	for l < r {
		mid = (l + r) / 2
		if nums[mid] > nums[r] {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return nums[l]
}

// Using min pointer, recursion
func findMinRec(nums []int, l, r int, min *int) {
	if l < 0 || r < 0 || r > len(nums)-1 {
		return
	}
	if l == r {
		if nums[l] < *min {
			*min = nums[l]
		}
		return
	}
	mid := l + (r-l)/2
	if nums[l] <= nums[mid] {
		// left is sorted
		if nums[l] < *min {
			*min = nums[l]
		}
		l = mid + 1
	} else {
		// right is sorted
		if nums[mid] < *min {
			*min = nums[mid]
		}
		r = mid - 1
	}
	findMinRec(nums, l, r, min)
}

func findMinPtr(nums []int) int {
	min := math.MaxInt
	findMinRec(nums, 0, len(nums)-1, &min)
	return min
}

// Using min pointer, recursion - however, array could contain duplicates (154)
func findMinRecDup(nums []int, l, r int, min *int) {
	if l < 0 || r < 0 || r > len(nums)-1 {
		return
	}
	if l == r {
		if nums[l] < *min {
			*min = nums[l]
		}
		return
	}
	mid := l + (r-l)/2
	if nums[l] <= nums[mid] && nums[mid] <= nums[r] {
		if nums[l] < *min {
			*min = nums[l]
		}
		l++
	} else if nums[l] <= nums[mid] {
		// left is sorted
		if nums[l] < *min {
			*min = nums[l]
		}
		l = mid + 1
	} else {
		// right is sorted
		if nums[mid] < *min {
			*min = nums[mid]
		}
		r = mid - 1
	}
	findMinRecDup(nums, l, r, min)
}

func findMinPtrDup(nums []int) int {
	min := math.MaxInt
	findMinRecDup(nums, 0, len(nums)-1, &min)
	return min
}

/* Test */
func printFindMinAns(nums []int, exp int) {
	for _, f := range []func([]int) int{findMin, findMinPtr, findMinPtrDup} {
		start := time.Now()
		ans := f(nums)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printFindMinAns([]int{3, 4, 5, 1, 2}, 1)
	printFindMinAns([]int{4, 5, 6, 7, 0, 1, 2}, 0)
	printFindMinAns([]int{11, 13, 15, 17}, 11)
	printFindMinAns([]int{2, 2, 2, 0, 1}, 0)
	printFindMinAns([]int{1, 1, 1, 1, 4, 0, 1}, 0)
}

package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func rotateArray(nums []int, k int) {
	l := len(nums)
	k = k % l
	if k == 0 {
		return
	}
	tmp := make([]int, 0, l)
	tmp = append(tmp, nums[l-k:]...)
	tmp = append(tmp, nums[:l-k]...)
	copy(nums, tmp)
}

/* Test */
func printRotateArrayAns(nums []int, w int, exp []int) {
	for _, f := range []func([]int, int){rotateArray} {
		start := time.Now()
		f(nums, w)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, nums, end, exp)
	}
}

func main() {
	printRotateArrayAns([]int{1, 2, 3, 4, 5, 6, 7}, 3, []int{5, 6, 7, 1, 2, 3, 4})
	printRotateArrayAns([]int{-1, -100, 3, 99}, 2, []int{3, 99, -1, -100})
}

package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func productExceptSelf(nums []int) []int {
	n := len(nums)
	a := make([]int, n)
	a[0], a[n-1] = 1, 1
	rightProd := 1
	for i := 1; i < n; i++ {
		a[i] = a[i-1] * nums[i-1]
	}
	for i := n - 2; i >= 0; i-- {
		rightProd *= nums[i+1]
		a[i] *= rightProd
	}
	return a
}

/* Test */
func printProduceExceptSelfAns(nums []int, exp []int) {
	for _, f := range []func([]int) []int{productExceptSelf} {
		start := time.Now()
		ans := f(nums)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	printProduceExceptSelfAns([]int{2, 3, -2, 4}, []int{-24, -16, 24, -12})
	printProduceExceptSelfAns([]int{1, 2, 3, 4}, []int{24, 12, 8, 6})
	printProduceExceptSelfAns([]int{-1, 1, 0, -3, 3}, []int{0, 0, 9, 0, 0})
}

package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func majorityElement(n []int) int {
	// Boyer-Moore Majority Vote Algorithm
	m, f := n[0], 1 // majority element, frequency
	for i := 1; i < len(n); i++ {
		if f == 0 {
			m, f = n[i], 1
		} else {
			if n[i] == m {
				f++
			} else {
				f--
			}
		}
	}
	return m
}

/* Test */
func printMajorityElementAns(w []int, exp int) {
	for _, f := range []func([]int) int{majorityElement} {
		start := time.Now()
		ans := f(w)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s(%v): %+v, elapsed %s, expected %+v\n", fname, w, ans, end, exp)
	}
}

func main() {
	printMajorityElementAns([]int{3, 2, 3}, 3)
	printMajorityElementAns([]int{2, 2, 1, 1, 1, 2, 2}, 2)
	printMajorityElementAns([]int{2, 2, 1, 1, 1, 2, 2, 1, 8, 5, 4, 3, 5, 4, 8}, 2)
}

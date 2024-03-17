package main

import (
	"fmt"
	"reflect"
	"runtime"
	"sort"
	"time"
)

func insertInterval(intervals [][]int, newInterval []int) [][]int {
	var n, i, j int
	n = len(intervals)
	i = sort.Search(n, func(i int) bool { return intervals[i][0] > newInterval[0] })
	j = sort.Search(n, func(j int) bool { return intervals[j][1] > newInterval[1] })
	if i >= 1 && newInterval[0] <= intervals[i-1][1] {
		newInterval[0] = intervals[i-1][0]
		i--
	}
	if j < n && newInterval[1] >= intervals[j][0] {
		newInterval[1] = intervals[j][1]
		j++
	}
	return append(intervals[:i], append([][]int{newInterval}, intervals[j:]...)...)
}

func intervalEquals(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if len(a[i]) != len(b[i]) {
			return false
		}
		for j := range a[i] {
			if a[i][j] != b[i][j] {
				return false
			}
		}
	}
	return true
}

/* Test */
func printInsertIntervalAns(i [][]int, ni []int, exp [][]int) {
	for _, f := range []func([][]int, []int) [][]int{insertInterval} {
		var passed string
		start := time.Now()
		ans := f(i, ni)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		if intervalEquals(exp, ans) {
			passed = "PASSED"
		} else {
			passed = "FAILED"
		}
		fmt.Printf("%s: %d, elapsed %s, expected %d %s\n", fname, ans, end, exp, passed)
	}
}

func main() {
	printInsertIntervalAns([][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, []int{4, 8}, [][]int{{1, 2}, {3, 10}, {12, 16}})
}

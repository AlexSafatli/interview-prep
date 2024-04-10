package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func rBit(c rune) uint32 {
	return 1 << (c - 'a')
}

func partitionString(s string) int {
	var ans = 1
	var c uint32
	for _, r := range s {
		b := rBit(r)
		if 0 < c&b {
			c = 0
			ans++
		}
		c |= b
	}
	return ans
}

/* Test */
func printPartitionStringAns(s string, exp int) {
	for _, f := range []func(string) int{partitionString} {
		start := time.Now()
		ans := f(s)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	printPartitionStringAns("abacaba", 4)
	printPartitionStringAns("ssssss", 6)
}

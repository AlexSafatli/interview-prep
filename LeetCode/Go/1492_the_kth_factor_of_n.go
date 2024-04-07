package main

import (
	"fmt"
	"math"
	"reflect"
	"runtime"
	"time"
)

func kthFactor(n, k int) int {
	if k > n {
		return -1
	}
	sqrt := int(math.Sqrt(float64(n)))
	for i := 1; i <= sqrt; i++ { // up to square root
		if n%i == 0 {
			k--
			if k == 0 {
				return i
			}
		}
	}
	for i := sqrt; i > 0; i-- { // down from square root
		if i*i == n {
			continue
		}
		if n%i == 0 {
			k--
			if k == 0 {
				return n / i
			}
		}
	}
	return -1
}

/* Test */
func printKthFactorAns(w1, w2, exp int) {
	for _, f := range []func(int, int) int{kthFactor} {
		start := time.Now()
		ans := f(w1, w2)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s(%v, %v): %+v, elapsed %s, expected %+v\n", fname, w1, w2, ans, end, exp)
	}
}

func main() {
	printKthFactorAns(12, 3, 3)
	printKthFactorAns(7, 2, 7)
	printKthFactorAns(56, 7, 28)
	printKthFactorAns(4, 4, -1)
}

package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func backtrack(a *[]string, n, open, close int, curr string) { // dfs
	if open == close && close == n { // base case, bottom of tree
		*a = append(*a, curr)
	}
	if open < n { // open can be added (count is less than allowed)
		backtrack(a, n, open+1, close, curr+"(")
	}
	if close < open { // closing can be added if open is there
		backtrack(a, n, open, close+1, curr+")")
	}
}

// Uses backtracking
func generateParantheses(n int) (ans []string) {
	backtrack(&ans, n, 0, 0, "")
	return
}

/* Test */
func printGenerateParanthesesAns(n int, exp []string) {
	for _, f := range []func(int) []string{generateParantheses} {
		start := time.Now()
		ans := f(n)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	printGenerateParanthesesAns(3, []string{"((()))", "(()())", "(())()", "()(())", "()()()"})
	printGenerateParanthesesAns(1, []string{"()"})
}

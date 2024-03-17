package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func longestCommonSubsequence(text1, text2 string) int {
	l1, l2 := len(text1), len(text2)
	dp := make([][]int, l1+1)
	for i := range dp {
		dp[i] = make([]int, l2+1)
	}
	for i := 1; i <= l1; i++ {
		for j := 1; j <= l2; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[l1][l2]
}

func longestCommonSubsequenceDP(text1, text2 string) int {
	dp := make([][]int, len(text1)+1)
	for i := 0; i < len(text1)+1; i++ {
		dp[i] = make([]int, len(text2)+1)
	}
	for i := 0; i < len(text1)+1; i++ {
		for j := 0; j < len(text2)+1; j++ {
			dp[i][j] = -1
		}
	}
	return lcs(0, 0, text1, text2, &dp)
}

// https://en.wikipedia.org/wiki/Longest_common_subsequence#LCS_function_defined
func lcs(i, j int, x, y string, dp *[][]int) int {
	if (*dp)[i][j] != -1 {
		return (*dp)[i][j]
	}
	var l int
	if i == len(x) || j == len(y) {
		l = 0
	} else if x[i] == y[j] {
		l = lcs(i+1, j+1, x, y, dp) + 1
	} else {
		l = max(lcs(i+1, j, x, y, dp), lcs(i, j+1, x, y, dp))
	}
	(*dp)[i][j] = l
	return l
}

/* Test */
func printLongestCommonSubsequenceAns(x, y string, exp int) {
	for _, f := range []func(string, string) int{longestCommonSubsequence, longestCommonSubsequenceDP} {
		start := time.Now()
		ans := f(x, y)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printLongestCommonSubsequenceAns("abcde", "ace", 3)
	printLongestCommonSubsequenceAns("abc", "abc", 3)
	printLongestCommonSubsequenceAns("abc", "def", 0)
}

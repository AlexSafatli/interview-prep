package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func isAlienSorted(words []string, order string) bool {
	if len(words) < 2 {
		return true
	}
	h := make(map[byte]byte)
	var l byte
	for l = 97; l <= 122; l++ {
		h[order[l-97]] = l
	}
	for i := 0; i < len(words)-1; i++ {
		if !inOrder(words[i], words[i+1], h) {
			return false
		}
	}
	return true
}

func inOrder(a, b string, m map[byte]byte) bool {
	for i := 0; i < len(a) && i < len(b); i++ {
		if a[i] != b[i] {
			return m[a[i]] < m[b[i]]
		}
	}
	return len(a) <= len(b)
}

/* Test */
func printIsAlienSortedAns(words []string, order string, exp bool) {
	for _, f := range []func([]string, string) bool{isAlienSorted} {
		start := time.Now()
		ans := f(words, order)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %t, elapsed %s, expected %t\n", fname, ans, end, exp)
	}
}

func main() {
	printIsAlienSortedAns([]string{"hello", "leetcode"}, "hlabcdefgijkmnopqrstuvwxyz", true)
	printIsAlienSortedAns([]string{"word", "world", "row"}, "worldabcefghijkmnpqstuvxyz", false)
	printIsAlienSortedAns([]string{"apple", "app"}, "abcdefghijklmnopqrstuvwxyz", false)
	printIsAlienSortedAns([]string{"app", "apple"}, "abcdefghijklmnopqrstuvwxyz", true)
	printIsAlienSortedAns([]string{"apple"}, "abcdefghijklmnopqrstuvwxyz", true)
}

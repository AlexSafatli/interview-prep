package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func mergeAlternately(word1 string, word2 string) string {
	var a, b, i int
	wl1 := len(word1)
	wl2 := len(word2)
	var s []byte
	s = make([]byte, wl1+wl2)
	for i = 0; i < wl1+wl2; i++ {
		if i%2 == 0 {
			if a < wl1 {
				s[i] = word1[a]
				a++
			} else {
				s[i] = word2[b]
				b++
			}
		} else {
			if b < wl2 {
				s[i] = word2[b]
				b++
			} else {
				s[i] = word1[a]
				a++
			}
		}
	}
	return string(s)
}

/* Test */
func printMergeAlternatelyAns(w1, w2, exp string) {
	for _, f := range []func(string, string) string{mergeAlternately} {
		start := time.Now()
		ans := f(w1, w2)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	printMergeAlternatelyAns("ab", "pqrs", "apbqrs")
	printMergeAlternatelyAns("abcd", "pq", "apbqcd")
}

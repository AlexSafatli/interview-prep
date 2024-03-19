package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

var (
	vowels [256]bool
	t      = "aeiouAEIOU"
)

func reverseVowels(s string) string {
	var ans []byte
	ans = make([]byte, len(s))
	var i, j int
	j = len(s) - 1
	for c := 0; c < len(s); c++ {
		ans[c] = s[c]
	}
	for i < j {
		for j > i && !vowels[s[j]-'a'] {
			j--
		}
		if vowels[s[i]-'a'] {
			ans[i], ans[j] = ans[j], ans[i]
			j--
		}
		i++
	}
	return string(ans)
}

/* Test */
func printReverseVowelsAns(w, exp string) {
	for _, f := range []func(string) string{reverseVowels} {
		start := time.Now()
		ans := f(w)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	for c := range t {
		vowels[t[c]-'A'] = true
		vowels[t[c]-'a'] = true
	}

	printReverseVowelsAns("hello", "holle")
	printReverseVowelsAns("leetcode", "leotcede")
}

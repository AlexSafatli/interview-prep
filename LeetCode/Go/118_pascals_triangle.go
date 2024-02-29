package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func generateRow(row int) []int {
	val := 1
	ans := make([]int, row)
	ans[0] = 1
	for col := 1; col < row; col++ {
		val *= row - col
		val /= col
		ans[col] = val
	}
	return ans
}

// Using nCr logic of generating rows/binary coefficients of each row
func generatePascalsTriangle(numRows int) (ans [][]int) {
	ans = make([][]int, numRows)
	for row := 1; row <= numRows; row++ {
		ans[row-1] = generateRow(row)
	}
	return
}

// Using a form of DP without building a full matrix
func generatePascalsTriangleDP(numRows int) (ans [][]int) {
	ans = make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		row := make([]int, i+1)
		for j := 0; j <= i; j++ {
			if j == 0 || j == i {
				row[j] = 1 // edges (left and right elements)
			} else {
				row[j] = ans[i-1][j-1] + ans[i-1][j] // pascal's rule
			}
		}
		ans[i] = row
	}
	return
}

/* Test */
func printGeneratePascalsTriangleAns(n int, exp [][]int) {
	for _, f := range []func(int) [][]int{generatePascalsTriangle, generatePascalsTriangleDP} {
		start := time.Now()
		ans := f(n)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %+v, elapsed %s, expected %+v\n", fname, ans, end, exp)
	}
}

func main() {
	printGeneratePascalsTriangleAns(5, [][]int{{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}})
	printGeneratePascalsTriangleAns(1, [][]int{{1}})
}

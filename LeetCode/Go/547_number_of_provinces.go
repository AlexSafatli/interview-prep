package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

// @SEE Algorithms, 4th Edition p. 228
type DSU struct {
	id    []int
	sz    []int
	count int
}

func NewDSU(n int) *DSU {
	parents := make([]int, n)
	size := make([]int, n)
	for i := range parents {
		parents[i] = i
		size[i] = 1
	}
	return &DSU{id: parents, sz: size, count: n}
}

func (d *DSU) find(p int) int {
	for d.id[p] != p { // compress path for each node (makes MST)
		d.id[p] = d.id[d.id[p]]
		p = d.id[p]
	}
	return p
}

func (d *DSU) union(p, q int) {
	p, q = d.find(p), d.find(q)
	if p == q {
		return
	}
	// make smaller root point to larger one (weighted quick union)
	if d.sz[p] < d.sz[q] {
		p, q = q, p
	}
	d.sz[q] += d.sz[p]
	d.id[p] = q
	d.count--
}

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	d := NewDSU(n)
	for a, connections := range isConnected {
		for b, connected := range connections {
			if connected == 1 {
				if d.find(a) != d.find(b) {
					d.union(a, b)
				}
			}
		}
	}
	return d.count
}

/* Test */
func printFindCircleNumAns(isConnected [][]int, exp int) {
	for _, f := range []func([][]int) int{findCircleNum} {
		start := time.Now()
		ans := f(isConnected)
		end := time.Since(start)
		fname := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Printf("%s: %d, elapsed %s, expected %d\n", fname, ans, end, exp)
	}
}

func main() {
	printFindCircleNumAns([][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}, 2)
	printFindCircleNumAns([][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}, 3)
}

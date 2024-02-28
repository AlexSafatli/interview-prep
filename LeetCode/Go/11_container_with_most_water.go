package main

import (
	"fmt"
)

func maxArea(height []int) int {
	var left, right, maxArea int
	right = len(height) - 1
	for left < right {
		currArea := min(height[left], height[right]) * (right - left)
		maxArea = max(maxArea, currArea)
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return maxArea
}

/* Main (Test) */
func main() {
	a1 := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	a2 := []int{1, 1}
	fmt.Println(maxArea(a1) == 49)
	fmt.Println(maxArea(a2) == 1)
}

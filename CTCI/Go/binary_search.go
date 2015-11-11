package main
import "fmt"

func binarySearch(arr *[18]int, key int) int {
  low := 0
  up  := 18 - 1
  mid := (low+up)/2
  for arr[mid] != key && low <= up {
    if key < arr[mid] {
      up = mid - 1;
    } else if key > arr[mid] {
      low = mid + 1;
    }
    mid = (low+up)/2
  }
  if (low <= up) {
    return mid
  }
  return -1
}

/* Main (Test) */
func main() {
  arr := [...]int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,85}
  fmt.Println(arr[binarySearch(&arr, 16)] == 16)
  fmt.Println(arr[binarySearch(&arr, 85)] == 85)
  fmt.Println(arr[binarySearch(&arr, 3)] == 3)
}
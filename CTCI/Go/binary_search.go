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
  arr := [...]int{12,32,4,23,6,42,16,3,85,23,4,7,3,5,45,34,2,1}
  fmt.Println(arr[binarySearch(&arr, 85)])
}
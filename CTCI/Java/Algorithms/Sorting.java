package algorithms;

public class Sorting {

  public static int binarySearch(int[] arr, int key) {
    // Assume array is sorted.
    int lower = 0, upper = arr.length - 1, mid = (lower+upper)/2;
    while (arr[mid] != key && lower <= upper) {
      if      (key < arr[mid]) upper = mid - 1;
      else if (key > arr[mid]) lower = mid + 1;
      mid = (lower+upper)/2;
    }
    return (lower <= upper) ? mid : -1;
  }

}
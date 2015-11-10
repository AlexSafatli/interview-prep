import algorithms.Sorting;
class BinarySearch {

  public static void main(String[] args) {
    int[] arr = { 0,1,2,3,4,5,6,7,8,21,25,28 };
    System.out.println(arr[Sorting.binarySearch(arr,25)]); // should print 25
  }

}
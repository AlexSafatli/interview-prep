import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class ProductOfOtherNumbers {

  public static List<Integer> getProductsOfAllIntsExceptAtIndex(
    List<Integer> intList) {
    int n = intList.size(), product = 1;
    List<Integer> productsOfAllIntsExceptAtIndex = new ArrayList<Integer>(n);
    // Sweep forward - multiply all before index.
    for (int i = 0; i < n; ++i) {
      productsOfAllIntsExceptAtIndex.add(product);
      product *= intList.get(i);
    }
    // Sweep backwards - multiply all after index.
    product = 1;
    for (int i = n-1; i >= 0; --i) {
      int val = productsOfAllIntsExceptAtIndex.get(i);
      productsOfAllIntsExceptAtIndex.set(i, product * val);
      product *= intList.get(i);
    }
    return productsOfAllIntsExceptAtIndex;
  }

  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    int num = stdin.nextInt();
    List<Integer> testList = new ArrayList<Integer>(num);
    for (int i = 0; i < num; ++i) testList.add(stdin.nextInt());
    System.out.println(getProductsOfAllIntsExceptAtIndex(testList));
  }

}
/*
Given integer N traverse its digits (d_1, d_2, ...) and determine how many 
digits evenly divide N - print the number of evenly divisible digits.
*/

import java.util.*;

public class FindDigits {
  private static Scanner stdin = new Scanner(System.in);
  public static void main(String[] args) {
    int numTestCases = stdin.nextInt();
    for (int i = 0; i < numTestCases; ++i)
      System.out.println(numEvenlyDividingDigits());   
  }
  public static int numEvenlyDividingDigits() {
    int n = stdin.nextInt(), k = n, numDividing = 0;
    while (k > 0) {
      int d = k % 10;
      if (d != 0 && n % d == 0) ++numDividing;
      k /= 10;
    }
    return numDividing;
  }
}
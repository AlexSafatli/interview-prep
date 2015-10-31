import java.util.Scanner;

class Solution {

  public static int getHighestProductOfThree(int[] arr) {
    int highestValue, highestProductOf2, highestProductOf3,
      lowestValue, lowestProductOf2;
    highestValue      = Math.max(arr[0],arr[1]);
    lowestValue       = Math.min(arr[0],arr[1]);
    highestProductOf2 = arr[0] * arr[1];
    lowestProductOf2  = highestProductOf2;
    highestProductOf3 = highestProductOf2 * arr[2];
    for (int i = 2; i < arr.length; ++i) {
      highestProductOf3 = Math.max(Math.max(
        highestProductOf3,arr[i]*highestProductOf2),arr[i]*lowestProductOf2);
      highestProductOf2 = Math.max(Math.max(
        highestProductOf2,arr[i]*highestValue), arr[i]*lowestValue);
      lowestProductOf2  = Math.min(Math.min(
        lowestProductOf2,arr[i]*lowestValue),arr[i]*highestValue);
      highestValue      = Math.max(arr[i], highestValue);
      lowestValue       = Math.min(arr[i], lowestValue );
    }
    return highestProductOf3;
  }

  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    int num = stdin.nextInt();
    if (num >= 3) {
      int[] arr = new int[num];
      for (int i = 0; i < num; ++i) arr[i] = stdin.nextInt();
      System.out.println(getHighestProductOfThree(arr));
    } else throw new Error("Need at least three values.");
  }

}
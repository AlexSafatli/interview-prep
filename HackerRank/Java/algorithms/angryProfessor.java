/*
The professor is conducting a course on Discrete Mathematics to a class of N 
students. He is angry at the lack of their discipline, and he decides to cancel 
the class if there are fewer than K students present after the class starts.

Given the arrival time of each student, your task is to find out if the class 
gets cancelled or not.

For each of N testcases, print "YES" (without quotes) if the class gets 
cancelled and "NO" (without quotes) otherwise.
*/

import java.util.*;

public class Solution {
  private static Scanner stdin = new Scanner(System.in);
  public static void main(String[] args) {
    int numTestCases = stdin.nextInt();
    for (int i = 0; i < numTestCases; ++i)
      System.out.println(isClassCancelled() ? "YES" : "NO");   
  }
  public static boolean isClassCancelled() {
    int n = stdin.nextInt(), k = stdin.nextInt(), numBeforeStart = 0;
    for (int i = 0; i < n; ++i) {
      int arrival = stdin.nextInt();
      if (arrival <= 0) ++numBeforeStart;
    }
    return (numBeforeStart < k);
  }
}
/* =============================================================================
http://hackerrank.com/challenges/sherlock-and-the-beast
================================================================================

Sherlock Holmes is getting paranoid about Professor Moriarty, his arch-enemy. 
All his efforts to subdue Moriarty have been in vain. These days Sherlock is 
working on a problem with Dr. Watson. Watson mentioned that the CIA has been 
facing weird problems with their supercomputer, 'The Beast', recently.

This afternoon, Sherlock received a note from Moriarty, saying that he has 
infected 'The Beast' with a virus. Moreover, the note had the number N printed 
on it. After doing some calculations, Sherlock figured out that the key to 
remove the virus is the largest Decent Number having N digits.

DECENT NUMBER: 3, 5, or both as digits; number of times 3 appears is divisible 
by 5; number of times 5 appears is divisible by 3.

INPUT: Integer T (number of test cases); T lines follow with: an integer N.
OUTPUT: For each test case, the largest DECENT NUMBER with N digits. If none, 
-1.
EXPLANATIONS: N = 1, no such number; N = 3, 555 only possible number; N = 5, 
33333 only possible number; N = 11, 55555533333 and all permutations of these 
digits are valid numbers - among them, the given number is the largest one.

============================================================================= */

import java.util.*;

class Solution {

  public static String largestDecentNumberWithNDigits(int n) {
    if  (n == 1)  return "-1";
    if  (n == 3)  return "555";
    if  (n == 5)  return "33333";
    if  (n == 11) return "55555533333";
    int z = n;
    while ((z % 3) != 0) {
      z -= 5;
      if (z < 0) return "-1";
    }
    return repeat("5", z) + repeat("3",(n - z));
  }

  public static String repeat(String num, int count) {
    if (count == 0) return "";
    return new String(new char[count]).replace("\0",num);
  }

  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    int t = stdin.nextInt();
    for (; t > 0; --t)
      System.out.println(largestDecentNumberWithNDigits(stdin.nextInt()));
  }

}
/*
You are given an integer N depicting the height of the staircase.
Draw a staircase of height N in the format given below.

     #
    ##
   ###
  ####
 #####
######

where N = 6.
*/

import java.util.*;

public class Staircase {
  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    int n = stdin.nextInt();
    if (n > 100) { n = 100; }
    for (int i = 0; i < n; ++i) {
      String s = "";
      while (s.length() < (n-i-1)) { s += " "; }
      while (s.length() != n) { s += "#"; }
      System.out.println(s);
    }
  }
}
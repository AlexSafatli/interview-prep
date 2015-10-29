/* =============================================================================
https://www.hackerrank.com/challenges/utopian-tree
================================================================================

The Utopian Tree goes through 2 cycles of growth every year. The first growth 
cycle occurs during the spring, when it doubles in height. The second growth 
cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. Its height 
is 1 meter. Can you find the height of the tree after N growth cycles?

INPUT: Integer T (number of test cases); T lines follow with: an integer N.
OUTPUT: For each test case, the height of Utopian Tree after N cycles.

============================================================================= */

import java.util.*;

class Solution {

  public static int heightOfTree(int numCycles) {
    int height = 1;
    for (int n = 1; n <= numCycles; ++n) {
      if (n % 2 != 0) height *= 2;
      else ++height;
    }
    return height;
  }

  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    int t = stdin.nextInt();
    for (; t > 0; --t) System.out.println(heightOfTree(stdin.nextInt()));
  }

}
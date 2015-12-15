/*
Calvin is driving his favorite vehicle on the 101 freeway. He notices that the 
'Check Engine' light is on - he wants to service his vehicle immediately. A 
service lane runs parallel on the highway. The length of that lane is N units 
and consists of N segments of equal length and different widths.

Calvin can enter to and exit from any of these segments. Let entry segment be 
i and exit as j. Assume that exit j >= enter index i and that 0 <= i. All 
segments between both i and j must be passed through (inclusive).

There are three types of vehicles (BIKE, CAR, TRUCK) or (1, 2, 3) also 
representing the size of the vehicle. Given array 'widths' of size N, only the 
bike can pass through a segment of width 1 and so on. Given entry and exit, 
output type of largest vehicle that can pass through service lane.
*/

import java.util.*;

public class ServiceLane {

  private static Scanner stdin = new Scanner(System.in);
  private static int[] widths;

  public static void main(String[] args) {
    int N = stdin.nextInt(), T = stdin.nextInt();
    widths = new int[N];
    for (int i = 0; i < N; ++i)
      widths[i] = stdin.nextInt();
    for (int i = 0; i < T; ++i)
      System.out.println(largestVehicle(stdin.nextInt(), stdin.nextInt()));   
  }

  public static int largestVehicle(int i, int j) {
    // @todo Represent vehicle as enum.
    int largest = widths[i];
    for (int n = i; n <= j; ++n)
      largest = Math.min(largest, widths[n]);
    return largest;
  }

}
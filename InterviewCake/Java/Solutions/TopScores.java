import java.util.Arrays;
public class TopScores {

  public static int[] sortScores(int[] unsortedScores, 
    int highestPossibleScore) {
    // Counting Sort - non-comparison based
    int[] count = new int[highestPossibleScore+1];
    int[] sorted = new int[unsortedScores.length];
    int cursor = 0;
    for (int score : unsortedScores) ++count[score];
    for (int score = 0; score <= highestPossibleScore; ++score) {
      int c = count[score];
      for (int occ = 0; occ < c; ++occ) {
        sorted[cursor] = score;
        ++cursor;
      }
    }
    return sorted;
  }

  public static void main(String[] args) {
    int[] arr = { 2, 3, 7, 10, 18, 7, 12 };
    System.out.println(Arrays.toString(sortScores(arr, 18)));
  }

}
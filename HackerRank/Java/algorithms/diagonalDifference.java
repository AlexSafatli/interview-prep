import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int n = stdin.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) matrix[j][i] = stdin.nextInt();
        }
        int sumOriginDiag = 0, sumOtherDiag = 0, diff;
        for (int i = 0; i < n; ++i) {
            sumOriginDiag += matrix[i][i];
            sumOtherDiag += matrix[i][n-i-1];
        }
        diff = sumOriginDiag - sumOtherDiag;
        System.out.println((diff < 0) ? -diff : diff);
    }
}

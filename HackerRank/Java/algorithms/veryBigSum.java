import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        long sum = 0;
        for (int n = stdin.nextInt(); n > 0; --n) sum += stdin.nextLong();
        System.out.println(sum);
    }
}

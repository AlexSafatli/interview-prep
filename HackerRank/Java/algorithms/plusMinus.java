/*
You're given an array containing integer values.
You need to print the fraction of count of positive numbers, negative numbers and zeroes to the total numbers.
Print the value of the fractions correct to 3 decimal places.
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        float pos, neg, zeroes;
        int posCount = 0, negCount = 0, zeroCount = 0, total = 0;
        for (int n = stdin.nextInt(); n > 0; --n) {
            int val = stdin.nextInt();
            if (val > 0) ++posCount;
            else if (val < 0) ++negCount;
            else ++zeroCount;
            ++total;
        }
        
    }
}
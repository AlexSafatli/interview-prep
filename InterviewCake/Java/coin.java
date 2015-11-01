class Solution {

  public static int numberOfWaysToMakeAmountWithDenominations(int amount,
    int[] denominations) {
    // waysForNCents[k] = how many ways to get to k cents using denominations
    int[] waysForNCents = new int[amount + 1];
    waysForNCents[0] = 1; // Always only a single way to make 0 cents.
    for (int i = 0; i < denominations.length; ++i) {
      int coin = denominations[i];
      for (int higher = coin; higher < amount + 1; ++higher) {
        // Bottom-up calculate successively larger remainders.
        waysForNCents[higher] += waysForNCents[higher - coin];
      }
    }
    return waysForNCents[amount];
  }

  public static void main(String[] args) {
    System.out.println(numberOfWaysToMakeAmountWithDenominations(4, 
      new int[] { 1, 2, 3 })); // #=> 4
    System.out.println(numberOfWaysToMakeAmountWithDenominations(5,
      new int[] { 1, 3, 5 })); // #=> 3
  }

}
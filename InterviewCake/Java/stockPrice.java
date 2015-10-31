class Solution {

  public int getMaxProfit(int[] stockPricesYesterday) {
    if (stockPricesYesterday.length < 2) {
      throw new IllegalArgumentException("Need at least two prices.");
    }
    int minPrice = stockPricesYesterday[0], // O(1) space
      maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];
    for (int i = 1; i < stockPricesYesterday.length; ++i) { // O(n) time
      int current = stockPricesYesterday[i],
        potential = current - minPrice;
      maxProfit   = Math.max(potential, maxProfit);
      minPrice    = Math.min(current  , minPrice );
    }
    return maxProfit;
  }

}
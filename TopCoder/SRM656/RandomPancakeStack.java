/* Problem statement is at
http://community.topcoder.com/stat?c=problem_statement&pm=13747 */

/* - Pancakes are numbered from 0 to N-1. There are N pancakes.
   - Pancake i has width i+1 and deliciousness d[i].
   - Choose first pancake uniformly at random. Place onto plate.
   - While (pancakes are left), choose randomly and if width > width on top of
   the stack, remove it -- otherwise, place it on top.
 */

public class RandomPancakeStack {
	public static double expectedDeliciousness(int[] d) {
		int n = d.length;
		double[][] DP = new double[n+1][n+1]; // for dynamic progr.		
		for (int got = n; got >= 0; --got) {
			int pancakesLeft = n-got;
			for (int last = 0; last+got <= n; ++last) {
				if (pancakesLeft == 0) {
					DP[got][last] = 0.;
					continue;
				}
				double sum = 0;
				for (int nextPancake = 0; nextPancake < last; ++nextPancake)
					sum += (1./pancakesLeft)*(d[nextPancake]+
						DP[got+1][nextPancake]);
				DP[got][last] = sum;
			}
		}
		return DP[0][n]; 
	}
	public static void main(String[] args) {
		int[] test = {1,1,1};
		System.out.println(expectedDeliciousness(test));
	}
}
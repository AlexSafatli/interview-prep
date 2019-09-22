import java.util.Scanner;

public class B {
	private class ThreeNumberBuffer {
		private double a = 0, b = 0, c = 0;

		public void enqueue(double n) {
			a = b;
			b = c;
			c = n;
		}
	}

	public static void main(String[] args) {
		ThreeNumberBuffer buffer = new ThreeNumberBuffer();
		double maximalAverage = 0;
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			double n = in.nextDouble();
			if (n == -2) {
				System.exit(0);
			} else if (n == -1) {
				System.out.printf("%.2f\n", maximalAverage);
				maximalAverage = 0;
			} else {
				buffer.enqueue(n);
				double newAverage = (buffer.a + buffer.b + buffer.c)/3;
				if (newAverage > maximalAverage) {
					maximalAverage = newAverage;
				}
			}
		}
	}	
}
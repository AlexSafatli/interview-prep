import java.util.Scanner;

public class A {
	public static String readLine(double a, double b, double c) {
		double min = Math.min(a, Math.min(b, c));
		if (min >= 120) {
			return "hurricane";
		} else {
			if (Math.max(a, Math.max(b, c)) < 59) {
				System.exit(1);
			}
			return "tropical";
		}

	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			double a = in.nextDouble();
			double b = in.nextDouble();
			double c = in.nextDouble();
			System.out.println(readLine(a, b, c));
		}
	}	
}
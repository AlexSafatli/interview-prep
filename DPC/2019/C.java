import java.util.Scanner;

public class C {
	public static int countWalls(String[] lines, int size) {
		boolean[][] labyrinth = new boolean[size][size];
		for (int i = 0; i < size; ++i) {
			String line = lines[i];
			char[] chars = line.toCharArray();
			for (int j = 0; j < size; ++j) {
				labyrinth[i][j] = chars[j] == 'x';
			}
		}
		int wallCount = 0;
		for (int i = 0; i < size; ++i) {
			for (int j = 0; j < size; ++j) {
				if (i-1 == -1 || labyrinth[i-1][j]) {
					++wallCount;
				}
				if (j-1 == -1 || labyrinth[i][j-1]) {
					++wallCount;
				}
				if (i+1 == size || labyrinth[i+1][j]) {
					++wallCount;
				}
				if (j+1 == size || labyrinth[i][j+1]) {
					++wallCount;
				}
			}
		}
		return wallCount;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int size = in.nextInt();
			String[] lines = new String[size];
			for (int i = 0; i < size; ++i) {
				lines[i] = in.nextLine();
			}
			System.out.println(countWalls(lines, size)*3*3);
		}
	}	
}
/* Problem Statement found at
http://community.topcoder.com/stat?c=problem_statement&pm=13748 */

public class CorruptedMessage {
	public static String reconstructMessage(String s, int k) {
		int[] counts = new int[128]; // Number of characters in ASCII.
		char c = 'a'; // Keep track of what the single character is for output.
		// Count the number of uses of each character. O(n) where n = len(s).
		for (int i = 0; i < s.length(); ++i) {
			++counts[s.charAt(i)]; // Count the number of uses of a character.
		}
		// Go over all possible characters from 'a' to 'z' and see which match.
		for (int i = 'a'; i <= 'z'; ++i) {
			if (counts[i] == s.length() - k) {
				// The number of missing characters matches.
				c = (char)i;
				return constructMessageOfNumLetters(c,s.length());
			}
			else if (counts[i] == 0) {
				c = (char)i;
			}
		} 
		return constructMessageOfNumLetters(c,s.length());
	}
	public static String constructMessageOfNumLetters(char c, int k) {
		String out = "";
		for (int i = 0; i <= k; ++i) {
			out += c;
		}
		return out;
	}
	public static void main(String[] args) {
		String test = "hello";
		System.out.println(reconstructMessage(test,3));
	}
}
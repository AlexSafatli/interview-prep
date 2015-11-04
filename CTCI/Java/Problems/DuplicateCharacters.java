import java.util.Map;
import java.util.HashMap;

class Solution {

  public static void main(String[] args) {
    Map<Character,Boolean> seen = new HashMap<Character,Boolean>();
    String s = args[0]; char[] chars = new char[s.length()];
    for (int i = 0; i < s.length(); ++i) {
      if (seen.get(s.charAt(i)) == null) {
        seen.put(s.charAt(i), true);
        chars[i] = s.charAt(i);
      }
    }
    System.out.println(new String(chars));
  }

}
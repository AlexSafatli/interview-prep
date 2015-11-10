class Palindromes {

  public static boolean isPalindrome(String s) {
    int l = s.length();
    for (int i = 0; i < l/2; ++i) {
      if (s.charAt(i) != s.charAt(l-i-1)) return false;
    } return true;
  }

  public static void main(String[] args) {
    if (args.length != 1) return; 
    String s = args[0];
    System.out.println(isPalindrome(s));
  }

}
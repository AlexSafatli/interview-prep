class Palindromes {

  public static boolean isPalindrome(String s) {
    int l = s.length();
    for (int i = 0; i < l/2; ++i) {
      char a = s.charAt(i), b = s.charAt(l-i-1);
      if (a != b) return false;
    }
    return true;
  }

  public static void main(String[] args) {
    if (args.length != 1) return; 
    String s = args[0];
    System.out.println(isPalindrome(s));
  }

}
using System.Collections.Generic;

namespace InterviewCake
{
    class PermutationPalindrome
    {
        internal static bool HasPalindromePermutation(string st)
        {
            HashSet<char> unpairedChars;
            unpairedChars = new HashSet<char>();
            foreach (char c in st)
            {
                if (unpairedChars.Contains(c))
                {
                    unpairedChars.Remove(c);
                }
                else
                {
                    unpairedChars.Add(c);
                }
            }
            return unpairedChars.Count <= 1;
        }
    }

}
using System;

namespace InterviewCake
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var a1 = PermutationPalindrome.HasPalindromePermutation("civic");
            var a2 = PermutationPalindrome.HasPalindromePermutation("icvic");
            var a3 = PermutationPalindrome.HasPalindromePermutation("liquid");
            Console.WriteLine(a1);
            Console.WriteLine(a2);
            Console.WriteLine(a3);

            var a4 = GetClosingParanthesis.GetClosingParen("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing", 10);
            Console.WriteLine(a4);

            Console.ReadLine();
        }

    }
}

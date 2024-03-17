namespace InterviewCake
{
    internal class GetClosingParanthesis
    {
        internal static int GetClosingParen(string st, int openingParenIndex)
        {
            int openNestedParens = 0;
            for (int i = openingParenIndex + 1; i < st.Length; i++)
            {
                if (st[i] == '(')
                {
                    openNestedParens++;
                }
                else if (st[i] == ')')
                {
                    if (openNestedParens == 0)
                    {
                        return i;
                    }
                    else
                    {
                        openNestedParens--;
                    }
                }
            }
            return -1;
        }
    }
}
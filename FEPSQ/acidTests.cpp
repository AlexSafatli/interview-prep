#include <string>
#include <iostream>

using namespace std;

string reverse(string str) {
  // Get integer values.
  int length = str.size(), midpt  = length/2;
  char strArr[length];
  str.copy(strArr,length+1); // Convert to array.
  // Swap and reverse.
  for (int i = 0; i < midpt; ++i) {
    char c = strArr[length-1-i];
    strArr[length-1-i] = strArr[i];
    strArr[i] = c;
  }
  return string(strArr);
}

unsigned long fibRecursive(int n) { // Recursive.
  return (n <= 1) ? n : fibRecursive(n-1) + fibRecursive(n-2);
}

unsigned long fib(int n) { // Iterative
  int curr = 0, next = 1;
  for (int i = 0; i < n; ++i) {
    next += curr;
    curr  = next-curr;
  }
  return curr;
}

int main(int n, char* args[]) {
  // Perform tests.
  string str = string("Madam, I'm Adam");
  cout << reverse(str) << endl;
  cout << fib(25) << endl;
  cout << fibRecursive(25) << endl;
  return 0;
}
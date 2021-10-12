import sys

def reverseString(string):
  length = len(string)
  midpt  = length/2
  strli  = list(string)
  for i in xrange(midpt):
    c = strli[i]
    strli[i] = strli[length-1-i]
    strli[length-1-i] = c
  return ''.join(strli)

def fibIterative(n):
  high,low = 1,0
  for x in xrange(0,n):
    high+=low
    low=high-low
  return low

def printMultiplicationTables(max):
  for i in xrange(1,max+1):
    for j in xrange(1,max+1):
      sys.stdout.write('%4d ' % (i*j))
    sys.stdout.write('\n')

if __name__ == '__main__':
  # Perform tests on all acid test functions.
  s = "Madam, I'm Adam"
  print 'String: %17s' % (s)
  print 'Reversed: %15s' % (reverseString(s))
  print '\nNth Fibonacci Number:'
  for n in xrange(0,10+1): print '\tN = %3d -> %3d' % (n,fibIterative(n))
  print '\tN = %3d -> %3d' % (25,fibIterative(25))
  print '\nMultiplication Table (up to 12*12):'
  printMultiplicationTables(12)

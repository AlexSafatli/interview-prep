def fib(n):
	''' Iterative solution to finding the Nth Fibonacci number. '''

	up,lo = 1,0
	for x in xrange(0,n):
		up += lo # high = high added to lo
		lo = (up-lo) # lo = what high was
	return lo


def isPrime(n):
	''' Solution extracted from a Project Euler solution of mine. '''

	if (n <= 1): return False # 1 is not considered prime.
	elif (n == 2): return True # 2 is first prime number.
	elif (n % 2 == 0): return False # A multiple of 2, not prime.
	i = 3
	while (i*i <= n):
		# Only need to look up to square root of n.
		if (n % i == 0): return False
		i += 2
	return True

# 19.1 (pg 265)
def swapinPlace(a,b):
    ''' Takes two integer values and swaps them in place. '''
    a = (a+b)
    b = (a-b)
    a = (a-b)
    return a,b

# 19.3 (pg 268); determine number of zeroes in n factorial by counting multiples of 5.

# 20.1 (pg 279); add two numbers NOT using any arithmetic operators.
def addNoArithmeticOperators(a,b):
	if (b == 0): return a
	sumNoCarry = a ^ b # No carry.
	carry = (a & b) << 1 # Carry (do not add).
	return addNoArithmeticOperators(sumNoCarry,carry) # Recurse.


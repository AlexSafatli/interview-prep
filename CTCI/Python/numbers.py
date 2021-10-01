import typing


def fib(n: int) -> int:
    """Finds the nth Fibonacci number, iterative."""
    up, lo = 1, 0
    for i in range(0, n):
        up += lo
        lo = up - lo  # what high was
    return lo


def is_prime(n: int) -> bool:
    """Solution extracted from a Project Euler solution of mine."""
    if n <= 1:
        return False  # 1 is not considered prime
    elif n == 2:
        return True  # 2 is considered (first) prime
    elif n % 2 == 0:
        return False  # a multiple of 2 (not prime)
    i = 3
    while i * i <= n:
        # Only need to look up to square root of n
        if n % i == 0:
            return False
        i += 2
    return True


# 20.1 (pg 279); add two numbers NOT using any arithmetic operators.
def add_no_arithmetic_operators(a: int, b: int) -> int:
    if b == 0:
        return a
    sum_no_carry = a ^ b  # no carry
    carry = (a & b) << 1  # carry (do not add)
    return add_no_arithmetic_operators(sum_no_carry, carry)


# Implementation of the binary search algorithm for a list of integers.
def binary_search(arr: typing.List[int], key: int) -> int:
    # Assumes already sorted array
    lower = 0
    upper = len(arr) - 1
    mid = int((lower + upper) / 2)
    while arr[mid] != key and lower < upper:
        if key < arr[mid]:
            upper = mid - 1
        elif key > arr[mid]:
            lower = mid + 1
        mid = int((lower + upper) / 2)
    if lower <= upper:  # number was found
        return mid
    return - 1  # was not found


if __name__ == '__main__':
    print('fib(5):', fib(5))
    print('is_prime(7):', is_prime(7))
    print('is_prime(673):', is_prime(673))
    print('add_no_arithmetic_operators(5,8):',
          add_no_arithmetic_operators(5, 8))
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 21, 25, 28]
    print(numbers[binary_search(numbers, 25)])
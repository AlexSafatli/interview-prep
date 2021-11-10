import typing
import math

from common import *


def compare_triplets(a: tuple, b: tuple) -> typing.Tuple[int, int]:
    # Rating is a triplet a = (a[0], a[1], a[2]) and b = (b[0], b[1], b[2])
    # Find comparison points by comparing respective index values and:
    #   - if a[i] > b[i], a is awarded 1 point
    #   - if b[i] < a[i], b is awarded 1 point
    #   - if a[i] = b[i], neither receives
    # comparison points = total points a person earned
    # return tuple (comparison_pts_for_a, comparison_pts_for_b)
    n = len(a)
    rewards = [0, 0]
    assert n == len(b)
    for i in range(n):
        if a[i] > b[i]:
            rewards[0] += 1
        elif a[i] < b[i]:
            rewards[1] += 1
    return rewards[0], rewards[1]


def mini_max_sum(arr: list) -> tuple:
    n = len(arr)
    arr = sorted(arr)  # if sorted, min is first n eles, max is last n eles
    return sum(arr[0:n - 1]), sum(arr[1:n])


def birthday_cake_candles(candles: list) -> int:
    tallest = max(candles)
    count = 0
    candles.sort()
    for i in range(len(candles) - 1, -1, -1):
        if candles[i] == tallest:
            count += 1
        else:
            return count
    return count


def time_conversion(s: str) -> str:
    # Given a time in 12h format, return it in 24h format.
    # Input format example:  07:05:45PM
    # Output format example: 19:05:45
    hour = int(s[:2])
    ampm = s[-2:]
    offset = 12 if ampm == 'PM' else 0
    return '%.2d:%s' % (hour % 12 + offset, s[3:-2])


def grading_students(grades: list) -> list:
    # Students are graded 0 to 100 inclusive. Any grade < 40 is failing.
    # If difference between grade and next multiple of 5 is < 3, round grade up
    # to next multiple of 5. If grade is < 38, no rounding occurs (will still be
    # a fail).
    #
    # Example: grade = 84, rounded to 85
    #          grade = 29, no rounding
    #          grade = 57, no rounding (60-57 is 3 or higher)
    #
    # This function returns grades after this rounding method.
    for i, grade in enumerate(grades):
        if grade < 38 or grade == 100:
            continue
        n = int(math.ceil(grade / 5.0) * 5)
        if n - grade < 3:
            grades[i] = n
    return grades


def forming_magic_square(s: list) -> int:
    # Define magic square to be n*n matrix of distinct + integers from 1 to n^2
    # where the sum of any row, column, or diag. of length n = same number; a
    # "magic constant". Given a 3*3 matrix (s) of integers in range [1,9] (not
    # necessarily a magic square).
    #
    # Can convert any digit a to another digit b in range [1,9] at cost |a-b|.
    # Given s, convert it into a magic square at minimal cost.
    s = s[0] + s[1] + s[2]  # reform to 1D
    m = all_magic_squares_for_3_by_3()  # can be pre-computed
    min_cost = None
    for sq in m:
        diff = 0
        for i, j in zip(s, sq):
            diff += abs(i - j)
        if min_cost is None:
            min_cost = diff
        else:
            min_cost = min(diff, min_cost)
    return min_cost


def library_fine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    # d1, m1, y1: returned date day, month and year, each an integer
    # d2, m2, y2: due date day, month and year, each an integer
    if y1 > y2:
        return 10000  # fixed fine
    elif y2 > y1:
        return 0
    if m1 > m2:
        return 500 * (m1 - m2)
    elif m2 > m1:
        return 0
    return 0 if d1 <= d2 else 15 * (d1 - d2)


def bon_appetit(bill: typing.List[int], k: int, b: int) -> int:
    # When splitting a bill at dinner, each of two friends Anna/Brian will only
    # pay for the items they consume. B gets the check and calculates A's part.
    # You must determine if the calc is correct. For example, assume bill has
    # the following prices: bill = [2, 4, 6]. Anna declines eating k = bill[2]
    # which costs 6. If B calculates the bill correctly, A pays (2+4)/2 = 3.
    # If he includes cost of bill[2], = 6 and should refund 3 to Anna.
    #
    # This function returns 0 (Bon Appetit) if bill is fairly split. Otherwise
    # print aamounnt B owes A (the amount of which they paid was b).
    f = sum(bill)
    f -= bill[k]
    return b - f // 2


def picking_numbers(a: typing.List[int]) -> int:
    # Given array of integers (a), find longest subarray where abs diff b/w any
    # two elements is <= 1.
    #
    # Example: a = [1,1,2,2,4,4,5,5,5]
    # Two subarrays meet this: [1,1,2,2] and [4,4,5,5,5]. Maximum length is 5.
    a = sorted(a)  # make sure array is sorted
    if len(set(a)) == 1:
        return len(a)  # check edge case where all elements are same
    max_len = 0
    start = 0
    for i in range(0, len(a) - 1):
        if abs(a[i + 1] - a[i]) > 1 or abs(a[i + 1] - a[start]) > 1:
            if (i + 1 - start) > max_len:
                max_len = i + 1 - start
            start = i + 1
    return max_len


def save_the_prisoner(n: int, m: int, s: int) -> int:
    # Jail has #/prisoners and #/treats to pass out. Jailer decides fairest way
    # to divide treats is seat prisoners around circular table in sequentially
    # numbered chairs. Chair number is drain from hat. Beginning with prisoner
    # in that chair, one candy handed to each prisoner sequentially until all
    # distributed. However, last piece of candy looks same but tastes awful.
    # The chair number of that last person should be returned.
    #
    # n = number of prisoners
    # m = number of sweets
    # s = chair number to begin passing out sweets from
    m %= n
    ans = (m + s - 1) % n
    return n if ans == 0 else ans

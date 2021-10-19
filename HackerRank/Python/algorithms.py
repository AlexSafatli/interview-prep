import math


def compare_triplets(a: tuple, b: tuple) -> list:
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
    return rewards


def mini_max_sum(arr: list) -> tuple:
    arr = sorted(arr)  # if sorted, min is first n eles, max is last n eles
    return sum(arr[0:len(arr)-1]), sum(arr[1:len(arr)])


def birthday_cake_candles(candles: list) -> int:
    tallest = max(candles)
    count = 0
    candles.sort()
    for i in range(len(candles)-1, -1, -1):
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

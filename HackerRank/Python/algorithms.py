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

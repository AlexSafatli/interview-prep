# Mergesort implementation; O(nlgn)
def mergesort(li):
    # If a single element, already sorted.
    if len(li) <= 1:
        return
    mid = int((len(li))/2)
    left = li[:mid]
    right = li[mid:]
    mergesort(left)
    mergesort(right)
    merge(li, left, right)


def merge(li, left, right):
    len_left = len(left)
    len_right = len(right)
    i, j, k = 0, 0, 0
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            li[k] = left[i]
            i += 1
        else:
            li[k] = right[j]
            j += 1
        k += 1
    while i < len_left:
        li[k] = left[i]
        i += 1
        k += 1
    while j < len_right:
        li[k] = right[j]
        j += 1
        k += 1


# 8.4, all subsets of a set
def all_subsets_of_a_set(li, index: int):
    # For n > 1, find set of subsets of 1, ..., n+1 then make two copies
    # For one of them, add n to each subset
    if index == len(li):
        return [[]]
    all_subsets = all_subsets_of_a_set(li, index+1)
    subsets = []
    for subset in all_subsets:
        new = []
        new.extend(subset)
        new.append(li[index])
        subsets.append(new)
    all_subsets.extend(subsets)
    return all_subsets


# 8.4, all subsets of a set - combinators/binary strings
def all_subsets_of_a_set_bin(li):
    all_subsets = []
    i = 0  # generate all binary numbers starting with 0
    while i < (1 << len(li)):
        k = i
        index = 0
        subset = []
        while k > 0:
            if (k & 1) > 0:
                subset.append(li[index])
            k >>= 1
            index += 1
        all_subsets.append(subset)
        i += 1
    return all_subsets


# All permutations of a sequence -- see Algorithms notes (1, p. 17)
#
# Pseudocode:
#
#   printperm(P, S)
# 1 if S has 1 element then // base case
# 2   print P followed by the single element of S
# 3 else
# 4   for each element i in S
# 5     printperm((P, i), S-{i})
#
# where P = prefix array of numbers already printed out and
#       S = nonempty set of remaining numbers to be printed
#
# first call is printperm([], {1,2,...,n})
def all_permutations(p, s):
    all_perms = []
    if len(s) == 1:  # base case
        all_perms.append(p + s)
    else:
        for v in s:
            li = []
            li.extend(s)
            li.remove(v)
            all_perms.extend(all_permutations(p + [v], li))
    return all_perms


# 8.5, all valid combinations of n-pairs of pantheses of form "( ... )"
def parantheses(i, r, cnt, str_li, coll):
    if i == 0 and r == 0:
        coll.append(''.join(str_li))
        return  # done
    if i > 0:  # some left "(" to place
        str_li[cnt] = '('
        parantheses(i-1, r, cnt+1, str_li, coll)
    if r > i:
        str_li[cnt] = ')'
        parantheses(i, r-1, cnt+1, str_li, coll)


def all_parantheses_for_n(n: int) -> str:
    li = ['*' for _ in range(2*n)]
    result = []
    parantheses(n, n, 0, li, result)
    return '\n'.join(result)


if __name__ == '__main__':
    arr = [0, 9, 2, 1, 19]
    print('mergesort on ', arr)
    mergesort(arr)
    print(arr)
    all_subsets_bin = sorted(all_subsets_of_a_set_bin(arr))
    all_subsets_rec = sorted(all_subsets_of_a_set(arr, 0))
    print(all_subsets_bin)
    print(all_subsets_rec)
    test_str = 'Dark'
    print(all_permutations([], test_str))
    print(all_parantheses_for_n(3))


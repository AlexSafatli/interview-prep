from stacks_queues import Stack


class TowerOfHanoi(object):
    def __init__(self, label: int):
        self.label = label
        self.disks = Stack()

    def add_disk(self, num: int):
        if len(self.disks) > 0 and self.disks.peek() <= num:
            raise AssertionError('Disk must be placed on larger one')
        self.disks.push(num)

    def remove_top_disk(self) -> int:
        if len(self.disks) == 0:
            return -1
        return self.disks.pop()

    def move_top_disk_to(self, dest):
        disk = self.remove_top_disk()
        if disk == -1:
            raise AssertionError('No top disk found')
        if dest is None:
            raise AssertionError('Need another tower')
        dest.add_disk(disk)
        print('Moved %d from %d to %d.' % (disk, self.label, dest.label))

    def move_n_disks_to(self, n, dest, intermediate):
        if n <= 0:
            return
        self.move_n_disks_to(n - 1, intermediate, dest)
        self.move_top_disk_to(dest)
        intermediate.move_n_disks_to(n - 1, dest, self)

    def __str__(self) -> str:
        return str(self.disks)


# Mergesort implementation; O(nlgn)
def mergesort(li):
    # If a single element, already sorted.
    if len(li) <= 1:
        return
    mid = int((len(li)) / 2)
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
    all_subsets = all_subsets_of_a_set(li, index + 1)
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
        parantheses(i - 1, r, cnt + 1, str_li, coll)
    if r > i:
        str_li[cnt] = ')'
        parantheses(i, r - 1, cnt + 1, str_li, coll)


def all_parantheses_for_n(n: int) -> str:
    li = ['*' for _ in range(2 * n)]
    result = []
    parantheses(n, n, 0, li, result)
    return '\n'.join(result)


# 8.2, Robot in a Grid, Uses dynamic programming top-down memoization approach
def find_path_for_robot_in_a_grid(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    failed_pts = {}
    if find_path(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_pts):
        return path
    return None


def find_path(maze, row: int, col: int, path: list, failed_pts: dict) -> bool:
    # Out of bounds or n/a
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    pt = (row, col)

    # If already visited
    if pt in failed_pts:
        return False

    is_at_origin = row == 0 and col == 0

    # If there is a path from start to here, add location to path
    if is_at_origin or find_path(maze, row, col - 1, path, failed_pts) or \
            find_path(maze, row - 1, col, path, failed_pts):
        path.append((row, col))
        return True

    # Cache failed results
    failed_pts[pt] = True
    return False


# 8.3, Magic index - given sorted array of distinct ints, find i where A[i] = i
def magic_index(li: list, start: int, end: int) -> int:
    if end < start:
        return -1  # not found
    mid = int((start + end) / 2)
    if li[mid] == mid:
        return mid  # found
    elif li[mid] > mid:  # must be on left
        return magic_index(li, start, mid - 1)
    else:  # must be on right
        return magic_index(li, mid + 1, end)


if __name__ == '__main__':
    arr = [0, 9, 2, 1, 19]
    sorted_distinct_arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
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
    print('\n' + '=' * 10 + 'Magic Index' + '=' * 10)
    print(sorted_distinct_arr)
    print(magic_index(sorted_distinct_arr, 0, len(sorted_distinct_arr) - 1))
    print('\n' + '=' * 10 + 'Tower of Hanoi Problem' + '=' * 10)
    towers = [TowerOfHanoi(0), TowerOfHanoi(1), TowerOfHanoi(2)]
    for x in range(4, -1, -1):
        towers[0].add_disk(x)
    towers[0].move_n_disks_to(5, towers[2], towers[1])
    for x in range(0, 3):
        print('Tower:', x, towers[x])
    print('\n' + '=' * 10 + 'Robot in a Grid Problem' + '=' * 10)
    grid = [[True, False, False, True], [True, True, True, True],
            [False, True, True, True]]
    correct_path = find_path_for_robot_in_a_grid(grid)
    print(correct_path)

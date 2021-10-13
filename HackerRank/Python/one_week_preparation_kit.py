class TowerBreakersState(object):
    def __init__(self, n: int, m: int):
        self.towers = [m] * n

    def has_move(self) -> bool:
        for i, x in enumerate(self.towers):
            if x == 1:
                continue
            for y in range(1, x):
                if x % y == 0:
                    self.towers[i] = y
                    return True
        return False


class Caesar(object):
    def __init__(self, s: str):
        self.text = s

    def encrypt(self, n: int):
        # Shift each character by N forward.
        li = []
        for i in self.text:
            if i.isalpha():
                offset = 65 if i.isupper() else 97
                li.append(chr((ord(i) + (n-offset)) % 26 + offset))
            else:
                li.append(i)
        return ''.join(li)


def lonely_integer(li: list) -> int:
    # Given array of integers li, all elements but one occur twice
    ints = {}
    for v in li:
        if v not in ints:
            ints[v] = 1
        else:
            ints[v] += 1
    for v in ints:
        if ints[v] == 1:
            return v
    return -1


def diag_diff(mat: list) -> int:
    # Given square matrix mat, want absolute difference between sum of its diags
    l_diag_sum = 0
    r_diag_sum = 0
    for i in range(0, len(mat)):
        l_diag_sum += mat[i][i]
    for i in range(len(mat)-1, -1):
        r_diag_sum += mat[i][len(mat)-1-i]
    return abs(l_diag_sum-r_diag_sum)


def frequency_arr_0_to_100(li: list) -> list:
    return frequency_arr_generic(li, 100)


def frequency_arr_generic(li: list, max_val: int) -> list:
    freq_arr = [0] * max_val
    for v in li:
        freq_arr[v] += 1
    return freq_arr


def tower_breakers(n: int, m: int) -> int:
    # Resolve a game of Tower Breakers.
    # - Initially there are n towers, each of height m
    # - Player 1/2 move in alternating turns
    # - Ea. turn, pick tower height x red by y (1 <= y < x, y evenly divides x)
    # - If cannot make a move, lose
    # Returns winner player (1 or 2)
    # player = 1
    # state = TowerBreakersState(n, m)
    # while state.has_move():
    #     player = (player % 2) + 1
    # return (player % 2) + 1
    return 2 if n % 2 == 0 or m == 1 else 1


def caesar_encrypt(s: str, k: int) -> str:
    c = Caesar(s)
    return c.encrypt(k)


def grid_challenge(grid: list) -> bool:
    # Given square grid of characters (a-z), rearrange eles of ea row lex (asc)
    # Determine if th ecolumns are also in ascending alpha order (top->bot)
    # Returns true or false
    g = [sorted(list(row)) for row in grid]
    cols = [[row[i] for row in g] for i in range(0, len(g))]
    for col in cols:
        if sorted(col) != col:
            return False
    return True


def new_year_chaos_min_brides(q: list) -> int:
    # Is New Year's Day, people are in line for Wonderland rollercoast ride.
    # Each person wears sticker indicating init. position in queue (1 to n).
    # Any person can bribe person directly in front of them to swap pos, but
    # they still wear the original sticker. One person can bribe at most 2.
    # This function determines the min. #/bribes took place to get to given
    # queue order and whether or not anyone may have bribed more than twice.
    #
    # Example: q = [1,2,3,5,4,6,7,8] -> only 1 required (5 bribed 4)
    # Example: q = [4,1,2,3] -> person 4 bribed 4 ppl -> "Too chaotic"
    #
    # This function returns -1 for "Too chaotic", otherwise #/bribes
    bribes = 0
    if len(q) <= 1:
        return 0
    for i in range(len(q)-1, -1, -1):  # will correct array going backwards
        if i + 1 != q[i]:  # i+1 is initial state expected value
            if i - 1 >= 0 and q[i-1] == i + 1:  # 1-pos bribe
                q[i-1] = q[i]
                q[i] = i
                bribes += 1
            elif i - 2 >= 0 and q[i-2] == i + 1:  # 2-pos bribe
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = i
                bribes += 2
            else:  # illegal move
                return -1
    return bribes


def brackets_are_balanced(s: str) -> bool:
    stack = []  # maintain a stack of brackets
    for sym in s:
        if sym in ['{', '[', '(']:  # opening bracket
            stack.append(sym)  # push
        else:
            if len(stack) > 0:
                peek = stack[-1]
                if peek == '(' and sym == ')':
                    stack.pop()
                elif peek == '[' and sym == ']':
                    stack.pop()
                elif peek == '{' and sym == '}':
                    stack.pop()
                else:
                    return False
            else:
                return False
    return len(stack) == 0


def queue_using_two_stacks(stacks, op: int, ele: str):
    # Process a query of type op with possible ele data
    # Queries:
    #   1 x - Enqueue x into end of queue
    #   2 - Dequeue element at front of queue
    #   3 - Print element at front of queue
    if op == 1:
        stacks[0].append(ele)
    elif op == 2:
        if len(stacks[1]) > 0:
            return stacks[1].pop()
        while len(stacks[0]) > 1:
            stacks[1].append(stacks[0].pop())
        return stacks[0].pop()
    elif op == 3:
        if len(stacks[1]) > 0:
            print(stacks[1][-1])
        else:
            print(stacks[0][0])

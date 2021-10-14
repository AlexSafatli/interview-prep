import heapq
import typing


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


class SinglyLinkedListNode(object):
    def __init__(self, data):
        self.next: typing.Optional[SinglyLinkedListNode] = None
        self.data = data


class HuffmanTreeNode(object):
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


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


class TextEditor(object):
    def __init__(self):
        self.text = ''
        self._edits: typing.List[str] = []

    def append(self, w: str):
        self._edits.append(self.text)
        self.text = ''.join([self.text, w])

    def delete(self, k: int):
        self._edits.append(self.text)
        self.text = self.text[:-k]

    def print(self, k: int):
        print(self.text[k-1])

    def undo(self):
        self.text = self._edits.pop()


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


def diag_diff(mat: typing.List[list]) -> int:
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


def grid_challenge(grid: typing.List[list]) -> bool:
    # Given square grid of characters (a-z), rearrange eles of ea row lex (asc)
    # Determine if th ecolumns are also in ascending alpha order (top->bot)
    # Returns true or false
    g = [sorted(list(row)) for row in grid]
    cols = [[row[i] for row in g] for i in range(0, len(g))]
    for col in cols:
        if sorted(col) != col:
            return False
    return True


def new_year_chaos_min_brides(q: typing.List[int]) -> int:
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


def queue_using_two_stacks(stacks: typing.List[list], op: int, ele: str):
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


def simple_text_editor(ops: typing.List[str]):
    # Perform q number of operations where q =
    #   1. append(W) - append W to end of string
    #   2. delete(k) - delete last k chars of string
    #   3. print(k) - print kth char
    #   4. undo() - undo last op
    # this will take too long if list of ops is long
    editor = TextEditor()
    while len(ops) > 0:
        op = ops[0]
        if len(ops) > 1:
            ops = ops[1:]
        else:
            ops = []
        op_code = int(op[0])
        if op_code == 1:
            editor.append(op[2:])
        elif op_code == 2:
            editor.delete(int(op[2:]))
        elif op_code == 3:
            editor.print(int(op[2:]))
        elif op_code == 4:
            editor.undo()


def lego_blocks():
    # Have an infinite number of 4 types of lego blocks of sizes (depth*h*w):
    #  d  h  w
    #  1  1  1
    #  1  1  2
    #  1  1  3
    #  1  1  4
    #
    # Using these, want to make a wall of height n, width m with features:
    #  - no holes
    #  - one solid structure; no straight vertical break
    #  - bricks must be laid horizontally
    # Want to find out how many ways such a wall can be built mod 10^9+7
    #
    # Example: n, m = 2, 2
    #
    # Have 3 possible configurations:
    # -- ** --
    # -- -- **
    #
    # where * = 1x1 block and -- is a 1x2 block
    #
    # This problem is effectively how to use the 4 types of blocks to solidly
    # cover a h*w rectangle without holes or overlapping.
    #
    # See lego_blocks.pdf in ../Editorials/ for details on the solution.
    mod = 1000000007

    def _pow(a: int, p: int) -> int:
        ans = 1
        while p:
            if p % 2:
                ans = ans * a % mod
            a = a * a % mod
            p = int(p/2)
        return ans

    t = int(input())
    f = [0] * 1111
    g = [0] * 1111

    f[0] = 1
    for i in range(1, 1001):
        for j in range(1, 5):
            if i - j >= 0:
                f[i] = (f[i] + f[i-j]) % mod
    for _ in range(t):
        line = input()
        spl = line.split(' ')
        n, m = int(spl[0]), int(spl[1])
        for i in range(1, m+1):
            g[i] = _pow(f[i], n)
        h = [0] * 1111
        h[1] = 1
        for i in range(2, m+1):
            h[i] = g[i]
            tmp = 0
            for j in range(1, i):
                tmp = (tmp + h[j] * g[i-j]) % mod
            h[i] = (h[i] - tmp + mod) % mod
        print(h[m])


def cookies(k: int, li: typing.List[int]) -> int:
    # Jesse loves cookies, wants sweetness of some cookies to be > k.
    # To do this, two cookies least sweatness repeatedly mixed so that:
    #   sweetness = (1 * least sweet + 2 * 2nd least sweet)
    # This occurs until all cookies have a sweetness >= k
    # k = threshold, li = array of sweetness values
    # returns min. # of operations or -1 if not possible
    heapq.heapify(li)
    num_ops = 0
    while True:
        ls = heapq.heappop(li)
        if ls >= k:
            return num_ops  # sweetness = least sweet
        if len(li) == 0:
            return -1  # not possible (cannot make them uniform sweetness)
        sls = heapq.heappop(li)
        ns = ls + 2*sls
        heapq.heappush(li, ns)
        num_ops += 1


def flipping_matrix(li: list) -> int:
    # Maximum sum of top-left quadrant
    _sum = 0
    n, m = len(li), len(li[0])
    for i in range(0, int(n/2)):
        for j in range(0, int(m/2)):
            cur = li[i][j]
            right = li[i][m-j-1]
            down = li[n-i-1][j]
            diag = li[n-i-1][m-j-1]
            ans = max(cur, right, down, diag)
            _sum += ans
    return _sum


def merge_two_sorted_linked_lists(head1: typing.Optional[SinglyLinkedListNode],
                                  head2: typing.Optional[SinglyLinkedListNode]):
    cursor3 = None
    new_list_head = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    cursor1 = head1
    cursor2 = head2
    while cursor1 is not None or cursor2 is not None:
        compare = None
        if cursor1 is not None:
            compare = cursor1.data if compare is None else min(cursor1.data,
                                                               compare)
        if cursor2 is not None:
            compare = cursor2.data if compare is None else min(cursor2.data,
                                                               compare)
        if compare is not None:
            if cursor1 is not None and compare == cursor1.data:
                cursor1 = cursor1.next
            elif cursor2 is not None and compare == cursor2.data:
                cursor2 = cursor2.next
            if new_list_head is None:
                new_list_head = SinglyLinkedListNode(compare)
                cursor3 = new_list_head
            else:
                cursor3.next = SinglyLinkedListNode(compare)
                cursor3 = cursor3.next
    return new_list_head


def decode_huffman(root: HuffmanTreeNode, s: str) -> str:
    ans = ''
    cursor = root
    for i in range(0, len(s)):
        if s[i] == '0':
            cursor = cursor.left
        else:
            cursor = cursor.right
        if cursor.left is None and cursor.right is None:  # leaf node
            ans += cursor.data
            cursor = root
    return ans

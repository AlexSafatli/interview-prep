ASCII_ALPHABET_LEN = 128
NUMBER_HOUSES = 8


# Have N number of houses in a straight line where every passing day each cell
# is analyzed for its active/inactive state based on its neighbors
class HousesState:
    def __init__(self, states: list):
        self.houses = [-1] * NUMBER_HOUSES
        for i in range(len(states)):
            if i >= NUMBER_HOUSES:
                break
            self.houses[i] = states[i]

    def pass_day(self):
        new_houses = [state for state in self.houses]
        start, end = 0, NUMBER_HOUSES - 1

        # Update all states simultaneously
        for i in range(NUMBER_HOUSES):
            # Check for left edge
            if i == start and self.houses[2] == 0:
                new_houses[i] = 0
            # Check for right edge
            elif i == end and self.houses[NUMBER_HOUSES-2] == 0:
                new_houses[i] = 0
            # Both inactive or active
            elif i != start and i != end and \
                    self.houses[i + 1] == self.houses[i - 1]:
                new_houses[i] = 0
            else:
                new_houses[i] = 1

        self.houses = new_houses
        return self.houses

    def pass_days(self, num_days=1):
        for _ in range(num_days):
            self.pass_day()
        return self.houses


def is_unique_characters_bool_arr(s: str) -> bool:
    # assume 128-character (ASCII) alphabet
    if len(s) > ASCII_ALPHABET_LEN:
        return False
    found_chars = [False for _ in range(ASCII_ALPHABET_LEN)]
    for char in s:
        if found_chars[ord(char)]:
            return False  # already found
        found_chars[ord(char)] = True
    return True


def is_unique_characters(s: str) -> bool:
    # use a bitvector; assumes a->z
    bitvector: int = 0
    for char in s:
        val: int = ord(char) - ord('a')
        if bitvector & (1 << val) > 0:
            return False
        bitvector |= 1 << val
    return True


def is_unique_characters_sorting_str(s: str) -> bool:
    # no other data structure, sort str in place, O(n^2)
    if len(s) < 2:
        return True
    s = sorted(s)
    for i in range(0, len(s)):
        for k in range(i+1, len(s)-1):
            if s[i] == s[k]:
                return False
    return True


def are_permutations(x, y) -> bool:
    # works as long as x, y have and a size/are sortable - intended for strings
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)


def are_permutations_char_counts(x, y) -> bool:
    # uses item counts, assumes x, y iterable
    if len(x) != len(y):
        return False
    found_map = {}
    for item in x:
        if item in found_map:
            found_map[item] += 1
        else:
            found_map[item] = 1
    for item in y:
        if item in found_map:
            found_map[item] -= 1
            if found_map[item] < 0:
                return False
        else:
            return False
    return True


def transpose_square_matrix_in_place(mat):
    # Only consider upper triangle
    for n in range(0, len(mat)-1):
        for m in range(n+1, len(mat)):
            # swap mat[m][n] with mat[n][m]
            mat[m][n], mat[n][m] = mat[n][m], mat[m][n]


# Testing Function
def call_one_arg_func(f, s: str):
    print('%s(%s):' % (f.__name__, s), f(s))


# Testing Function
def call_two_arg_func(f, x, y):
    print('%s(%s,%s):' % (f.__name__, x, y), f(x,y))


# Testing Function
def print_square_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], ' ', end='')
        print()


if __name__ == '__main__':
    print('== Unique Characters ==')
    test_strs = ['balance', 'red', 'magic', 'magical']
    for test_str in test_strs:
        for func in [is_unique_characters_sorting_str, is_unique_characters,
                     is_unique_characters_bool_arr]:
            call_one_arg_func(func, test_str)
    print('\n== Permutations ==')
    test_strs = ['dog', 'god', 'dog ', 'God']
    for test_str in test_strs:
        for test_str2 in test_strs:
            if test_str != test_str2:
                for func in [are_permutations, are_permutations_char_counts]:
                    call_two_arg_func(func, test_str, test_str2)
    print('\n==Tranpose==')
    mat = [[0, 1, 2, 8], [5, 4, 3, 3], [9, 2, 1, 6], [7, 2, 1, 9]]
    print_square_matrix(mat)
    transpose_square_matrix_in_place(mat)
    print()
    print_square_matrix(mat)
    print()
    print('\n==Houses==')
    states_1 = [1, 0, 0, 0, 0, 1, 0, 0]
    states_2 = [1, 1, 1, 0, 1, 1, 1, 1]
    houses_1 = HousesState(states_1)
    houses_2 = HousesState(states_2)
    print(states_1, '->', houses_1.pass_day())
    print(states_2, '->', houses_2.pass_days(2))

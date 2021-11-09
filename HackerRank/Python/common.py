def all_permutations(p, s):
    if len(s) == 1:
        return [p + s]
    perms = []
    for v in s:
        li = [_ for _ in s]
        li.remove(v)
        perms.extend(all_permutations(p + [v], li))
    return perms


def all_permutations_of_1_to_9():
    return all_permutations([], list(range(1, 10)))


def rows_are_magic(sq: list, c: int) -> bool:
    for i in range(len(sq)):
        s = 0
        for j in range(len(sq)):
            s += sq[i][j]
        if s != c:
            return False
    return True


def cols_are_magic(sq: list, c: int) -> bool:
    for i in range(len(sq)):
        s = 0
        for j in range(len(sq)):
            s += sq[j][i]
        if s != c:
            return False
    return True


def dia_are_magic(sq: list, c: int) -> bool:
    # L-to-R
    s = 0
    for i in range(len(sq)):
        s += sq[i][i]
    if s != c:
        return False
    # R-to-L
    s = 0
    for i in range(len(sq)):
        s += sq[i][-(i + 1)]
    return s == c


def is_magic_square(sq: list) -> bool:
    c = sum([i for i in sq[0]])
    return all([rows_are_magic(sq, c),
                cols_are_magic(sq, c),
                dia_are_magic(sq, c)])


def all_magic_squares_for_3_by_3():
    all_magic = []
    all_perms = all_permutations_of_1_to_9()
    for perm in all_perms:
        c = perm[0] + perm[3] + perm[6]
        sq = [[], [], []]
        for i in range(0, 3):
            sq[0].append(perm[i])
        for i in range(3, 6):
            sq[1].append(perm[i])
        for i in range(6, 9):
            sq[2].append(perm[i])
        if all([rows_are_magic(sq, c),
                cols_are_magic(sq, c),
                dia_are_magic(sq, c)]):
            all_magic.append(perm)
    return all_magic

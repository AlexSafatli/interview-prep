# http://www.dsalgo.com/2013/02/gold-coins-in-pots-game.html

def number_of_coins(pots) -> int:
    outcomes = [[None for _ in range(0, len(pots))] for _ in
                range(0, len(pots))]
    return max_coins(pots, 0, len(pots) - 1, outcomes)


def max_coins(pots, lo, up, f) -> int:
    if lo > up:
        return 0
    if f[lo][up] is not None:
        return f[lo][up]

    def _max_coins(i, j):
        return max_coins(pots, i, j, f)

    start = pots[lo] + min([_max_coins(lo + 2, up), _max_coins(lo + 1, up - 1)])
    end = pots[up] + min([_max_coins(lo, up - 2), _max_coins(lo + 1, up - 1)])
    f[lo][up] = max([start, end])
    return f[lo][up]


if __name__ == '__main__':
    gold_pots = [12, 32, 4, 23, 6, 42, 16, 3, 85, 23, 4, 7, 3, 5, 45, 34, 2, 1]
    print(gold_pots, number_of_coins(gold_pots))

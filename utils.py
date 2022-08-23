import random


def rand_n(n: int) -> int:
    return random.randint(0, n-1)


def rand_idx(n: int, m: int) -> (int, int):
    return rand_n(n), rand_n(m)


def rand_idx_except(n: int, m: int, except_x: [int], except_y: [int]) -> (int, int):
    x, y = rand_idx(n, m)
    while x in except_x and y in except_y:
        x, y = rand_idx(n, m)
    return x, y

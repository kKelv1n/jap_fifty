import random


def rand_n(n: int) -> int:
    return random.randint(0, n-1)


def rand_idx(n: int, m: int) -> (int, int):
    return rand_n(n), rand_n(m)


def rand_idx_exclude(n: int, m: int, exclude_x: [int], exclude_y: [int]) -> (int, int):
    x, y = rand_idx(n, m)
    while x in exclude_x and y in exclude_y:
        x, y = rand_idx(n, m)
    return x, y

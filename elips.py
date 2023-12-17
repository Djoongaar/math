from typing import List


def get_y(x, a, b, mod):
    result = (x**3 + a * x + b)%mod
    print(result)
    return result


def sum_same_points(x: int, y: int, a: int, mod:int) -> List[int]:
    # P=(0,2), a=-3
    bon = 0
    while True:
        cisl = (3 * x ** 2 + a) + bon
        c = cisl / (2 * y)
        if c == int(c):
            break

        bon += mod

    x3 = c ** 2 - 2 * x
    y3 = c * (x - x3) - y
    print([x3, y3])
    return [x3, y3]


def sum_points(x1: int, y1: int, x2:int, y2:int, mod:int):
    # P=(0,2), a=-3
    bon = 0
    while True:
        cisl = (y2 - y1) + bon
        c = cisl / (x2 - x1)
        if c == int(c):
            break

        bon += mod

    x3 = c**2 - x1 - x2
    y3 = c * (x1 - x3) - y1

    print([x3%mod, y3%mod])
    return [x3, y3]


# sum_same_points(x=0, y=2, a=-3, mod=7)
# sum_points(x1=5, y1=3, x2=5, y2=-3, mod=7)
# P1 (0, 2)
# P2 (1, -3)
# P3 (3, -1)
# P4 ()
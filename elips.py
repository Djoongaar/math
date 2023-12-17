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



    while True:
        min = 1
        if x3<0:
            min = -1
        x3 = x3-mod*(min)
        if -5<=x3<=4:
            break
    while True:
        min = 1
        if y3 < 0:
            min = -1
        y3 = y3 - mod * (min)
        if -5<=y3<=5:
            break


    print([x3, y3])
    return [x3, y3]


# sum_same_points(x=0, y=5, a=-2, mod=11)
sum_points(x1=0, y1=5, x2=-3, y2=-2, mod=11)
# P1 (0, 2)
# P2 (1, -3)
# P3 (3, -1)
# P4 ()
# from typing import List
#
#
# def get_y(x, a, b, mod):
#     result = (x**3 + a * x + b)%mod
#     print(result)
#     return result
#
#
# def sum_same_points(x: int, y: int, a: int, mod:int) -> List[int]:
#     # P=(0,2), a=-3
#     bon = 0
#     while True:
#         cisl = (3 * x ** 2 + a) + bon
#         c = cisl / (2 * y)
#         if c == int(c):
#             break
#
#         bon += mod
#
#     x3 = c ** 2 - 2 * x
#     y3 = c * (x - x3) - y
#     print([x3, y3])
#     return [x3, y3]


# def sum_points(x1: int, y1: int, x2:int, y2:int, mod:int):
#     # P=(0,2), a=-3
#     bon = 0
#     while True:
#         cisl = (y2 - y1) + bon
#         c = cisl / (x2 - x1)
#         if c == int(c):
#             break
#
#         bon += mod
#
#     x3 = c**2 - x1 - x2
#     y3 = c * (x1 - x3) - y1
#
#
#
#     while True:
#         min = 1
#         if x3<0:
#             min = -1
#         x3 = x3-mod*(min)
#         if -5<=x3<=4:
#             break
#     while True:
#         min = 1
#         if y3 < 0:
#             min = -1
#         y3 = y3 - mod * (min)
#         if -5<=y3<=5:
#             break
#
#
#     print([x3, y3])
#     return [x3, y3]


# sum_same_points(x=0, y=5, a=-2, mod=11)
# sum_points(x1=0, y1=5, x2=4, y2=2, mod=11)
# P1 (0, 2)
# P2 (1, -3)
# P3 (3, -1)
# P4 ()
# #

data_x_and_y = []

x1 = int(input("Введите х1:   "))
y1 = int(input("Введите у1:   "))
# x2 = int(input("Введите х2:   "))
# y2 = int(input("Введите у2:   "))
mod = int(input("Введите mod:   "))
a = int(input("Введите a:   "))
data_x_and_y_new = []
max_porog_x = int(input("Введите max х:   "))
min_porog_x = int(input("Введите  min х:   "))
max_porog_y = int(input("Введите max y:   "))
min_porog_y = int(input("Введите  min y:   "))
print("      x      y                           ")
print(f"1P = ({float(x1)}, {float(y1)} )")
def sum_points(x1, y1, a, mod):
    bon = 0
    cheker = 3
##################################################
    bon = 0
    while True:
        cisl = (3 * x1 ** 2 + a) + bon
        c = cisl / (2 * y1)
        if c == int(c):
            break

        bon += mod
    data_1 = []
    x3 = c ** 2 - 2 * x1
    y3 = c * (x1 - x3) - y1
    while True:
        min = 1
        if x3 < 0:
            min = -1
        x3 = x3 - mod * (min)
        if min_porog_x <= x3 <= max_porog_x:
            break
    while True:
        min = 1
        if y3 < 0:
            min = -1
        y3 = y3 - mod * (min)
        if min_porog_y <= y3 <= max_porog_y:
            break


    data_1.append(str(x3))
    data_1.append(str(y3))
    x2, y2 = x3, y3

    print(f"2P = ({', '.join(data_1)})")
#################################################
    while True:
        data = []
        while True:

            cisl = (y2 - y1) + bon
            if cisl == 0 or (x2 - x1)==0:
                return data_x_and_y_new
            c = cisl / (x2 - x1)
            if c == int(c):
                break

            bon += mod

        x3 = c ** 2 - x1 - x2
        y3 = c * (x1 - x3) - y1
        while True:
            min = 1
            if x3 < 0:
                min = -1
            x3 = x3 - mod * (min)
            if min_porog_x <= x3 <= max_porog_x:
                break
        while True:
            min = 1
            if y3 < 0:
                min = -1
            y3 = y3 - mod * (min)
            if min_porog_y <= y3 <= max_porog_y:
                break
        data.append(str(x3))
        data.append(str(y3))

        data_x_and_y_new.append(data)
        print(f"{cheker}P = ({', '.join(data)})")
        x2, y2 = x3, y3
        cheker+=1
    return data_x_and_y_new


data_x_and_y_new = sum_points(x1, y1, a, mod)
# print(data_x_and_y_new)

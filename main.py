import math
from typing import List


def check_gcd(index: int) -> List[int]:
    # Все элементы кольца
    Z = [i for i in range(index)]
#############################################33333
    # Наибольшие общие делители
    all_gcd = [1]

    for ni in Z[2:]:
        gcd = math.gcd(ni, index)
        if gcd == 1:
            all_gcd.append(ni)
            print(f"НОД({ni},{index}) = {gcd},следовательно {ni} ∈  ℤ*{index} ")
        else:
            print(f"НОД({ni},{index}) = {gcd},следовательно {ni} ∉  ℤ*{index} ")
    print()
    print(f"Группа обратимых элементов кольца классов вычетов по модулю {index} имеет следующий вид:")
    print(f"ℤ*{index} = {set(Z)}")
    return all_gcd


index = int(input("index = "))
all_gcd = check_gcd(index)

print(f"Данное кольцо классов вычетов состоит из {index} элементов")
print()
print(f"Может быть записано следующим образом: ")
print(f"ℤ15 = {set(all_gcd)}")
print()

result = {}

for number, divider in enumerate(all_gcd):
    Hz = [1]
    degree = 1

    while True:
        H = (divider ** degree) % index
        degree += 1

        if H == 1:
            break

        if H in all_gcd:
            Hz.append(H)

    print(f'H{number+1} = 〈 {divider} 〉 = \u007B {", ".join([str(i) for i in Hz])} \u007D')
    print(f'O 〈 {divider} 〉 = {degree - 1}')


print('----------------------------------------------------------------')
print('FINAL')
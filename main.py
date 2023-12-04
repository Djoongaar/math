import math

n= int(input("n = "))
Zgcd = ['1']
Zn = [ str(i) for i in range(n)]

print(f"Данное кольцо классов вычетов состоит из {n} элементов")
print()
print(f"Может быть записано следующим образом: ")
print(f"ℤ15 = \u007B {', '.join(Zn) } \u007D")
print()
def gcd_check(Zgcd,Zn,n):
    for ni in range(2,len(Zn)):
        gcd = math.gcd(ni, n)
        if gcd==1:
            Zgcd.append(Zn[ni])
            print(f"НОД({ni},{n}) = {gcd},следовательно {Zn[ni]} ∈  ℤ*{n} ")

        else:

            print(f"НОД({ni},{n}) = {gcd},следовательно {Zn[ni]} ∉  ℤ*{n} ")

    print()
    print(f"Группа обратимых элементов кольца классов вычетов по модулю {n} имеет следующий вид:")
    print(f"ℤ*{n} = \u007B {', '.join(Zgcd) } \u007D")
    return Zgcd
Zgcd = gcd_check(Zgcd,Zn,n)

print()

for i in range(len(Zgcd)):
    Hz = ["1"]
    coint = 1
    while True:
        H = (int(Zgcd[i])  coint) % n
        coint += 1

        if H == 1:
            break

        if str(H) in Zn:
            Hz.append(str(H))

    print(f'H{i+1} = 〈 {Zgcd[i]} 〉 = \u007B {", ".join(Hz)} \u007D')
    print(f'O 〈 {Zgcd[i]} 〉 = {coint - 1}')

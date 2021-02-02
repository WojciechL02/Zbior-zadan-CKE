"""
zadanie 59, zbiór zadań CKE
"""


def rozklad(n):
    czynniki = []
    k = 1
    while k < n ** (1 / 2):
        k += 1
        while n % k == 0:
            czynniki.append(k)
            n /= k
    if n != 1:
        czynniki.append(int(n))
    return czynniki



def iloczyn_cyfr(n):
    iloczyn = 1
    while n > 0:
        iloczyn *= n % 10
        n = n // 10
    return iloczyn


def moc(n):
    ile = 1
    n = iloczyn_cyfr(n)
    while n > 9:
        n = iloczyn_cyfr(n)
        ile += 1
    return ile


licznik1 = 0
licznik2 = 0
tablica3 = []
for i in range(9):
    tablica3.append(0)
max3 = 0
min3 = 999999999
with open("liczby.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        # 59.1
        r = set(rozklad(int(L)))
        if len(r) == 3 and 2 not in r:
            licznik1 += 1
        # 59.2
        a = str(int(L) + int(L[::-1]))
        if a == a[::-1]:
            licznik2 += 1
        # 59.3
        for N in range(1, 9):
            if moc(int(L)) == N:
                tablica3[N] += 1
        if moc(int(L)) == 1:
            if int(L) < min3:
                min3 = int(L)
            if int(L) > max3:
                max3 = int(L)


with open("wyniki_liczby.txt", "w") as odp:
    odp.write("59.1\n" + str(licznik1))
    odp.write("\n\n59.2\n" + str(licznik2))
    odp.write("\n\n59.3\n" + "Ilość liczb w kolejności (1-8): ")
    for i in range(1, 9):
        odp.write(str(tablica3[i]) + "  ")
    odp.write(" \n" + "max: " + str(max3) + "\n" +
              "min: " + str(min3))
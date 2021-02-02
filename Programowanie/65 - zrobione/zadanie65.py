"""
zadanie 65, zbiór zadań CKE
"""


def rozklad(n):
    czynniki = []
    k = 2
    while int(n) != 1:
        while int(n) % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki


def NWD(x, y):
    while y != 0:
        x, y = y, x % y
    return x



# ---------------DANE--------------- #
dane = []
with open("dane_ulamki.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        L = L.split(" ")
        dane.append(L)
# ---------------------------------- #

# 65.1
min1 = 100000000
para1 = ""
for P in dane:
    if int(P[0]) / int(P[1]) < min1:
        min1 = int(P[0]) / int(P[1])
        para1 = P[0] + " " + P[1]

# 65.2
licznik2 = 0
for Q in dane:
    pom = []
    czyn1 = set(rozklad(int(Q[0])))
    czyn2 = set(rozklad(int(Q[1])))
    i = len(czyn1)
    for j in czyn1:
        if j not in czyn2:
            pom.append(j)
    if len(pom) == i:
        licznik2 += 1

# 65.3
nowe_dane = []
suma3 = 0
for M in dane:
    x = int(M[0])
    y = int(M[1])
    d = NWD(x, y)
    if d == 1:
        nowe_dane.append(M)
    if d != 1:
        p = [str(x//d), str(y//d)]
        nowe_dane.append(p)
for L in nowe_dane:
    suma3 += int(L[0])

# 65.4

suma4 = 0
b = 4 * 9 * 25 * 49 * 13
for H in dane:
    i = b // int(H[1])
    w = int(H[0]) * i
    suma4 += w


with open("wyniki_ulamki.txt", "w") as odp:
    odp.write("65.1\n" + str(para1))
    odp.write("\n\n65.2\n" + str(licznik2))
    odp.write("\n\n65.3\n" + str(suma3))
    odp.write("\n\n65.4\n" + str(suma4))

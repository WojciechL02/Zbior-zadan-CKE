"""
zadanie 76, zbiór zadań CKE
"""


def szyfr1(s, P):
    jawny = list(s)
    for i in range(len(s)):
        k = P[i % len(P)] - 1
        jawny[i], jawny[k] = jawny[k], jawny[i]
    szyfr = ""
    for l in jawny:
        szyfr += l
    return szyfr


def deszyfr(s, P):
    napis = list(s)
    for i in range(len(napis)-1, -1, -1):
        k = P[i % len(P)] - 1
        napis[i], napis[k] = napis[k], napis[i]
    szyfr = ""
    for l in napis:
        szyfr += l
    return szyfr


# 76.1
dane1 = []
odp1 = ""
with open("szyfr1.txt", "r") as plik1:
    for w in plik1:
        w = w.strip()
        dane1.append(w)
klucz1 = dane1[6].split(" ")
klucz1 = [int(x) for x in klucz1]
for j in range(6):
    odp1 += f'{szyfr1(dane1[j], klucz1)}\n'


# 76.2
dane2 = []
with open("szyfr2.txt", "r") as plik2:
    for w in plik2:
        w = w.strip()
        dane2.append(w)
klucz2 = dane2[1].split(" ")
klucz2 = [int(x) for x in klucz2]
odp2 = f'{szyfr1(dane2[0], klucz2)}'


# 76.3
dane3 = []
odp3 = ""
with open("szyfr3.txt", "r") as plik3:
    for L in plik3:
        dane3.append(L.strip())
napis3 = dane3[0]
odp3 = deszyfr(napis3, [6, 2, 4, 1, 5, 3])


with open("wyniki_szyfr1.txt", "w") as odpw1:
    odpw1.write(odp1)
with open("wyniki_szyfr2.txt", "w") as odpw2:
    odpw2.write(odp2)
with open("wyniki_szyfr3.txt", "w") as odpw3:
    odpw3.write(odp3)
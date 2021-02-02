"""
zadanie 69, zbiór zadań CKE
"""


def geny(n):
    gen = []
    m = n
    while len(m) > 0:
        if "AA" in m:
            ip = m.find("AA")
        else:
            return gen
        if "BB" in m:
            ik = m.find("BB") + 2
        else:
            return gen
        if len(m[ip:ik]) > 0:
            gen.append(m[ip:ik])
        m = m[ik:]
    return gen


def geny_odwr(n):
    gen1 = []
    m = n[::-1]
    while len(m) > 0:
        if "AA" in m:
            ip = m.find("AA")
        else:
            return gen1
        if "BB" in m:
            ik = m.find("BB") + 2
        else:
            return gen1
        if len(m[ip:ik]) > 0:
            gen1.append(m[ip:ik])
        m = m[ik:]
    return gen1


def odpornosc(n, m):
    ok = True
    j = 0
    if len(n) != len(m):
        ok = False
        return ok
    while j < len(n):
        if n[j] != m[j]:
            ok = False
            break
        j += 1
    return ok


# ---------------DANE--------------- #
dane = []
gatunki = []
with open("dane_geny.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        dane.append(L)
        if len(L) not in gatunki:
            gatunki.append(len(L))
# ---------------------------------- #

# 69.1
max1 = 0
for G in gatunki:
    il = 0
    for C in dane:
        if G == len(C):
            il += 1
    if il > max1:
        max1 = il

# 69.2
licznik2 = 0
geny_os = []
for O in dane:
    geny_os.append(geny(O))

for L in geny_os:
    for P in L:
        if "BCDDC" in P:
            licznik2 += 1

# 69.3
il_genow = 0
dl_max = 0
for K in geny_os:
    if len(K) > il_genow:
        il_genow = len(K)
    for R in K:
        if len(R) > dl_max:
            dl_max = len(R)

# 69.4
geny_os_odwr = []
odporni = 0
silnie_odp = 0
for T in dane:
    geny_os_odwr.append(geny_odwr(T))

i = 0
while i < len(geny_os):
    if dane[i] == dane[i][::-1]:
        silnie_odp += 1
    if odpornosc(geny_os[i], geny_os_odwr[i]):
        odporni += 1
    i += 1


with open("wyniki_gen.txt", "w") as odp:
    odp.write("69.1\n" + "Ilość gatunków: " + str(len(gatunki)) + "\n" +
              "Najwięcej dla jednego gatunku: " + str(max1))
    odp.write("\n\n69.2\n" + str(licznik2))
    odp.write("\n\n69.3\n" + "Największa ilość genów: " + str(il_genow) + "\n" +
              "Długość najdłuższego genu: " + str(dl_max))
    odp.write("\n\n69.4\n" + "Liczba odpornych: " + str(odporni) + "\n" +
              "Liczba silnie odpornych: " + str(silnie_odp))
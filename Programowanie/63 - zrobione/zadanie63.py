"""
zadanie 63, zbiór zadań CKE
"""


def dwucykliczny(n):
    if len(n) % 2 != 0:
        return False
    p = int(len(n) / 2)
    if n[:p] == n[p:]:
        return True


def nie_kolo_siebie(n):
    ok = True
    i = 0
    while i < len(n) - 1:
        if n[i] == "1" and n[i+1] == "1":
            ok = False
            break
        i += 1
    return ok


def rozklad(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki


tablica1 = []
licznik2 = 0
licznik3 = 0
min3 = 262143
max3 = 0
with open("ciagi.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        # 63.1
        if dwucykliczny(L):
            tablica1.append(L)
        # 63.2
        if nie_kolo_siebie(L):
            licznik2 += 1
        # 63.3
        l_dzies = int(L, 2)
        if len(rozklad(l_dzies)) == 2:
            licznik3 += 1
            if l_dzies < min3:
                min3 = l_dzies
            if l_dzies > max3:
                max3 = l_dzies

with open("wyniki_ciagi.txt", "w") as odp:
    odp.write("63.1\n")
    for C in tablica1:
        odp.write(C + "\n")
    odp.write("\n63.2\n" + str(licznik2))
    odp.write("\n\n63.3\n" + "Ilość półpierwszych: " + str(licznik3) + "\n" +
              "Najmniejsza: " + str(min3) + "\n" +
              "Największa: " + str(max3))
"""
zadanie 74, zbiór zadań CKE
"""


def same_cyfry(n):
    ok = True
    for Z in n:
        if Z not in cyfry:
            ok = False
            break
    return ok


def cztery_kolejne_znaki(n):
    ok = False
    i = 0
    while i < len(n) - 3:
        tab = [ord(n[i]), ord(n[i+1]), ord(n[i+2]), ord(n[i+3])]
        tab.sort()
        if tab[0] - tab[1] == -1 and tab[1] - tab[2] == -1 and tab[2] - tab[3] == -1:
            ok = True
            break
        i += 1
    return ok


def warunki_hasel(n):
    ok1 = False
    ok2 = False
    ok3 = False
    for L in n:
        if L in cyfry:
            ok1 = True
        elif ord(L) in range(97, 123):
            ok2 = True
        elif ord(L) in range(65, 91):
            ok3 = True
    if ok1 and ok2 and ok3:
        return True
    else:
        return False


dane = []
cyfry = ["0","1","2","3","4","5","6","7","8","9"]
licznik1 = 0
odp2 = []
uzyte2 = []
licznik3 = 0
licznik4 = 0
with open("hasla.txt", "r") as plik:
    for H in plik:
        H = H.strip()
        dane.append(H)
        # 74.1
        if same_cyfry(H):
            licznik1 += 1
        # 74.3
        if cztery_kolejne_znaki(H):
            licznik3 += 1
        # 74.4
        if warunki_hasel(H):
            licznik4 += 1

# 74.2
for S in dane:
    if dane.count(S) >= 2:
        if S not in uzyte2:
            uzyte2.append(S)
            odp2.append(S)
odp2.sort()

with open("wyniki_hasla.txt", "w") as odp:
    odp.write("74.1\n" + str(licznik1))
    odp.write("\n\n74.2\n")
    k = 0
    while k < len(odp2):
        odp.write(odp2[k] + "\n")
        k += 1
    odp.write("\n74.3\n" + str(licznik3))
    odp.write("\n\n74.4\n" + str(licznik4))
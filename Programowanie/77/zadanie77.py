"""
zadanie 77, zbiór zadań CKE
"""

# ZROBIONE TYLKO 77.1, OGARNIJ SZYFROWANIE I NAPISZ SAM

def szyfr_litery(litera, klucz):
    l = 0
    k = ord(klucz) - 65
    if litera in [" ", ",", "."]:
        return litera
    else:
        l = ord(litera) + k
    if l > 90:
        l -= 26
    return chr(l)


def szyfr_slowa(slowo, klucz):
    slowo = list(slowo)
    szyfr = ""
    klucz = list(klucz)
    i = 0
    for l in slowo:
        szyfr += szyfr_litery(l, klucz[i % len(klucz)])
        if l not in [" ", ",", "."]:
            i += 1
    return szyfr


# --------------- DANE --------------- #
dane_dokad = ""
with open("dokad.txt", "r") as plik1:
    for T in plik1:
        dane_dokad += T.strip()

dane_szyfr = []
with open("szyfr.txt", "r") as plik2:
    for line in plik2:
        dane_szyfr.append(line.strip())
# ------------------------------------ #

# 77.1
klucz = "LUBIMYCZYTAC"
zad1 = szyfr_slowa(dane_dokad, klucz)
dl = 0
for z in dane_dokad:
    if z not in [" ", ",", "."]:
        dl += 1
zad1_powtorzenia = int(dl/len(klucz)) + 1


with open("Vigenere_wyniki.txt", "w") as odp:
    odp.write("77.1\n" + zad1 + "\n" + str(zad1_powtorzenia))
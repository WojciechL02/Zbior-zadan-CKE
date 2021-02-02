"""
zadanie 68, zbiór zadań CKE
"""


def jednolity_anagram(a, b):
    ok = True
    if a != b:
        ok = False
        return ok
    if a.count(a[0]) != len(a):
        ok = False
        return ok
    return ok


def anagramy(a, b):
    ok = True
    if len(a) != len(b):
        ok = False
        return ok
    for L in a:
        if a.count(L) != b.count(L):
            ok = False
            return ok
    return ok


# ---------------DANE--------------- #
dane = []
with open("dane_napisy.txt", "r") as plik:
    for P in plik:
        P = P.strip()
        dane.append(P.split(" "))
# ---------------------------------- #

# 68.1
licznik1 = 0
for P in dane:
    if jednolity_anagram(P[0], P[1]):
        licznik1 += 1

# 68.2
licznik2 = 0
for S in dane:
    if anagramy(S[0], S[1]):
        licznik2 += 1

# 68.3
dane3 = []
licznik3 = 0
for L in dane:
    for S in L:
        dane3.append(S)

max3 = 0
i = 0
while i < len(dane3):
    j = 0
    najw = 1
    while j < len(dane3):
        if i != j:
            if anagramy(dane3[i], dane3[j]):
                najw += 1
            else:
                if najw > max3:
                    max3 = najw
        j += 1
    i += 1

with open("wyniki_anagramy.txt", "w") as odp:
    odp.write("68.1\n" + str(licznik1))
    odp.write("\n\n68.2\n" + str(licznik2))
    odp.write("\n\n68.3\n" + str(max3))
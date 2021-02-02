"""
zadanie 61, zbiór zadań CKE
"""


def ciag_artym(n):
    ok = True
    r = int(n[1]) - int(n[0])
    for i in range(1, len(n)):
        if int(n[i]) - int(n[i-1]) != r:
            ok = False
            break
    return ok


def najw_szescian(n):
    max = 0
    for L in n:
        for i in range(1, 101):
            if (pow(i, 3)) == int(L):
                if int(L) > max:
                    max = int(L)
    return max


def bledny_wyraz(n):
    tab = ""
    r = []
    for i in range(4):
        r.append(int(n[i+1]) - int(n[i]))
    if r[0] != r[1] and r[1] == r[2]:
        tab += n[0] + " "
        return tab
    if r[0] != r[1] and r[1] != r[2] and r[2] == r[3]:
        tab += n[1] + " "
        return tab
    j = 0
    while j <= len(n) - 1:
        if int(n[j+1]) - int(n[j]) != int(r[0]):
            tab += n[j+1] + " "
            return tab
        j += 1


# ----------------DANE--------------- #
tablica = []
tablica1 = []
dane1 = []
dane2 = []
with open("ciagi.txt", "r") as plik1:
    for C in plik1:
        C = C.strip()
        tablica.append(C)
with open("bledne.txt", "r") as plik2:
    for G in plik2:
        G = G.strip()
        tablica1.append(G)
i = 1
while i <= 200:
    dane1.append(tablica[i].split(" "))
    i += 2
j = 1
while j <= 40:
    dane2.append(tablica1[j].split(" "))
    j += 2
# ----------------------------------- #

# 61.1
licznik1 = 0
max_r = 0
for N in dane1:
    if ciag_artym(N):
        licznik1 += 1
        r = int(N[1]) - int(N[0])
        if r > max_r:
            max_r = r
# 61.2
tablica2 = []
for M in dane1:
    a = najw_szescian(M)
    if a != 0:
        tablica2.append(a)

# 61.3
odp3 = []
for K in dane2:
    odp3.append(bledny_wyraz(K))


with open("wyniki61.txt", "w") as odp:
    odp.write("61.1\n" + str(licznik1) + "\n" + "max_r: " + str(max_r))
    odp.write("\n\n61.2\n")
    for i in range(len(tablica2)):
        odp.write(str(tablica2[i]) + "\n")
    odp.write("\n\n61.3\n")
    for k in range(len(odp3)):
        odp.write(str(odp3[k]) + "\n")
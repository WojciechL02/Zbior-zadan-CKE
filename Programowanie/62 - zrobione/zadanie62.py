"""
zadanie 62, zbiór zadań CKE
"""


liczby1 = []    # ósemkowe
liczby2 = []    # dziesiętne
liczby2w8 = []
max = "0"
min = "777777"
with open("liczby1.txt", "r") as plik1:
    for L in plik1:
        L = L.strip()
        liczby1.append(L)
        # 62.1
        if int(L, 8) > int(max, 8):
            max = L
        if int(L, 8) < int(min, 8):
            min = L


with open("liczby2.txt", "r") as plik2:
    for N in plik2:
        N = N.strip()
        liczby2.append(N)

# 62.2
max_dl = 0
max_liczba = 0
i = 0
j = 1
dl = 1
while i <= 998 and j <= 999:
    if int(liczby2[i]) <= int(liczby2[j]):
        dl += 1
    else:
        if dl > max_dl:
            max_dl = dl
            max_liczba = liczby2[i-dl+1]
        dl = 1
    i += 1
    j += 1

# 62.3
rowne = 0
wieksze = 0
for k in range(1000):
    if int(liczby1[k], 8) == int(liczby2[k]):
        rowne += 1
    if int(liczby1[k], 8) > int(liczby2[k]):
        wieksze += 1

# 62.4
dzies = 0
osemkowe = 0
for M in liczby2:
    M = int(M)
    liczby2w8.append(oct(M))

for L in liczby2:
    for x in L:
        if x == "6":
            dzies += 1

for K in liczby2w8:
    for y in K:
        if y == "6":
            osemkowe += 1


with open("wyniki62.txt", "w") as odp:
    odp.write("62.1\n" + "min: " + min + "\n" + "max: " + max)
    odp.write("\n\n62.2\n" + str(max_dl) + "  " + str(max_liczba))
    odp.write("\n\n62.3\n" + "a). " + str(rowne) + "\n" + "b). " + str(wieksze))
    odp.write("\n\n62.4\n" + "w dziesiętnym: " + str(dzies) + "\n" + "w ósemkowym: " + str(osemkowe))

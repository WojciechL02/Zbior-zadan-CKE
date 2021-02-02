"""
zadanie 58, zbiór zadań CKE
"""


# dane_systemy1 - S1 - binarne
# dane_systemy2 - S2 - czwórkowe
# dane_systemy3 - S3 - ósemkowe


system1 = []
system2 = []
system3 = []
with open("dane_systemy1.txt", "r") as plik1:
    for L in plik1:
        L = L.strip()
        L = L.split(" ")
        system1.append(L)

with open("dane_systemy2.txt", "r") as plik2:
    for L in plik2:
        L = L.strip()
        L = L.split(" ")
        system2.append(L)

with open("dane_systemy3.txt", "r") as plik3:
    for L in plik3:
        L = L.strip()
        L = L.split(" ")
        system3.append(L)

# 58.1
min1 = 10000000000000
for I in system1:
    if int(I[1], 2) < min1:
        min1 = int(I[1], 2)
min2 = 10000000000000
for J in system2:
    if int(J[1], 4) < min2:
        min2 = int(J[1], 4)
min3 = 10000000000000
for K in system3:
    if int(K[1], 8) < min3:
        min3 = int(K[1], 8)

# 58.2
licznik2 = 0
k = 0
i = 0
while i <= 1095 and k <= 1094:
    if int(system1[i][0], 2) != (12 + k * 24) and int(system2[i][0], 4) != (12 + k * 24) and int(system3[i][0], 8) != (12 + k * 24):
        licznik2 += 1
    k += 1
    i += 1

# 58.3
indeksy1 = []
max1 = 0
max2 = 0
max3 = 0
i = 1
while i <= 1094:
    if int(system1[i][1], 2) > max1:
        max1 = int(system1[i][1], 2)
        indeksy1.append(i)
    if int(system2[i][1], 4) > max2:
        max2 = int(system2[i][1], 4)
        indeksy1.append(i)
    if int(system3[i][1], 8) > max3:
        max3 = int(system3[i][1], 8)
        indeksy1.append(i)
    i += 1

licznik3 = 0
odrzucone = []
for i in indeksy1:
    if i not in odrzucone:
        licznik3 += 1
        odrzucone.append(i)
            
# 58.4
temp1 = []
for l in range(1095):
    temp1.append(int(system1[l][1], 2))

max_skok = 0
for i in range(len(temp1)):
    for j in range(i+1, len(temp1)):
        ti = temp1[i]
        tj = temp1[j]
        r = pow((ti-tj), 2)
        skok = r/abs(i-j)
        if skok > max_skok:
            max_skok = skok

a = max_skok - int(max_skok)
if a > 0:
    max_skok += 1 - a


with open("wyniki_systemy.txt", "w") as odp:
    odp.write("58.1\n" + "stacja S1: " + str(bin(min1)) + "\n" +
              "stacja S2: " + str(bin(min2)) + "\n" +
              "stacja S3: " + str(bin(min3)))
    odp.write("\n\n58.2\n" + str(licznik2))
    odp.write("\n\n58.3\n" + str(licznik3))
    odp.write("\n\n58.4\n" + str(max_skok))

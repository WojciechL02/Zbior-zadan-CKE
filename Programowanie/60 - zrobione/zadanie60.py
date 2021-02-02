"""
zadanie 66, zbiór zadań CKE
"""


def dzielniki(n):
    tab = []
    d = 2
    tab.append(1)
    while d <= n/2 + 1:
        if n % d == 0:
            tab.append(d)
        if len(tab) > 17:
            break
        d += 1
    tab.append(n)
    return tab


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


dane = []
licznik1 = 0
tablica1 = []
with open("liczby.txt", "r") as plik:
    for L in plik:
        L = int(L.strip())
        dane.append(L)
        # 60.1
        if L < 1000:
            licznik1 += 1
            tablica1.append(L)
# 60.2
odp2 = []
odp21 = []
for N in dane:
    tab1 = dzielniki(N)
    if len(tab1) == 18:
        odp2.append(N)
        odp21.append(tab1)

# 60.3
najw = 0
for Q in dane:
    l = 0
    for O in dane:
        if NWD(Q, O) == 1:
            l += 1
    if l == len(dane) - 1:
        if Q > najw:
            najw = Q

with open("wyniki.txt", "w") as odp:
    odp.write("60.1\n" + str(licznik1) + "\n" +
              "Dwie ostatnie: " + str(tablica1[-2]) + " " + str(tablica1[-1]))
    odp.write("\n\n60.2\n")
    j = 0
    while j < len(odp2):
        odp.write(str(odp2[j]) + "\n" + str(odp21[j]) + "\n")
        j += 1
    odp.write("\n60.3\n" + str(najw))
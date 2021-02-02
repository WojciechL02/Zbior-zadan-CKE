"""
zadanie 78, zbriór zadań CKE
"""


def skrot(w):
    S = [ord(Z) for Z in "ALGORYTM"]
    while len(w) % 8 != 0:
        w += "."
    a = len(w)
    p = 0
    k = 7
    while k <= len(w):
        w1 = w[p:k+1]
        for j in range(8):
            S[j] = (S[j] + ord(w1[j])) % 128
        p += 8
        k += 8
    wynik = ""
    for i in range(8):
        wynik = wynik + chr(65 + S[i] % 26)
    return a, S, wynik


def deszyfr(podpis):
    wynik = ""
    for y in podpis:
        x = ((int(y)*3) % 200)
        wynik += chr(x)
    return wynik


wiadomosci = []
podpisy = []
with open("wiadomosci.txt", "r") as file1:
    for L in file1:
        wiadomosci.append(L.strip())

with open("podpisy.txt", "r") as file2:
    podpisy = [M.strip().split() for M in file2]

# 78.1
zad1 = skrot(wiadomosci[0])

# 78.2
zad2 = []
for skr in podpisy:
    zad2.append(deszyfr(skr))

# 78.3
skroty = []
for wiad in wiadomosci:
    skroty.append(skrot(wiad)[2])
wiarygodnosc = []
numery = ""
for i in range(11):
    if skroty[i] == zad2[i]:
        wiarygodnosc.append("wiarygodne")
        numery += str(i+1) + " "
    else:
        wiarygodnosc.append("zmienione")
zad3 = ""
for i, sk in enumerate(zad2, 1):
    zad3 += f'{i} {sk} {wiarygodnosc[i-1]}\n'

with open("wyniki.txt", "w") as odp:
    odp.write(f'78.1\n{zad1}')
    odp.write(f'\n\n78.2\n{zad2}')
    odp.write(f'\n\n78.3\n{zad3}\n{numery}')
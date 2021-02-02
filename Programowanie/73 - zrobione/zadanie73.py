"""
zadanie 73, zbiór zadań CKE
"""


def dwie_litery(n):
    ok = False
    i = 0
    while i < len(n) - 1:
        if n[i] == n[i+1]:
            ok = True
            break
        i += 1
    return ok


def podslowo(n):
    samogloski = ["A", "E", "I", "O", "U", "Y"]
    dl_max = 0
    dl = 0
    for L in n:
        if L not in samogloski:
            dl += 1
        else:
            if dl > dl_max:
                dl_max = dl
            dl = 0
    return dl_max


licznik1 = 0
tekst = ""
alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ilosc2 = []
max3 = 0
licznik3 = 0
slowa3 = []
with open("tekst.txt", "r") as plik:
    for Z in plik:
        Z = Z.strip().split(" ")
        for S in Z:
            # 73.1
            if dwie_litery(S):
                licznik1 += 1
            tekst += S
            # 73.3
            if podslowo(S) > max3:
                max3 = podslowo(S)
        for N in Z:
            if podslowo(N) == max3:
                licznik3 += 1
                slowa3.append(N)

# 73.2
for L in alfabet:
    ilosc2.append(tekst.count(L))


with open("wyniki.txt", "w") as odp:
    odp.write("73.1\n" + str(licznik1))
    odp.write("\n\n73.2\n")
    k = 0
    while k < len(alfabet):
        odp.write(alfabet[k] + str(": ") + str(ilosc2[k]) + "  " + str(round(ilosc2[k]/len(tekst)*100, 2)) + "%" +"\n")
        k += 1
    odp.write("\n73.3\n" + "Dlugosc najdluzszego podslowa: " + str(max3) + "\n" +
              "Liczba słów: " + str(licznik3) + "\n" +
              "Pierwsze występujące takie słowo: " + slowa3[0])
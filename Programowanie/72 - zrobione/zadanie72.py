"""
zadanie 72, zbiór zadań CKE
"""


def trzy_x_wiekszy(n):
    a = n[0]
    b = n[1]
    if len(a) >= 3*len(b) or len(b) >= 3*len(a):
        return True
    else:
        return False


def podobne(n):
    a = n[0]
    b = n[1]
    if a in b[0:len(a)]:
        return True
    else:
        return False


def funkcja3(n):
    koniec = ""
    a = n[0][::-1]
    b = n[1][::-1]
    kr = min(len(a), len(b))
    i = 0
    while i < kr:
        if a[i] == b[i]:
            koniec += a[i]
        else:
            break
        i += 1
    return koniec


licznik1 = 0
tablica1 = []
tablica2 = []
max3 = 0
il_max = 0
slowa3 = []
with open("napisy.txt", "r") as plik:
    for L in plik:
        L = L.strip().split(" ")
        # 72.1
        if trzy_x_wiekszy(L):
            licznik1 += 1
            if len(tablica1) < 1:
                tablica1.append(L)
        # 72.2
        if podobne(L):
            x = L[0]
            y = L[1]
            koncowka = y[len(x):]
            tablica2.append(L)
            tablica2.append(koncowka)
        # 72.3
        if len(funkcja3(L)) == max3:
            il_max += 1
            slowa3.append(L)
        if len(funkcja3(L)) > max3:
            max3 = len(funkcja3(L))
            il_max = 1
            slowa3 = []
            slowa3.append(L)


with open("wyniki.txt", "w") as odp:
    odp.write("72.1\n" + str(licznik1) + "\n"+
              "Pierwsza para: " + "\n" + str(tablica1))
    odp.write("\n\n72.2\n")
    for l in tablica2:
        odp.write(str(l) + "\n")
    odp.write("\n72.3\n" + "Najdluzsza koncowka: " + str(max3) + "\n")
    for k in slowa3:
        odp.write(str(k) + "\n")
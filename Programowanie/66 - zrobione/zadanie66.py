"""
zadanie 66, zbiór zadań CKE
"""


def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma


def liczba_pierwsza(n):
    pierwsza = True
    i = 2
    while i <= int(n/2 + 1):
        if n % i == 0:
            pierwsza = False
            break
        else:
            i += 1
    return pierwsza


def pitagoras(list):
    x, y, z = list
    c = max(int(x), int(y), int(z))
    a = min(int(x), int(y), int(z))
    b = (int(x) + int(y) + int(z)) - (c + a)
    if a*a + b*b == c*c:
        return True
    else:
        return False


def czy_trojkat(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


# ---------------DANE--------------- #
dane = []
with open("trojki.txt", "r") as plik:
    for T in plik:
        T = T.strip()
        T = T.split(" ")
        dane.append(T)
# ---------------------------------- #

# 66.1
tablica1 = []
for Q in dane:
    if suma_cyfr(int(Q[0])) + suma_cyfr(int(Q[1])) == int(Q[2]):
        tablica1.append(Q)

# 66.2
tablica2 = []
for M in dane:
    a = int(M[0]) * int(M[1])
    if liczba_pierwsza(int(M[0])) and liczba_pierwsza(int(M[1])) and a == int(M[2]):
        tablica2.append(M)

# 66.3
tablica3 = []
i = 0
while i <= len(dane) - 1:
    if pitagoras(dane[i]):
        if pitagoras(dane[i+1]):
            tablica3.append(dane[i])
            tablica3.append(dane[i+1])
    i += 1

# 66.4
licznik4 = 0
max4 = 0
for L in dane:
    if czy_trojkat(int(L[0]), int(L[1]), int(L[2])):
        licznik4 += 1

j = 0
ciag = 1
while j <= len(dane) - 2:
    if czy_trojkat(int(dane[j][0]), int(dane[j][1]), int(dane[j][2])) and czy_trojkat(int(dane[j+1][0]), int(dane[j+1][1]), int(dane[j+1][2])):
        ciag += 1
    else:
        if ciag > max4:
            max4 = ciag
        ciag = 1
    j += 1


with open("wyniki_trojki.txt", "w") as odp:
    odp.write("66.1\n")
    for P in tablica1:
        odp.write(str(P) + "\n")
    odp.write("\n\n66.2\n")
    for K in tablica2:
        odp.write(str(K) + "\n")
    odp.write("\n\n66.3\n")
    for I in tablica3:
        odp.write(str(I) + "\n")
    odp.write("\n\n66.4\n" + "Liczba wierszy: " + str(licznik4) + "\n" +
              "Najdluższy ciąg: " + str(max4))
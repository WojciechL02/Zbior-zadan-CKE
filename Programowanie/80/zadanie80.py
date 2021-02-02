"""
zadanie80, zbiór zadań CKE
"""


def prostokotny(a, b, c):
    if pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(c, 2) + pow(b, 2) == pow(a, 2):
        return True
    return False


def trojkat(a, b, c):
    if a + b > c:
        return True
    return False


dane = []
with open("dane_trojkaty.txt", "r") as file:
    for L in file:
        dane.append(int(L.strip()))

# 80.1
max = 0
zad1 = []
i = 0
while i <= len(dane)-3:
    if prostokotny(dane[i], dane[i+1], dane[i+2]):
        a = str(dane[i]) + ", " + str(dane[i+1]) + ", " + str(dane[i+2])
        zad1.append(a)
    i += 1

# 80.2
for a in dane:
    for b in dane:
        for c in dane:
            if a != b and b != c and a != c:
                if trojkat(a, b, c):
                    if a + b + c > max:
                        max = a + b + c

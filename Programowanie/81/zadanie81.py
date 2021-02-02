"""
zadanie 81, zbiór zadań CKE
"""


def Icwiartka(list):
    for L in list:
        if int(L) <= 0:
            return False
    return True


def dlugosc_odcinka(Xa, Ya, Xb, Yb):
    d = pow(pow(Xb-Xa, 2) + pow(Yb-Ya, 2), 1/2)
    return d


def pitagoras(a, b, c):
    t = [a**2 for a in [a, b, c]]
    if sum(t) == 2 * max(t):
        return True
    return False


def srodek(xa, ya, xb, yb):
    xs = (xa + xb) / 2
    ys = (ya + yb) / 2
    return xs, ys


def punktD(Xb, Yb, Xs, Ys):
    xd = 2 * Xs - Xb
    yd = 2 * Ys - Yb
    return xd, yd


dane1 = []
with open("wspolrzedne.txt", "r") as file1:
    for line in file1:
        line = line.strip().split("\t")
        line = [int(x) for x in line]
        dane1.append(line)

dane2 = []
with open("wspolrzedneTR.txt", "r") as file2:
    for line in file2:
        line = line.strip().split("\t")
        line = [int(x) for x in line]
        dane2.append(line)

# 81.1
zad1 = 0
for zestaw in dane1:
    if Icwiartka(zestaw):
        zad1 += 1


# 81.2
zad2 = 0
for wierzcholki in dane1:
    Xa, Ya, Xb, Yb, Xc, Yc = wierzcholki
    if (Xb-Xa)*(Yc-Yb) == (Xc-Xb)*(Yb-Ya):
        zad2 += 1


# 81.3, 81.4, 81.5
zad3_ob = 0
zad3_wsp = []
zad4 = 0
zad5 = []
for wierzcholki in dane2:
    Xa, Ya, Xb, Yb, Xc, Yc = wierzcholki
    x = dlugosc_odcinka(Xa, Ya, Xb, Yb)
    y = dlugosc_odcinka(Xb, Yb, Xc, Yc)
    z = dlugosc_odcinka(Xa, Ya, Xc, Yc)
    if sum([x, y, z]) > zad3_ob:
        zad3_ob = sum([x, y, z])
        zad3_wsp = ", ".join(str(l) for l in wierzcholki)
    if pitagoras(x, y, z):
        zad4 += 1
    Xs, Ys = srodek(Xa, Ya, Xc, Yc)
    Xd, Yd = punktD(Xb, Yb, Xs, Ys)
    if Xd == Yd:
        zad5.append(f'A({Xa}; {Ya}), B({Xb}; {Yb}), C({Xc}; {Yc}), D({Xd}; {Yd})')
zad3_ob = round(zad3_ob, 2)

with open("wyniki81.txt", "w") as odp:
    odp.write("81.1\n" + str(zad1))
    odp.write("\n\n81.2\n" + str(zad2))
    odp.write("\n\n81.3\n" + f'{zad3_ob}\n{zad3_wsp}')
    odp.write("\n\n81.4\n" + str(zad4))
    odp.write("\n\n81.5\n")
    for wsp in zad5:
        odp.write(wsp + "\n")
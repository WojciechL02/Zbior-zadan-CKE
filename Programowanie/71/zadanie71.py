"""
zadanie 71, zbiór zadań CKE
"""


def f(n):
    wsp = []
    if n >= 0 and n < 1:
        wsp = float(dane[0])
    elif n >= 1 and n < 2:
        wsp = float(dane[1])
    elif n >= 2 and n < 3:
        wsp = float(dane[2])
    elif n >= 3 and n < 4:
        wsp = float(dane[3])
    else:
        wsp = float(dane[4])
    a0 = wsp[0]
    a1 = wsp[1]
    a2 = wsp[2]
    a3 = wsp[3]
    h = a0 + a1 * n + a2 * pow(n, 2) + a3 * pow(n, 3)
    return h


def mz(a, b, e):
    if f(a) == 0.0: return a
    if f(b) == 0.0: return b
    s = (a+b)/2
    if  b-a <= e:
        return s
    if f(a)*f(s) < 0:
        return mz(a, s, e)
    else:
        return mz(s, b, e)


# ---------------DANE--------------- #
dane = []
with open("funkcja.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        L = L.split("   ")
        dane.append(L)
# ---------------------------------- #

# 71.1
x = 1.5
a = float(dane[1][0]) + float(dane[1][1]) * x + float(dane[1][2]) * pow(x, 2) + float(dane[1][3]) * pow(x, 3)
odp1 = str(round(a, 5))

# 71.2
max = 0
max_x = 0
x = 4
while x >= 4 and x <= 4.5:
    b = float(dane[4][0]) + float(dane[4][1]) * x + float(dane[4][2]) * pow(x, 2) + float(dane[4][3]) * pow(x, 3)
    if b > max:
        max = b
        max_x = x
    x += 0.00001

# 71.3
odp3 = ""
for i in range(5):
    odp3 += str(mz(i, i+1, 0.00001)) + "\n"


with open("wyniki_funkcja.txt", "w") as odp:
    odp.write("71.1\n" + odp1)
    odp.write("\n\n71.2\n" + "Największa wartość: " + str(round(max, 5)) + "\n" +
              "Dla argumentu: " + str(round(max_x, 3)))
    odp.write("\n\n71.3\n")

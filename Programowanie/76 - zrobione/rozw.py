
def szyfr(s, p):
    j = list(s)
    for i in range(len(s)):
        k = p[i % len(p)] - 1
        j[i], j[k] = j[k], j[i]
    return "".join(j)


def deszyfr(z, P):
    sl = list(z)
    for i in range(len(z)-1, -1, -1):
        k = P[i % len(P)] - 1
        sl[i], sl[k] = sl[k], sl[i]
    return "".join(sl)


# 1
dane1 = []
with open("szyfr1.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        dane1.append(line)
klucz1 = dane1[6].split(" ")
klucz1 = [int(x) for x in klucz1]
odp1 = ""
for sl in dane1[:6]:
    odp1 += f'{szyfr(sl, klucz1)}\n'

# 2
dane2 = []
with open("szyfr2.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        dane2.append(line)
klucz2 = dane2[1]
klucz2 = [int(x) for x in klucz2.split(" ")]
odp2 = szyfr(dane2[0], klucz2)

# 3
sl3 = ""
with open("szyfr3.txt", "r") as file3:
    for line in file3:
        line = line.strip()
        sl3 = line

odp3 = deszyfr(sl3, [6, 2, 4, 1, 5, 3])


with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + odp1)
    odp.write("\n2.\n" + odp2)
    odp.write("\n\n3.\n" + odp3)
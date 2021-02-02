
def arytm(c):
    r = int(c[1]) -int(c[0])
    for i in range(2, len(c)):
        if int(c[i]) - int(c[i-1]) != r:
            return False, r
    return True, r


def szescian(c):
    najw = 0
    for w in c:
        if int(round(pow(int(w), 1/3)))**3 == int(w):
            if int(w) > najw:
                najw = int(w)
    return najw


def bledny_wyraz(c):
    tab = ""
    r = []
    for i in range(4):
        r.append(int(c[i+1]) - int(c[i]))
    if r[0] != r[1] and r[1] == r[2]:
        tab += c[0]
        return tab
    elif r[0] != r[1] and r[1] != r[2] and r[0] == r[2]:
        tab += c[1]
        return tab
    j = 0
    while j <= len(c) - 1:
        if int(c[j+1]) - int(c[j]) != r[0]:
            tab += c[j+1]
            return tab
        j += 1


ciagi = []
bledne = []
with open("ciagi.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        if len(line.split(" ")) != 1:
            ciagi.append(line.split(" "))

with open("bledne.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        if len(line.split(" ")) != 1:
            bledne.append(line.split(" "))

# 1, 2
odp2 = []
r_max = 0
licznik1 = 0
for ciag in ciagi:
    if arytm(ciag)[0]:
        licznik1 += 1
        if arytm(ciag)[1] > r_max:
            r_max = arytm(ciag)[1]
    a = szescian(ciag)
    if a != 0:
        odp2.append(a)

# 3
wyr3 = []
for bl in bledne:
    wyr3.append(bledny_wyraz(bl))

odp3 = "\n".join(wyr3)


with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + f'{licznik1}\t{r_max}')
    odp.write("\n\n2.\n" + str(odp2))
    odp.write("\n\n3.\n" + odp3)

def test(n):
    ok = True
    for p in n[1:]:
        if p != n[0]:
            ok = False
            break
    return ok


dane = [[] for x in range(200)]
k = 0
obrazki = [[] for x in range(200)]
with open("dane_obrazki.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            dane[k].append(line)
        if line == "":
            k += 1

for i, obr in enumerate(dane):
    for k in range(20):
        obrazki[i].append(obr[k][:-1])

# 1, 2
rew = 0
najw = 0
rek = 0
first = ""
tmp = 0
for ob in obrazki:
    if "".join(ob).count("1") > "".join(ob).count("0"):
        rew += 1
    jed = "".join(ob).count("1")
    if jed > najw:
        najw = jed
    mobr = [[], [], [], []]
    w = 0
    while w < 20:
        if w < 10:
            mobr[0].append(ob[w][:10])
            mobr[1].append(ob[w][10:])
        else:
            mobr[2].append(ob[w][:10])
            mobr[3].append(ob[w][10:])
        w += 1
    if test(mobr):
        rek += 1
        if tmp == 0:
            first = "\n".join(ob)
            tmp += 1

# 3, 4
popr = 0
napr = 0
nienapr = 0
maks_bl = 0
odp4 = ""
for i, obr in enumerate(obrazki):
    ok = True
    b_rz = 0
    rz_idx = 0
    b_kol = 0
    kol_idx = 0
    cols = ["" for k in range(20)]
    for l, row in enumerate(obr):
        if row.count("1") % 2 != int(dane[i][l][-1]):
            b_rz += 1
            rz_idx = l
            if ok and b_rz > 1:
                nienapr += 1
                ok = False
        for j, znak in enumerate(row):
            cols[j] += (znak)
    for h, col in enumerate(cols):
        if col.count("1") % 2 != int(dane[i][20][h]):
            b_kol += 1
            kol_idx = h
            if ok and b_kol > 1:
                nienapr += 1
                ok = False
    bl = b_rz + b_kol
    if bl > maks_bl:
        maks_bl = bl
    if b_rz == 0 and b_kol == 0:
        popr += 1
    elif b_rz <= 1 and b_kol <= 1:
        napr += 1
        if b_rz == 1 and b_kol == 1:
            odp4 += f'{i+1} ({rz_idx+1}; {kol_idx+1})\n'
        elif b_rz == 1 and b_kol == 0:
            odp4 += f'{i+1} ({rz_idx+1}; {21})\n'
        elif b_rz == 0 and b_kol == 1:
            odp4 += f'{i+1} ({21}; {kol_idx+1})\n'


with open("wyniki64.txt", "w") as odp:
    odp.write("1.\n" + f'{rew}\n{najw}')
    odp.write("\n\n2.\n" + f'{rek}\n\n{first}')
    odp.write("\n\n3.\n" + f'poprawnych: {popr}\nnaprawialnych: {napr}\nnienaprawialnych: {nienapr}\nNajwiększa liczba błędnych b.p.: {maks_bl}')
    odp.write("\n\n4.\n" + odp4)

def geny(n):
    gen = []
    m = n
    while len(m) > 0:
        if "AA" in m:
            ip = m.find("AA")
        else: return gen
        if "BB" in m:
            ik = m.find("BB") + 2
        else: return gen
        if len(m[ip:ik]) > 0:
            gen.append(m[ip:ik])
        m = m[ik:]
    return gen



dane = []
gat = []
najw_w_gat = 0
with open("dane_geny.txt", "r") as file:
    for line in file:
        line = line.strip()
        dane.append(line)
        if len(line) not in gat:
            gat.append(len(line))

# 1
for g in gat:
    il = 0
    for os in dane:
        if len(os) == g:
            il += 1
    if il > najw_w_gat:
        najw_w_gat = il

# 2, 3
licznik2 = 0
geny_os = [geny(X) for X in dane]
max3 = 0
max_g = 0
for Y in geny_os:
    for gen in Y:
        if len(gen) > max_g:
            max_g = len(gen)
        if "BCDDC" in gen:
            licznik2 += 1
    if len(Y) > max3:
        max3 = len(Y)

# 4
silne = 0
odporne = 0
for L in dane:
    if L == L[::-1]:
        silne += 1
    if "".join(geny(L)) == "".join(geny(L[::-1])):
        odporne += 1


with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + f'{len(gat)}\n{najw_w_gat}')
    odp.write("\n\n2.\n" + f'{licznik2}')
    odp.write("\n\n3.\n" + f'{max3}\n{max_g}')
    odp.write("\n\n4.\n" + f'odporne: {odporne}\nsilnie odporne: {silne}')
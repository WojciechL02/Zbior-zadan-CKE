
def szyfr(a, b, n):
    w = ""
    t = []
    for l in n:
        t.append(b + a*(ord(l)-97))
    for x in t:
        w += chr(97 + x % 26)
    return w


slowa = []
jawne = []
ukryte = []
with open("tekst.txt", "r") as file:
    for line in file:
        line = line.strip()
        slowa = line.split(" ")

with open("probka.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        jawne.append(line.split(" ")[0])
        ukryte.append(line.split(" ")[1])
        

# 1, 2
odp1 = ""
odp2 = ""
for s in slowa:
    if s[0] == "d" and s[-1] == "d":
        odp1 += s + "\n"
    if len(s) >= 10:
        odp2 += szyfr(5, 2, s) + "\n"

# 3
odp3 = ""
for s in range(5):
    sl = ""
    p = False
    for i in range(26):
        for j in range(26):
            if szyfr(i, j, jawne[s]) == ukryte[s]:
                sl += f'({i}, {j}); '
                p = True
            if szyfr(i, j, ukryte[s]) == jawne[s]:
                sl += f'({i}, {j})'
                if p:
                    break
    odp3 += str(sl) + "\n"

with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + odp1)
    odp.write("\n2.\n" + odp2)
    odp.write("\n3.\n" + odp3)
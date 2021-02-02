
def min_i_max(c):
    mini = []
    maxi = []
    i = 0
    while i < len(c) - 1:
        mini.append(min(int(c[i], 8), int(c[i+1], 8)))
        maxi.append(max(int(c[i], 8), int(c[i+1], 8)))
        i += 2
    return mini, maxi


dane1 = []
dane2 = []
with open("liczby1.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        dane1.append(line)

with open("liczby2.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        dane2.append(int(line))


# 1
min1 = oct(min(min_i_max(dane1)[0]))[2:]
max1 = oct(max(min_i_max(dane1)[1]))[2:]

# 2
maxd = 0
maxe = 0
for i in range(1, len(dane2)):
    d = 1
    e = dane2[i]
    for j in range(i+1, len(dane2)):
        if dane2[j-1] <= dane2[j]:
            d += 1
        else:
            break
    if d > maxd:
        maxd = d
        maxe = e

# 3
licznik1 = 0
licznik2 = 0
for i in range(len(dane1)):
    if int(dane1[i], 8) == dane2[i]:
        licznik1 += 1
    if int(dane1[i], 8) > dane2[i]:
        licznik2 += 1

# 4
dec = 0
osm = 0
for L in dane2:
    dec += str(L).count("6")
    osm += oct(L)[2:].count("6")

with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + f'{min1}\n{max1}')
    odp.write("\n\n2.\n" + f'{maxd}\n{maxe}')
    odp.write("\n\n3.\n" + f'{licznik1}\n{licznik2}')
    odp.write("\n\n4.\n" + f'{dec}\n{osm}')
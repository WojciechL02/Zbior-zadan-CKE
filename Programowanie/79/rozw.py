
dane = []
with open("okregi.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        line = [float(x) for x in line]
        dane.append(line)

# 1, 2
odp1 = [0, 0, 0, 0, 0]
odp2 = 0
for i, okrag in enumerate(dane):
    x, y, r = okrag
    if x > 0 and y > 0:
        if x-r > 0 and y-r > 0:
            odp1[0] += 1
        else:
            odp1[4] += 1
    elif x < 0 and y > 0:
        if x+r < 0 and y-r > 0:
            odp1[1] += 1
        else:
            odp1[4] += 1
    elif x < 0 and y < 0:
        if x+r < 0 and y+r < 0:
            odp1[2] += 1
        else:
            odp1[4] += 1
    elif x > 0 and y < 0:
        if x-r > 0 and y+r < 0:
            odp1[3] += 1
        else:
            odp1[4] += 1
    else:
        odp1[4] += 1
    
    for j in range(i+1, len(dane)):
        if dane[i][0] == dane[j][0] and dane[i][1] == -dane[j][1] and dane[i][2] == dane[j][2]:
            odp2 += 1
        elif dane[i][1] == dane[j][1] and dane[i][0] == -dane[j][0] and dane[i][2] == dane[j][2]:
            odp2 += 1
    
# 1 i 2 są zrobione dobrze




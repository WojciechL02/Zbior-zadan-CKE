import math

dane1 = []
dane2 = []
dane3 = []
temp1 = []
temp2 = []
temp3 = []

with open("dane_systemy1.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        dane1.append(line.split(" "))
        temp1.append(int(line.split(" ")[1], 2))

with open("dane_systemy2.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        dane2.append(line.split(" "))
        temp2.append(int(line.split(" ")[1], 4))

with open("dane_systemy3.txt", "r") as file3:
    for line in file3:
        line = line.strip()
        dane3.append(line.split(" "))
        temp3.append(int(line.split(" ")[1], 8))

# 1
min1 = 100
min2 = 100
min3 = 100
for odczyt in dane1:
    if int(odczyt[1], 2) < min1:
        min1 = int(odczyt[1], 2)
for odczyt in dane2:
    if int(odczyt[1], 4) < min2:
        min2 = int(odczyt[1], 4)
for odczyt in dane3:
    if int(odczyt[1], 8) < min3:
        min3 = int(odczyt[1], 8)
odp1 = f'{bin(min1)}, {bin(min2)}, {bin(min3)}'

# 2
licznik2 = 0
for i in range(len(dane1)):
    if int(dane1[i][0], 2) % 12 != 0 and int(dane2[i][0], 4) % 12 != 0 and int(dane3[i][0], 8) % 12 != 0:
        licznik2 += 1

# 3
licznik3 = 0
max1 = 0
max2 = 0
max3 = 0
for k in range(len(temp1)):
    tmp = False
    if temp1[k] > max1:
        max1 = temp1[k]
        tmp = True
    if temp2[k] > max2:
        max2 = temp2[k]
        tmp = True
    if temp3[k] > max3:
        max3 = temp3[k]
        tmp = True
    if tmp:
        licznik3 += 1

# 4
max4 = 0
for i in range(len(dane1)-1):
    for j in range(i+1, len(dane1)):
        r = pow(temp1[i] - temp1[j], 2)
        res = math.ceil(r/abs(i - j))
        if res > max4:
            max4 = res

with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + odp1)
    odp.write("\n\n2.\n" + str(licznik2))
    odp.write("\n\n3.\n" + str(licznik3))
    odp.write("\n\n4.\n" + str(max4))

def dzielniki(n):
    t = [1]
    for i in range(2, n//2 + 1):
        if n % i == 0:
            t.append(i)
    t.append(n)
    return t


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def wzgl_prw(n, arr):
    for L in arr:
        if n != L:
            if NWD(n, L) != 1:
                return False
    return True


dane = []
with open("liczby.txt", "r") as file:
    for line in file:
        line = line.strip()
        dane.append(int(line))

# 1, 2
odp1 = ""
odp2 = ""
l1 = 0
for L in dane[::-1]:
    if L < 1000:
        l1 += 1
        if l1 <= 2:
            odp1 += str(L) + "\n"
    if len(dzielniki(L)) == 18:
        odp2 += f'{L}\t{dzielniki(L)}\n'

# 3
najw = 0
for x in dane:
    if wzgl_prw(x, dane):
        if x > najw:
            najw = x


with open("wyniki1.txt", "w") as odp:
    odp.write("1.\n" + str(l1) + "\n" + odp1)
    odp.write("\n\n2.\n" + odp2)
    odp.write("\n\n3.\n" + str(najw))
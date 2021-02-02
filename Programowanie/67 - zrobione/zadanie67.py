"""
zadanie 67, zbiór zadań CKE
"""


def liczba_pierwsza(n):
    pierwsza = True
    if n == 1:
        return False
    if n == 2:
        return pierwsza
    i = 2
    while i <= int(n/2 + 1):
        if n % i == 0:
            pierwsza = False
            break
        else:
            i += 1
    return pierwsza


# 67.1
Fib = [1, 1, 2]
i = 3
while i <= 39:
    Fib.append(Fib[i-1] + Fib[i-2])
    i += 1
# 67.2
tablica2 = []
for L in Fib:
    if liczba_pierwsza(L):
        tablica2.append(L)

# 67.3
Fib_bin = []
for N in Fib:
    a = str(bin(N))
    Fib_bin.append(a[2:])
odp3 = []
dl = len(Fib_bin[-1])
for Q in Fib_bin:
    dl1 = len(Q)
    k = dl - dl1
    odp3.append(k * "0" + Q)

# 67.4
tablica4 = []
for M in Fib_bin:
    l = M.count("1")
    if l == 6:
        tablica4.append(M)

with open("wyniki.txt", "w") as odp:
    odp.write("67.1\n" + "F10: " + str(Fib[9]) + "\n" + "F20: " + str(Fib[19]) + "\n" +
              "F30: " + str(Fib[29]) + "\n" + "F40: " + str(Fib[39]))
    odp.write("\n\n67.2\n")
    for j in tablica2:
        odp.write(str(j) + "\n")
    odp.write("\n\n67.3\n")
    for k in odp3:
        odp.write(k + "\n")
    odp.write("\n\n67.4\n")
    for p in tablica4:
        odp.write(p + "\n")

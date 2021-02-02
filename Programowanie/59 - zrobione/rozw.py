
def rozklad(n):
    czynniki = []
    k = 1
    while k < n ** (1 / 2):
        k += 1
        while n % k == 0:
            czynniki.append(k)
            n /= k
    if n != 1:
        czynniki.append(int(n))
    return czynniki


def il_cyfr(n):
    il = 1
    for i in str(n):
        il *= int(i)
    return il


licznik1 = 0
licznik2 = 0
arr3 = [0 for i in range(8)]
min = 999999999
max = 0
with open("liczby.txt", "r") as file:
    for line in file:
        line = line.strip()
        # 1
        r = set(rozklad(int(line)))
        if len(r) == 3 and 2 not in r:
            licznik1 += 1

        # 2
        s = str(int(line) + int(line[::-1]))
        if s == s[::-1]:
            licznik2 += 1
        
        # 3
        l = 0
        liczba = int(line)
        while len(str(line)) > 1:
            line = il_cyfr(line)
            l += 1
        for j in range(8):
            if l-1 == j:
                arr3[j] += 1
        if l == 1:
            if liczba > max:
                max = liczba
            if liczba < min:
                min = liczba
        odp3 = f'{arr3}\nmax: {max}\nmin: {min}'


with open("wyniki.txt", "w") as odp:
    odp.write("1.\n" + str(licznik1))
    odp.write("\n\n2.\n" + str(licznik2))
    odp.write("\n\n3.\n" + odp3)        
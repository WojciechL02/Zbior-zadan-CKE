"""
zadnie 75, zbiór zadań CKE
"""


def pierw_i_ost_d(n):
    if n[0] == "d" and n[-1] == "d":
        return True
    else:
        return False


def szyfr(n, a=5, b=2):
    slowo = ""
    for L in n:
        w = alfabet.get(L) * a + b
        if w > 25:
            l = w % 26
        else:
            l = w
        s = l + 97
        slowo += chr(s)
    return slowo


tablica1 = []
tablica2 = []
alfabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
with open("tekst.txt", "r") as plik1:
    for T in plik1:
        T = T.strip().split(" ")
        for S in T:
            # 75.1
            if pierw_i_ost_d(S):
                tablica1.append(S)
            # 75.2
            if len(S) >= 10:
                tablica2.append(szyfr(S))

odp3 = ""
with open("probka.txt", "r") as plik2:
    for L in plik2:
        L = L.strip().split(" ")
        slowo, zaszyfrowane = L
        for A in range(26):
            for B in range(26):
                if szyfr(slowo, A, B) == zaszyfrowane:
                    odp3 += f'{L} - szyfr - {A, B}\n'
                if szyfr(zaszyfrowane, A, B) == slowo:
                    odp3 += f'{L} - deszyfr - {A, B}\n'


with open("wyniki.txt", "w") as odp:
    odp.write("75.1\n")
    for s in tablica1:
        odp.write(s + "\n")
    odp.write("\n75.2\n")
    for k in tablica2:
        odp.write(k + "\n")
    odp.write("\n75.3\n" + odp3)
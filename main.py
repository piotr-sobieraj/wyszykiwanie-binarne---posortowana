def binarnie(tablica: list[int], lewy: int, prawy: int, szukany: int):

    if lewy > prawy:
        print(f"Nie znaleziono {szukany}.")
        return 
    
    s = (lewy + prawy) // 2
    if szukany == tablica[s]:
        print(f"Znaleziono {szukany} na pozycji {s}.")
    else:
        if szukany < tablica[s]:
            binarnie(tablica, lewy, s - 1, szukany)
        else:
            binarnie(tablica, s + 1, prawy, szukany)

tab = [x for x in range(10)]
binarnie(tab, 0, len(tab) - 1, -1)
binarnie(tab, 0, len(tab) - 1, 0)
binarnie(tab, 0, len(tab) - 1, 1)
binarnie(tab, 0, len(tab) - 1, 2)
binarnie(tab, 0, len(tab) - 1, 3)
binarnie(tab, 0, len(tab) - 1, 4)
binarnie(tab, 0, len(tab) - 1, 5)
binarnie(tab, 0, len(tab) - 1, 6)
binarnie(tab, 0, len(tab) - 1, 7)
binarnie(tab, 0, len(tab) - 1, 8)
binarnie(tab, 0, len(tab) - 1, 9)
binarnie(tab, 0, len(tab) - 1, 10)


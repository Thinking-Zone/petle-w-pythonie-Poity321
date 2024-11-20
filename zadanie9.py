def znajdz_podzielna_przez_7(): 
    for liczba in range(1, 101):
        if liczba % 7 == 0:
            print(f"Pierwsza liczba podzielna przez 7 to: {liczba}") 
            break 
znajdz_podzielna_przez_7()

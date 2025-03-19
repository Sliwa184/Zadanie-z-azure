def rysuj_plansze(plansza):
    print(f"\n{plansza[0]} | {plansza[1]} | {plansza[2]}")
    print("--+---+--")
    print(f"{plansza[3]} | {plansza[4]} | {plansza[5]}")
    print("--+---+--")
    print(f"{plansza[6]} | {plansza[7]} | {plansza[8]}\n")

def sprawdz_zwyciestwo(plansza, gracz):
    zwyciestwa = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # wiersze
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolumny
                  (0, 4, 8), (2, 4, 6)]  # przekątne
    for x, y, z in zwyciestwa:
        if plansza[x] == plansza[y] == plansza[z] == gracz:
            return True
    return False

def sprawdz_remis(plansza):
    return all(komorka in ["X", "O"] for komorka in plansza)

def gra_w_kolko_krzyzyki():
    plansza = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gracze = ["X", "O"]
    tura = 0

    while True:
        rysuj_plansze(plansza)

        while True:
            try:
                wybor = int(input(f"Gracz {gracze[tura]} wybiera pole (1-9): "))
                if wybor < 1 or wybor > 9 or plansza[wybor - 1] in ["X", "O"]:
                    print("Podaj wartość pola od 1-9, które jest jeszcze wolne.")
                else:
                    break
            except ValueError:
                print("Nie ma mordo takiej wartości... Podaj liczbę od 1 do 9.")

        plansza[wybor - 1] = gracze[tura]

        if sprawdz_zwyciestwo(plansza, gracze[tura]):
            rysuj_plansze(plansza)
            print(f"Gratulacje! Gracz {gracze[tura]} wygrał!")
            break

        if sprawdz_remis(plansza):
            rysuj_plansze(plansza)
            print("Remis! Nie ma zwycięzcy.")
            break

        tura = 1 - tura

gra_w_kolko_krzyzyki()
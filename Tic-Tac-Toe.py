def atspausdinti_tinkleli(tinklelis):
    print(f"\n|{tinklelis[0]}|{tinklelis[1]}|{tinklelis[2]}|")
    print(f"|{tinklelis[3]}|{tinklelis[4]}|{tinklelis[5]}|")
    print(f"|{tinklelis[6]}|{tinklelis[7]}|{tinklelis[8]}|\n")


def ar_laimejo(tinklelis, zaidejas):
    if (tinklelis[0] == zaidejas and tinklelis[1] == zaidejas and tinklelis[2] == zaidejas) or \
       (tinklelis[3] == zaidejas and tinklelis[4] == zaidejas and tinklelis[5] == zaidejas) or \
       (tinklelis[6] == zaidejas and tinklelis[7] == zaidejas and tinklelis[8] == zaidejas) or \
       (tinklelis[0] == zaidejas and tinklelis[3] == zaidejas and tinklelis[6] == zaidejas) or \
       (tinklelis[1] == zaidejas and tinklelis[4] == zaidejas and tinklelis[7] == zaidejas) or \
       (tinklelis[2] == zaidejas and tinklelis[5] == zaidejas and tinklelis[8] == zaidejas) or \
       (tinklelis[0] == zaidejas and tinklelis[4] == zaidejas and tinklelis[8] == zaidejas) or \
       (tinklelis[2] == zaidejas and tinklelis[4] == zaidejas and tinklelis[6] == zaidejas):
        return True
    else:
        return False


def ar_lygiosios(tinklelis):
    if type(tinklelis[0]) == str and type(tinklelis[1]) == str and type(tinklelis[2]) == str and \
       type(tinklelis[3]) == str and type(tinklelis[4]) == str and type(tinklelis[5]) == str and \
       type(tinklelis[6]) == str and type(tinklelis[7]) == str and type(tinklelis[8]) == str:
        return True
    else:
        return False


def pradeti_ejima(zaidejas):
    vieta = input(f"{zaidejas}'ko ėjimas. Pasirink skaičių (1-9):\n")
    vieta = int(vieta)-1
    return vieta


def zaisti_zaidima():
    tinklelis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pradeda1 = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    pradeda2 = ["O", "X", "O", "X", "O", "X", "O", "X", "O"]

    while True:
        pasirinkimas = input("Pasirinkite, kas pradeda žaidimą, O ar X?\n")
        if pasirinkimas == "X" or pasirinkimas == "O":
            if pasirinkimas == 'X':
                zaidejai = pradeda1
                break
            if pasirinkimas == "O":
                zaidejai = pradeda2
                break
        else:
            print("Neteisingai pasirinktas simbolis. Įrašykite X arba O didžiosiomis raidėmis")

    zaidejas_index = 0

    while True:
        atspausdinti_tinkleli(tinklelis)        # Spausdinamas tinklelis
        zaidejas = zaidejai[zaidejas_index]     # Iš list zaidėjai, parenkamas X arba O pagal indeksą
        ejimas = pradeti_ejima(zaidejas)        # Ėjimui priskiriamas skaičius nuo 0 iki 9
        tinklelis[ejimas] = zaidejas            # listui tinklelis pagal indeksą priskiriamas žaidėjas, t. y. X arba O
        if ar_laimejo(tinklelis, zaidejas):     # Tikrinamas laimėtojas
            atspausdinti_tinkleli(tinklelis)
            print(f"{zaidejas} laimėjo!")
            break
        elif ar_lygiosios(tinklelis):           # Tikrinamos lygiosios
            atspausdinti_tinkleli(tinklelis)
            print(f"Lygiosios!")
            break
        zaidejas_index += 1                     # Po kiekvienos iteracijos 1-tu padidinamas indeksas


zaisti_zaidima()                                # Inicijuoja žaidimą

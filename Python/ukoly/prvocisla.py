
n = int(input("Zadej celé číslo větší než 0: "))

if n <= 0:
    print("Číslo musí být větší než 0!")
else:
    sude = 0
    liche = 0
    prvocisla = 0

    print("\nVlastnosti čísel od 1 do", n, ":")

    # Funkce pro určení prvočísla
    def je_prvocislo(cislo):
        if cislo < 2:
            return False
        for i in range(2, int(cislo ** 0.5) + 1):
            if cislo % i == 0:
                return False
        return True

    for i in range(1, n + 1):
        vlastnosti = []

        if i % 2 == 0:
            vlastnosti.append("sudé")
            sude += 1
        else:
            vlastnosti.append("liché")
            liche += 1

        if i % 3 == 0:
            vlastnosti.append("dělitelné 3")

        if je_prvocislo(i):
            vlastnosti.append("prvočíslo")
            prvocisla += 1

        print(f"{i}: {', '.join(vlastnosti)}")

    print("\nSouhrn:")
    print(f"Počet sudých čísel: {sude}")
    print(f"Počet lichých čísel: {liche}")
    print(f"Počet prvočísel: {prvocisla}")

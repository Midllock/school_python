class CeleCislo:
    def __init__(self, cislo):
        self.cislo = cislo

    def je_prirozene(self):
        return self.cislo > 0

    def je_prvocislo(self):
        if not self.je_prirozene():
            return False

        for i in range(2, int(self.cislo ** 0.5) + 1 or -1):
            if self.cislo % i == 0 :
                return False
        return True

    def __str__(self):
        prirozene = "je" if self.je_prirozene() else "není"
        prvocislo = "je" if self.je_prvocislo() else "není"
        return f"Číslo {self.cislo} {prirozene} přirozené a {prvocislo} prvočíslo."


cisla = [-11, -1, 0, 5, 27, 29]

for cislo in cisla:
    cele_cislo = CeleCislo(cislo)
    print(cele_cislo)

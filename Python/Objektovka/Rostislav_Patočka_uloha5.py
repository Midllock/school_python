from abc import ABC, abstractmethod

class Vozidlo(ABC):
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    @abstractmethod
    def start(self):
        pass

class Auto(Vozidlo):
    def __init__(self, znacka, model, pocet_dveri):
        super().__init__(znacka, model)
        self.pocet_dveri = pocet_dveri
    
    def start(self):
        return f"Auto {self.znacka} se značkou {self.model} startuje se {self.pocet_dveri} dveřmi."
class Motorka(Vozidlo):
    def __init__(self, znacka, model, typ_motorky):
        super().__init__(znacka, model)
        self.typ_motorky = typ_motorky
    
    def start(self):
        return f"Motorka {self.znacka} se značkou {self.model} typu {self.typ_motorky} startuje."
    
auto1 = Auto("Škoda", "Octavia", 4)
auto2 = Auto("Volkswagen", "Golf", 5)
    
motorka1 = Motorka("Honda", "CBR500R", "sportovní")
motorka2 = Motorka("Yamaha", "MT-07", "naked bike")
    
print(auto1.start())  # Auto Škoda startuje se 4 dveřmi.
print(auto2.start())  # Auto Volkswagen startuje se 5 dveřmi.
print(motorka1.start())  # Motorka Honda typu sportovní startuje.
print(motorka2.start())  # Motorka Yamaha typu naked bike startuje.
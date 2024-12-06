class Tovarna:
    def __init__(self,darky):
        self.darky = darky
        self.darky_list=[]

    def vyrobdarky (self, darky, pocet):
        self.darky = darky
        self.pocet = pocet
        self.darky_list.append({'darky': darky, 'pocet': pocet})

    def __str__(self):
        darky_list = "" .join(f"Vyrobili jsme {vyrobdarky['darky']} v počtu: {vyrobdarky['pocet']}\n" for vyrobdarky in self.darky_list) 
        return f"{darky_list}"
    

Tovarna = Tovarna("Druhy")
Tovarna.vyrobdarky("autíčko", 5)
Tovarna.vyrobdarky("fotbalový míč", 1)
Tovarna.vyrobdarky("mobil", 2)
Tovarna.vyrobdarky("tablet", 4)
Tovarna.vyrobdarky("sluchátka", 18)
print(Tovarna)
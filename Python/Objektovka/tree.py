
class Tree:
        

    def __init__(self,ozdob):
        self.ozdoby = ozdob
        self.ozdob_list=[]

    def ozdob (self, typ, barva, pocet):
        self.typ = typ
        self.barva = barva
        self.pocet = pocet
        self.ozdob_list.append({'typ': typ, 'barva': barva, 'pocet': pocet})

    def __str__(self):
        ozdoby_list = "\n" .join(f"{ozdob['typ']} {ozdob['barva']} {ozdob['pocet']}\n" for ozdob in self.ozdob_list)
        return f"{self.ozdoby} s: \n{ozdoby_list}"

Tree = Tree("borovice")
Tree.ozdob("světelný řetez", "studená bílá", 1)
Tree.ozdob("koule", "červená", 10)
Tree.ozdob("koule", "bílá", 10)
Tree.ozdob("girlanda", "bílá", 3)
Tree.ozdob("girlanda", "červená", 3)
Tree.ozdob("cukrovinka", "hnědá", 20)

print(Tree)


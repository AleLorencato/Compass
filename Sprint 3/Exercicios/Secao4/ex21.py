class Passaro:
    def voar(self):
        print("Voando...")
    def emitir_som(self,som):
        self.som = som
class Pato(Passaro):
    def voar(self):
        print("Voando...")
    def emitir_som(self,som):
        print(som)
class Pardal(Passaro):
    def voar(self):
        print("Voando...")
    def emitir_som(self,som):
        print(som)

som = "Quack Quack"

p1 = Pato()

print("Pato")

p1.voar()

print("Pato emitindo som...")

p1.emitir_som(som)

som ="Piu Piu"

p2 = Pardal()

print("Pardal")

p2.voar()

print("Pardal emitindo som...")

p2.emitir_som(som)
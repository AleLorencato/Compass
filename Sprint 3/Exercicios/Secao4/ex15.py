class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada


l1 = Lampada(False)

l1.liga()
print("A lâmpada está ligada?", l1.esta_ligada())  

l1.desliga()
print("A lâmpada ainda está ligada?", l1.esta_ligada())
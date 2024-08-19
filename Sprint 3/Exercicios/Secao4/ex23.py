class Calculo:

    def soma(self,x,y):
        resultado = 0
        self.x = x
        self.y = y
        resultado = x + y
        return resultado
    def subtracao(self,x,y):
        resultado = 0
        self.x = x
        self.y = y
        resultado = x - y
        return resultado

c1 = Calculo()
print(f"Somando: {c1.soma(4,5)}")
print(f"Subtraindo: {c1.subtracao(4,5)}")
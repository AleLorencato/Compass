class Aviao:
    def __init__(self,modelo,velocidade_maxima,cor,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade


aviao1 = Aviao("BOIENG456","1500 km/h","",400)
aviao2 = Aviao("Embraer Praetor 600","863km/h","",14)
aviao3 = Aviao("Antonov An-2","258 Km/h","",12)

print(f"O avião de modelo {aviao1.modelo} possui uma velocidade máxima de {aviao1.velocidade_maxima}, capacidade para {aviao1.capacidade} passageiros e é da cor {aviao1.cor}")
print(f"O avião de modelo {aviao2.modelo} possui uma velocidade máxima de {aviao2.velocidade_maxima}, capacidade para {aviao2.capacidade} passageiros e é da cor {aviao2.cor}")
print(f"O avião de modelo {aviao3.modelo} possui uma velocidade máxima de {aviao3.velocidade_maxima}, capacidade para {aviao3.capacidade} passageiros e é da cor {aviao3.cor}")
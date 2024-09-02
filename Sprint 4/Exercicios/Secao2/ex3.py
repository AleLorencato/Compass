from functools import reduce
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
def calcula_saldo(lancamentos) -> float:
    valores = list(map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos))
    def calcular_total():
        return reduce(lambda x,y: x+y, valores, 0)
    return calcular_total()

resultado = calcula_saldo(lancamentos)
print(resultado)

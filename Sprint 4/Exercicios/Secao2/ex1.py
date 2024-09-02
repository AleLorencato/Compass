with open('number.txt', 'r') as arquivo:
    numeros = list(map(lambda linha: int(linha.strip()), arquivo.readlines()))

def filtrar(numeros):
    pares = filter(lambda x: x % 2 == 0, numeros)
    maiores_pares = sorted(pares, reverse=True)[:5]
    return maiores_pares

maiores_pares = filtrar(numeros)

soma = sum(maiores_pares)

print(maiores_pares)
print(soma)

def soma(texto):
    numeros = texto.split(',')
    final = sum(int(valor) for valor in numeros)
    print(final)

texto = "1,3,4,6,10,76"
soma(texto)

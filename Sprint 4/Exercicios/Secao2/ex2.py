def conta_vogais(texto:str) -> int:
    vogais = filter(lambda x: x.lower() in ('a', 'e', 'i', 'o', 'u'),texto)
    return len(list(vogais))

texto = "Paralelepipedo"
tamanho = conta_vogais(texto)
print(tamanho)

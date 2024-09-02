conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

def maiores_que_media(conteudo:dict)->list:
    maiores = []
    media = sum(conteudo.values())/len(conteudo)
    for key, value in conteudo.items():
        if value > media:
            maiores.append((key, value))

    maiores.sort(key=lambda x: x[1])

    return maiores

print(maiores_que_media(conteudo))
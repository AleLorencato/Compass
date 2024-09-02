lista = []
with open('estudantes.csv', 'r') as lines:
    for line in lines:
        lista.append(line.strip().split(','))

def nome(lista):
    nomes = map(lambda x: x[0], lista)
    return list(nomes)

def maiores_notas(lista):
    maiores = []
    for estudante in lista:
        notas = list(map(int, estudante[1:]))
        notas = sorted(notas, reverse=True)
        maiores.append(notas[:3])
    return maiores

def media(maiores_notas):
    medias = list(map(lambda x: round(sum(x) / 3, 2), maiores_notas))
    return medias

nome_estudante = nome(lista)
maiores_notas_lista = maiores_notas(lista)
media_estudante = media(maiores_notas_lista)

estudante = list(zip(nome_estudante, maiores_notas_lista, media_estudante))
estudante.sort(key=lambda x: x[0])

for nome, notas, media in estudante:
    print(f'Nome: {nome} Notas: {notas} Média: {media}')
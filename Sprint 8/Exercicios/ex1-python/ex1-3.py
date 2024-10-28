import names
import random
import time

random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0,qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios'.format(qtd_nomes_aleatorios))

dados = []

for i in range (0,qtd_nomes_aleatorios):
    dados.append(random.choice(aux))



def gerar_arquivo(dados):
    with open('nomes_aleatorios.txt','w') as file:
        for nome in dados:
            file.write(nome + '\n')
    print('Arquivo nomes_aleatorios.txt criado com sucesso!')

gerar_arquivo(dados)

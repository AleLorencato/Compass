def getAnimais():
    animais = ['cachorro', 'gato', 'papagaio', 'peixe', 'tartaruga', 'cobra', 'leão', 'tigre', 'elefante', 'girafa', 'hipopótamo', 'rinoceronte', 'urso', 'panda', 'puma', 'lobo', 'raposa', 'guaxinim', 'esquilo', 'veado']
    animaisOrdernados = []
    for animal in sorted(animais):
        animaisOrdernados.append(animal)
        print(animal)
    return animaisOrdernados

def writeCsv():
    resultado = getAnimais()
    with open('animais.csv','w') as file:
        for animal in resultado:
            file.write(animal + '\n')
    print('Arquivo animais.csv criado com sucesso!')

if __name__ == "__main__":
    writeCsv()

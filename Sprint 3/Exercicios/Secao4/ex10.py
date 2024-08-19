lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
def funcao(l):
    return list(set(l))
print(funcao(lista))

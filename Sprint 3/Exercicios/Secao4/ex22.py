class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None


    def nome(self):
        return self.__nome


    def nome(self, valor):
        self.__nome = valor


pessoa = Pessoa(0)
pessoa.nome = "Fulano De Tal"
print(pessoa.nome)
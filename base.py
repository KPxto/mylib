class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def quem(self):
        return f'Ola, meu nome é {self.nome} e tenho {self.idade} anos'

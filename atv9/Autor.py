class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento

    def exibirAutor(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Data de Nascimento: {self.dataNascimento}")

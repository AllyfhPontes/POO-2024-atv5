import json

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionarLivro(self, livro):
        self.__livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' adicionado com sucesso!")

    def removerLivro(self, titulo):
        for livro in self._livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def buscarLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                print(f"Livro encontrado: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano: {livro.get_anoPublicacao()}")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listarLivros(self):
        if not self.__livros:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print("Lista de Livros na Biblioteca:")
            for livro in self.__livros:
                print(f"- {livro.get_titulo()} ({livro.get_anoPublicacao()}), Autor: {livro.get_autor().get_nome()}")

    def salvarEmJson(self, arquivo):
        objetos_dict = [obj.to_dict() for obj in self.__livros]
        dados_em_json = json.dumps(objetos_dict)
        with open(arquivo, 'w') as arquivo:
            arquivo.write(dados_em_json)

    def recuperarDeJson(self, arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados_em_dicionario = json.load(f)
        for dados in dados_em_dicionario:
            objeto = Livro.from_dict(dados)
            self.adicionarLivro(objeto)

    
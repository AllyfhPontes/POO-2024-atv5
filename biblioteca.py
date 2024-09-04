class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado.")

    def removerLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido.")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"Livro '{titulo}' encontrado:")
                livro.exibirLivro()
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listarLivros(self):
        if len(self.livros) == 0:  # Pequeno erro: poderia ser simplesmente 'if not self.livros:'
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                livro.exibirLivro()
    
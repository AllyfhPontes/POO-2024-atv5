class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def exibirLivro(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de Publicação: {self.anoPublicacao}")
        self.autor.exibirAutor()

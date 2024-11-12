from biblioteca import Autor, Livro, Biblioteca

def menu():
    print("\nMenu Biblioteca")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Buscar livro")
    print("4. Listar livros")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            data_nascimento = input("Data de nascimento do autor: ")
            ano_publicacao = input("Ano de publicação do livro: ")  # Pequeno erro: não converte para int

            autor = Autor(nome_autor, nacionalidade, data_nascimento)
            livro = Livro(titulo, autor, ano_publicacao)

            biblioteca.adicionarLivro(livro)

        elif opcao == "2":
            titulo = input("Título do livro a ser removido: ")
            biblioteca.removerLivro(titulo)

        elif opcao == "3":
            titulo = input("Título do livro a ser buscado: ")
            biblioteca.buscarLivro(titulo)

        elif opcao == "4":
            biblioteca.listarLivros()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

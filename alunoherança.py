class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Curso: {self.curso}"

# Classe AlunoCursando herda de Aluno
class AlunoCursando(Aluno):
    def __init__(self, matricula, nome, curso, ano_atual, ano_concluir):
        super().__init__(matricula, nome, curso)
        self.ano_atual = ano_atual
        self.ano_concluir = ano_concluir

    def __str__(self):
        return (f"{super().__str__()}, Ano Atual: {self.ano_atual}, Ano de Conclusão: {self.ano_concluir}")

# Classe AlunoConcluinte herda de Aluno
class AlunoConcluinte(Aluno):
    def __init__(self, matricula, nome, curso, data_conclusao, emitiu_diploma):
        super().__init__(matricula, nome, curso)
        self.data_conclusao = data_conclusao
        self.emitiu_diploma = emitiu_diploma

    def __str__(self):
        return (f"{super().__str__()}, Data de Conclusão: {self.data_conclusao.strftime('%d/%m/%Y')}, "
                f"Emitiu Diploma: {'Sim' if self.emitiu_diploma else 'Não'}")

# Exemplos de uso
def main():
    aluno_cursando = AlunoCursando(
        matricula="12345",
        nome="João Silva",
        curso="Engenharia",
        ano_atual=2024,
        ano_concluir=2026
    )
    
    aluno_concluinte = AlunoConcluinte(
        matricula="67890",
        nome="Maria Oliveira",
        curso="Medicina",
        data_conclusao=datetime(2023, 7, 15),
        emitiu_diploma=True
    )

    alunos = [aluno_cursando, aluno_concluinte]

    for aluno in alunos:
        print(aluno)

if __name__ == "__main__":
    main()
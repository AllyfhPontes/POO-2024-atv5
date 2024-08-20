class Conta_bancaria:
    def __init__(self, titular, cpf, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def mostrar_conta(self):
        return f"Titular: {self.titular}, CPF: {self.cpf}, Saldo: {self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def verificar_saldo(self):
        return self.saldo


class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, numerocc, saldo=0):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f"{self.mostrar_conta()}, Número da Conta Corrente: {self.numerocc}"


class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, rendimento, saldo=0):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        return f"Rendimento: {self.rendimento:.2%}"

    def render(self):
        self.saldo += self.saldo * self.rendimento


def menu():
    contas = {}

    while True:
        opcao = input("1. Criar Conta Corrente\n2. Criar Conta Poupança\n3. Depositar\n4. Sacar\n5. Verificar Saldo\n6. Verificar Rendimento\n7. Aplicar Rendimento\n8. Mostrar Conta\n9. Sair\nEscolha uma opção: ")

        if opcao == "1":
            titular = input("Nome do Titular: ")
            cpf = input("CPF: ")
            numerocc = input("Número da Conta Corrente: ")
            contas[cpf] = Conta_corrente(titular, cpf, numerocc)

        elif opcao == "2":
            titular = input("Nome do Titular: ")
            cpf = input("CPF: ")
            rendimento = float(input("Taxa de Rendimento (ex: 0.05 para 5%): "))
            contas[cpf] = Conta_poupanca(titular, cpf, rendimento)

        elif opcao == "3":
            cpf = input("Informe o CPF: ")
            valor = float(input("Valor para depósito: "))
            if cpf in contas:
                contas[cpf].depositar(valor)

        elif opcao == "4":
            cpf = input("Informe o CPF: ")
            valor = float(input("Valor para saque: "))
            if cpf in contas:
                contas[cpf].sacar(valor)

        elif opcao == "5":
            cpf = input("Informe o CPF: ")
            if cpf in contas:
                print(f"Saldo atual: {contas[cpf].verificar_saldo():.2f}")

        elif opcao == "6":
            cpf = input("Informe o CPF: ")
            if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
                print(contas[cpf].ver_rendimento())

        elif opcao == "7":
            cpf = input("Informe o CPF: ")
            if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
                contas[cpf].render()

        elif opcao == "8":
            cpf = input("Informe o CPF: ")
            if cpf in contas:
                if isinstance(contas[cpf], Conta_corrente):
                    print(contas[cpf].mostrarcc())
                else:
                    print(contas[cpf].mostrar_conta())

        elif opcao == "9":
            break

menu()
class ContaBancaria:
    def __init__(self):
        self.saldo = 5000
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return

        if self.numero_saques >= self.LIMITE_SAQUES:
            print("Você excedeu o limite de saques")
            return

        if valor > self.saldo:
            print("Saldo insuficiente")
            return

        if valor > self.limite:
            print("Você excedeu o limite de saque")
            return

        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1

    def exibir_extrato(self):
        print("\n ==============Extrato==============")
        print("Não foram realizadas movimentações" if not self.extrato else self.extrato)
        print(f"\n Saldo : R$ {self.saldo:.2f}")
        print(" ===================================")


def main():
    conta = ContaBancaria()

    while True:
        print("\n =======Sistema Bancário v.16======")
        opcao = input(
            "[m] menu\n[t] telefones\n[q] sair\n=> "
        ).lower()

        if opcao == "m":
            while True:
                opcao_menu = input(
                    "[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] sair\n=> "
                ).lower()

                if opcao_menu == "d":
                    valor = float(input("Informe o valor de depósito: "))
                    conta.depositar(valor)
                elif opcao_menu == "s":
                    valor = float(input("Informe o valor de saque: "))
                    conta.sacar(valor)
                elif opcao_menu == "e":
                    conta.exibir_extrato()
                elif opcao_menu == "q":
                    break
                else:
                    print("Opção inválida")

        elif opcao == "q":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

entrada = """
[m] menu
[t] telefones
[q] sair
=> """

menu = """
[d] Depositar
[s] sacar
[e] Extrato
[q] sair
=> """

saldo = 5000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
quantia_depositos=0

while True:
    print("\n =======Sistema Bancario v.02======")
    opcao2=input(entrada)
    if opcao2 in ['m','t','q']:
        if opcao2 in ['m','M']:            
            while True:  # Adiciona um loop para retornar ao menu sempre que necessário
                opcao=input(menu)
                if opcao not in ['d', 's', 'e', 'q', 'm']:
                    print('Digite um caracter valido')
                if opcao in ['d','D']: #deposito
                    valor = float(input("Informe o valor de deposito: "))
                    if valor <=0:
                        print("Digite um numero valido")
                    elif valor > 0:
                        saldo += valor
                        extrato += f" Depósito: R$ {valor:.2f}\n"
                        quantia_depositos += 1
                        print(f"O saldo é {saldo}, o extratro é de {extrato},e a qd é {quantia_depositos}")   
                elif opcao in ['s','S']:#saque
                    valor = float(input("Informe o valor de saque: "))
                    excedeu_saldo = valor > saldo
                    excedeu_limite = valor > limite
                    excedeu_saque = numero_saques >= LIMITE_SAQUES
                    if excedeu_saldo:
                        print("Vocé excedeu o seu saldo")
                    elif excedeu_limite:
                        print("Vocé excedeu o seu limite")        
                    elif excedeu_saque:
                        print("Vocé excedeu o seu limite de saque")
                    elif valor<=0:
                        print("Valor invalido")
                    elif valor>0:
                        saldo -=  valor 
                        extrato += (f" Saque: R$ {valor:.2f}\n")
                        numero_saques += 1
                        print(f"O saque é{ valor}, o saldo é de {saldo}")
                    print(f" e lhe resta {LIMITE_SAQUES} saques")
                elif opcao in ['e','E']:# extrato
                    print("\n ==============Extrato==============")
                    print("Não foram realizadas movimentações" if not extrato else extrato)
                    print(f"\n Saldo : R$ {saldo:.2f}")
                    print(" ===================================")                
                elif opcao in ['q','Q']:
                    print( "Obrigado por usa os nossos serviços. ")
                    break
        elif opcao2 in ['q','Q']:
            print( "Obrigado por usa os nossos serviços. ")
            break
        elif opcao2 in ['t','T']: 
            print(" ===================================")
            print("Para regions metropolitanas 4002-8922")
            print("Demais localidades, mude para a cidade")
            print(" ===================================")
    print( "Obrigado por usa os nossos serviços. ")
    break
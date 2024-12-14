menu = """ 
    |============ Sistema Bancário ============|
    |    Escolha entre as seguintes opções:    |
    |    [d] Deposito                          |
    |    [s] Sacar                             |
    |    [e] Extrato                           |
    |    [q] Sair                              |
    |==========================================|
    
    """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(menu.center(20))
    
    opcao = input()

    if opcao == "d":
        print("Indique o valor para deposito\n")
        deposito = float(input())
        extrato += f"Deposito: {deposito}\n"

        print("=============================================")
        print(f"Realizando Deposito no valor de {deposito}")
        print("=============================================")
        
        saldo += deposito
        print(f"Depósito realizado! \nSaldo atual: {saldo}")

    elif opcao == "s":
        if(numero_saques < LIMITE_SAQUES):
            print("Informe o valor de saque:")
            saque = float(input())
            saldo -= saque
            extrato += f"Saque: {saque}\n"
            numero_saques += 1

            print(f"\n=============== EXTRATO ===============")
            print(f"Saque Realizado, Saldo atual{saldo}")
            print("==========================================")


        else:
            print(f"Limite diario de {LIMITE_SAQUES} saques atingido")

    elif opcao == "e":
        print(f"\n=============== EXTRATO ===============")
        print("Não foram realizadas transções" if extrato not in extrato else extrato)
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação ínvalida")





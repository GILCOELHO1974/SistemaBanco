menu = """
Digite a operação desejada!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("DEPÓSITO")

        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

            print("DEPÓSITO EFETUADO COM SUCESSO!")

        else:
            print("Valor do depósito tem que ser maior que zeros!")

    elif opcao == "s":
        print("SAQUE")

        saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("EXTRATO")

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print()
        print("Obrigado por usar nosso sistemas!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

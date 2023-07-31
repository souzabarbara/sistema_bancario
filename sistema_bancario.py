menu = """
[d] Depósito
[s] Saque
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
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if 0 < valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            elif valor_saque > saldo:
                print("Não será possível sacar o dinheiro por falta de saldo.")
            else:
                print(f"Valor de saque inválido. O limite diário de saque é R$ {limite:.2f}.")
        else:
            print("Limite diário de saques atingido. Aguarde até amanhã para sacar novamente.")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Encerrando o programa.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

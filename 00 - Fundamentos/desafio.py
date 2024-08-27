menu = """

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
    match opcao:
        case "q":
            print("Saindo do sistema...")
            break
        case "d":
            try:
                valor = float(input("Qual valor você deseja depositar: R$"))
                if valor<=0:
                    print("Valor inválido! Digite um número positivo!")
                    continue
                saldo+=valor
                print("Depósito efetuado com sucesso!")
                print(f"Saldo atual de R${saldo:.2f}")
                extrato += f"Depósito: R${valor:.2f}\n"
            except ValueError:
                print("Valor inválido! Tente novamente!")
                continue
        case "s":
            try:
                if saldo==0:
                    print("Você não possui saldo para sacar.")
                    continue
                if numero_saques >= LIMITE_SAQUES:
                    print("Você atingiu o limite de saques!")
                    continue
                print(f"Você possui {LIMITE_SAQUES - numero_saques} saques restantes de no máximo R$500.00 cada")
                valor_saque = float(input("Qual valor você deseja depositar: R$"))
                if valor_saque <=0:
                    print("Valor inválido! Digite um número positivo!")
                    continue
                if valor_saque > 500:
                    print("Valor do saque excede o limite!")
                    continue
                if saldo < valor_saque:
                    print("Saldo insuficiente!")
                    continue
                saldo -= valor_saque
                numero_saques += 1
                print("Saque efetuado com sucesso!")
                print(f"Saldo atual de R${saldo:.2f}")
                extrato += f"Saque: R${valor_saque:.2f}\n"
            except ValueError:
                print("Valor inválido! Tente novamente!")
                continue
        case "e":
            if not extrato:
                print("Você não realizou nenhuma operação.")
            else:
                print("Extrato:")
                print(extrato,end="")
                print(f"Seu saldo atual é de R${saldo:.2f}")
        case _:
            print("Opção invalida, tente novamente.")

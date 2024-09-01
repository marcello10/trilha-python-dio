from datetime import datetime
menu = """
[c]  Criar usuário
[cc] Criar conta corrente
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
contas = []
operacoes_bancarias = []
extratos = []
def saque(*,saldo,valor,extrato,numero_saques,limite_saques):
    try:
        if saldo==0:
            print("Você não possui saldo para sacar.")
            return saldo, extrato
        if numero_saques >= limite_saques:
            print("Você atingiu o limite de saques!")
            return saldo, extrato
        print(f"Você possui {limite_saques - numero_saques -1} saques restantes de no máximo R$500.00 cada")
        if valor <=0:
            print("Valor inválido! Digite um número positivo!")
            return saldo, extrato
        if valor > 500:
            print("Valor do saque excede o limite!")
            return saldo, extrato
        if saldo < valor:
            print("Saldo insuficiente!")
            return saldo, extrato
        saldo -= valor
        print("Saque efetuado com sucesso!")
        print(f"Saldo atual de R${saldo:.2f}")
        extrato.append(f"Saque: R${valor:.2f}")
        return saldo, extrato
    except ValueError:
        print("Valor inválido! Tente novamente!")
        return False
def deposito(saldo,valor,extrato,/):
    try:
        if valor<=0:
            print("Valor inválido! Digite um número positivo!")
        saldo+=valor
        print("Depósito efetuado com sucesso!")
        print(f"Saldo atual de R${saldo:.2f}")
        extrato.append(f"Depósito: R${valor:.2f}")
    except ValueError:
        print("Valor inválido! Tente novamente!")
    return saldo, extrato
def exibir_extrato(saldo,/,*,extrato):
    if not extrato:
        print(f"Seu saldo atual é de R${saldo:.2f}")
        print("Você não realizou nenhuma operação.")
    else:
        print("Extrato:")
        print("\n".join(extratos))
        print(f"Seu saldo atual é de R${saldo:.2f}")
    return extrato
def criar_usuario():
    nome = input("Qual o nome do novo usuário: ")
    data_nascimento = input("Qual a data de nascimento do usuário? ex: 04/04/1999\n")
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        print("Data de nascimento inválida! Tente novamente!")
        return False
    cpf = input("Qual o CPF do novo usuário: ")
    logradouro = input("Informe o logradouro do usuário: ")
    numero_log = input("Informe o número do logradouro do usuário: ")
    bairro = input("Informe o bairro do usuário: ")
    cidade_estado = input("Informe a cidade e estado do usuário (ex: São Paulo-SP): ")
    if lista_usuarios:
        for usuario in lista_usuarios:
            if usuario.get("cpf") == cpf:
                print("Já existe um usuário com esse CPF!")
                return False
    usuario  = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": f"{logradouro} - {numero_log} - {bairro} - {cidade_estado}"
    }
    lista_usuarios.append(usuario)
    return True
def criar_conta_corrente(cpf_usuario):
    agencia = "0001"
    numero_conta = 1
    cpf = cpf_usuario
    existe_usuario = False
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            existe_usuario = True
    if not existe_usuario:
        print("Usuário não encontrado!")
        return False
    if contas:
        ultimo_numero  = contas[-1].get("numero_conta")
        numero_conta = ultimo_numero + 1
    conta = {
        "agencia":agencia,
        "numero_conta":numero_conta,
        "usuario":cpf
    }
    contas.append(conta)
    return conta
while True:
    opcao = input(menu)
    match opcao:
        case 'c':
            usuario_criado = criar_usuario()
            if not usuario_criado:
                continue
            print(lista_usuarios[-1])
        case 'cc':
            cpf = input("digite o cpf do usuario: ")
            cc_criada = criar_conta_corrente(cpf)
            if cc_criada:
                print("Conta corrente criada com sucesso!")
                print(cc_criada)   
        case 'd':
            if not saldo:
                saldo = float(input("Saldo atual de R$"))
                extratos.append(f"Saldo inicial de R${saldo:.2f}")
            valor = float(input("Depósito de R$"))
            saldo_novo,extrato_novo = deposito(saldo,valor,extratos)
            saldo = saldo_novo
        case 's':
            valor_saque = float(input("Valor do saque R$"))
            saldo_novo, extrato = saque(saldo=saldo,valor=valor_saque,extrato=extratos,
                numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
            if saldo_novo != saldo:
                numero_saques+=1
                saldo = saldo_novo
        case 'e':
            exibir_extrato(saldo,extrato=extratos)
        case "q":
            print("Saindo do sistema...")
            break 
        case _:
            print("Opção invalida, tente novamente.")

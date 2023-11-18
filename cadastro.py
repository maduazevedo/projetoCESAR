print("LucidApp\n")

def cadastrar_empresa():
    nome = input("Nome da empresa: ")
    cnpj = input("CNPJ: ")
    senha = input("Digite a senha: ")

    with open("empresas.txt", "a") as arquivo_empresas:
        arquivo_empresas.write(f"Empresa  {nome} \n CNPJ {cnpj}\n Senha {senha}\n")
        arquivo.close()
    print("Cadastro de empresa realizado com sucesso!")

def cadastrar_cliente():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite a senha: ")

    with open("clientes.txt", "a") as arquivo_clientes:
        arquivo_clientes.write(f"Nome do cliente {nome}\n E-mail do cliente {email}, Senha do cliente {senha}\n")

    print("Cadastro de cliente realizado com sucesso!")

def escolher_tipo_cadastro():
    tipo_cadastro = input("Deseja cadastrar uma EMPRESA ou um CLIENTE? ").lower()


    if tipo_cadastro == "empresa":
        cadastrar_empresa()
    elif tipo_cadastro == "cliente":
        cadastrar_cliente()
    else:
        print("Opção inválida. Escolha entre 'empresa' ou 'cliente'.")

# Chama a função para escolher o tipo de cadastro
escolher_tipo_cadastro()

if escolher_tipo_cadastro==True:
    print("Abrir menu")
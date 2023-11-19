print("LucidApp\n")

#funções para cadastro da empresa CRUD

def create_usuario():
    empresa = input("Digite o nome do seu empreendimento: ")
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite a senha : ")
    print(f'Olá {empresa}, estamos felizes em te ter conosco!')
    
    with open("usuarios.txt", "a") as arquivo:
        #incrementa
        linha = (f'\n{empresa} CNPJ: {cnpj} Senha: {senha}\n')
        arquivo.write(linha)
        print("Cadastro realizado com sucesso!")

def login():
    cnpj = input("CNPJ: ")
    senha = input("Senha: ")
    encontrado = False

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(':')
            if len(dados) == 3:  # Verifica se há três campos (empresa, CNPJ, senha)
                empresa, cnpj_armazenado, senha_armazenada = dados
                if cnpj == cnpj_armazenado and senha == senha_armazenada:
                    encontrado = True
                    print("Login bem-sucedido!")
                    break
    if not encontrado:
        print("CNPJ ou senha incorretos. Caso não tenha cadastro, realize-o.")
        
        

def read_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            if usuario:
                print("Lista de usuários cadastrados:")
                for usuario in usuarios:
                    print(usuario, "\n")
            else:
                print("Não há usuários cadastrados.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


def update_usuario():
    cnpj = input("Digite o CNPJ que deseja atualizar: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            #substitui
            with open("usuarios.txt", "w") as arquivo:
                usuario_encontrado = False
                for linha in linhas:
                    if cnpj in linhas:
                        usuario_encontrado = True
                        empresa = input("Digite o novo nome: ")
                        senha = input("Digite a nova senha: ")
                        #atualização:
                        linha = (f'\n {empresa} CNPJ: {cnpj} Senha: {senha}\n')
                        arquivo.write(linha)
                        print("Informações atualizadas com sucesso!")
                    else:
                        arquivo.write(linha)
                        #nao deixa as informações das linhas serem apagadas
        if not usuario_encontrado:
            print("Usuário não encontrado.")
            
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


def delet_usuario():
    cnpj = input("Digite o CNPJ que deseja deletar: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            with open("usuarios.txt", "w") as arquivo:
                usuario_encontrado = False
            for linha in linhas:
                if cnpj in linha:
                    usuario_encontrado = True
                    print(f"Empresa com CNPJ {cnpj} deletada com sucesso!")
                else:
                    arquivo.write(linha)
                    #nao deixa o arquivo ser apagado
        if not usuario_encontrado:
            print("CNPJ não encontrado.")
            
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")








# MENU PRINCIPAL QUE INTERAGE COM O CRUD DE EMPRESAS E USER
while True:
    print("\nEscolha uma opção:")
    print("1. Cadastro de Usuário")
    print("2. Login de Usuário")
    print("3. Configurações do Usuário")
    print("4. Menu")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        create_usuario()
        
    elif opcao == "2":
        login()

    elif opcao == "3":
        while True:
            print("\nEscolha uma opção para usuários:")
            print("6. Listar Usuários")
            print("7. Atualizar Usuário")
            print("8. Deletar Usuário")
            print("9. Voltar")
            
            opcao_usuarios = input("Opção: ")
            
            if opcao_usuarios == "6":
                create_usuario()
            elif opcao_usuarios == "7":
                update_usuario()
            elif opcao_usuarios == "8":
                delet_usuario()
            elif opcao_usuarios == "9":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Escolha uma opção de 6 a 9.")
        
    elif opcao == "4":
        print("menu de carlos")


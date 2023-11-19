print("LucidApp\n")

#funções para cadastro da empresa CRUD

def create_empresa():
    cnpj = input("Digite o CNPJ da empresa: ")
    empresa = input("Digite o nome da empresa: ")
    senha = input("Digite a senha da empresa: ")
    
    with open("empresas.txt", "a") as arquivo:
        #incrementa
        linha = (f'\nCNPJ: {cnpj} Empresa: {empresa} Senha: {senha}\n')
        arquivo.write(linha)
        print("Empresa cadastrada com sucesso!")


def read_empresas():
    try:
        with open("empresas.txt", "r") as arquivo:
            empresas = arquivo.readlines()
            if empresas:
                print("Lista de empresas cadastradas:")
                for empresa in empresas:
                    print(empresa, "\n")
            else:
                print("Não há empresas cadastradas.")
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")


def update_empresa():
    cnpj = input("Digite o CNPJ da empresa que deseja atualizar: ")
    try:
        with open("empresas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            #substitui
            with open("empresas.txt", "w") as arquivo:
                empresa_encontrada = False
                for linha in linhas:
                    if cnpj in linhas:
                        empresa_encontrada = True
                        empresa = input("Digite o novo nome: ")
                        senha = input("Digite a nova senha: ")
                        #atualização:
                        linha = (f'\nCNPJ: {cnpj} Empresa: {empresa} Senha: {senha}\n')
                        arquivo.write(linha)
                        print("Empresa atualizada com sucesso!")
                    else:
                        arquivo.write(linha)
                        #nao deixa as informações das linhas serem apagadas
        if not empresa_encontrada:
            print("Empresa não encontrada.")
            
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")


def delet_empresa():
    cnpj = input("Digite o CNPJ da empresa que deseja deletar: ")
    try:
        with open("empresas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            with open("empresas.txt", "w") as arquivo:
                empresa_encontrada = False
            for linha in linhas:
                if cnpj in linha:
                    empresa_encontrada = True
                    print(f"Empresa com CNPJ {cnpj} deletada com sucesso!")
                else:
                    arquivo.write(linha)
                    #nao deixa o arquivo ser apagado
        if not empresa_encontrada:
            print("Empresa não encontrada.")
            
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")

















# Funções para cadastro de usuários CRUD
def create_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    senha1 = input("Digite a senha do usuário: ")
    with open("usuarios.txt", "a") as arquivo:
        #incremento
        linha = (f"Nome: {nome}, E-mail: {email}, Senha: {senha1}\n")
        arquivo.write(linha)
        print("Seja bem vindo(a)", nome)


def read_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            if usuarios:
                print("Lista de usuários cadastrados:")
                for usuario in usuarios:
                    print("Usuários LucidApp:", usuario)
            else:
                print("Não há usuários cadastrados.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


def update_usuario():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            with open("usuarios.txt", "w") as arquivo:
                usuario_encontrado = False
                for linha in linhas:
                    if email in linha:
                        usuario_encontrado = True
                        nome = input("Digite o novo nome: ")
                        email= input("Insira seu novo email: ")
                        senha = input("Digite a nova senha: ")
                        linha = (f"Nome: {nome}, E-mail: {email}, Senha: {senha}\n")
                        arquivo.write(linha)
                        print("Suas informações foram atualizadas com sucesso!")
                    else:
                        arquivo.write(linha)
            if not usuario_encontrado:
                print("Usuário não encontrado.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


def delet_usuario():
    
    email = input("Digite o e-mail do usuário que deseja deletar: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            with open("usuarios.txt", "w") as arquivo:
                usuario_encontrado = False
                for linha in linhas:
                    if email in linha:
                        usuario_encontrado = True
                        print(f"Usuário com e-mail {email} deletado com sucesso!")
                    else:
                        arquivo.write(linha)
        if not usuario_encontrado:
            print("Usuário não encontrado")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        
        
        
        
        
        
        
        


# MENU PRINCIPAL QUE INTERAGE COM O CRUD DE EMPRESAS E USER
while True:
    print("\nEscolha uma opção:")
    print("1. Cadastro de Usuário")
    print("2. Configurações do Usuário")
    print("3. Menu")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        create_usuario
        
    elif opcao == "2":
        create_usuario()
        
    elif opcao == "3":
        while True:
            print("\nEscolha uma opção para empresas:")
            print("6. Listar Empresas")
            print("7. Atualizar Empresa")
            print("8. Deletar Empresa")
            print("9. Voltar")
            
            opcao_empresas = input("Opção: ")
            
            if opcao_empresas == "6":
                read_empresas()
            elif opcao_empresas == "7":
                update_empresa()
            elif opcao_empresas == "8":
                delet_empresa()
            elif opcao_empresas == "9":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Escolha uma opção de 6 a 9.")
                
    elif opcao == "4":
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
        
    elif opcao == "5":
        print("menu de carlos")


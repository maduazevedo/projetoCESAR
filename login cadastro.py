

print("LucidApp\n")



#função create Crud

def create_usuario():
    empresa = input("Digite o nome do seu empreendimento: ")
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite a senha (apenas 3 caracteres especiais): ")
    print(f'Olá {empresa}, estamos felizes em te ter conosco!')
    
    with open("usuarios.txt", "a") as arquivo:
        #incrementa
        linha = (f'\n{empresa} {cnpj} {senha}\n')
        arquivo.write(linha)
        print("\nCadastro realizado com sucesso!")


#funçao login

def login():
    with open("usuarios.txt", "r") as arquivo:
        empresa = input("Digite o nome do seu empreendimento: ")
        cnpj = input("Digite o CNPJ: ")
        senha = input("Digite a senha (apenas 3 caracteres especiais): ")
        for linhas in arquivo:
            linhas=arquivo.readlines()
            for linha in linhas:
                info=linha.split()
    
        if (cnpj and senha) in info:
            print(f'\nBem vindo (a), {empresa}!\n')
        else:
            print("\nInformação errada\n")


#função read cRud

def read_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            if usuarios:
                print("\nLista de usuários cadastrados:")
                for usuario in usuarios:
                    print(usuario, "\n")
            else:
                print("\nNão há usuários cadastrados.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


#função update crUd

def update_usuario():
    cnpj = input("Digite o CNPJ que deseja atualizar: ")
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            #substitui
            with open("usuarios.txt", "w") as arquivo:
                usuario_encontrado = False
                for linha in linhas:
                    if cnpj in linha:
                        usuario_encontrado = True
                        empresa = input("Digite o novo nome: ")
                        senha = input("Digite a nova senha: ")
                        #atualização:
                        linha = (f'{empresa} {cnpj} {senha}\n')
                        arquivo.write(linha)
                        print("\nInformações atualizadas com sucesso!")
                    else:
                        arquivo.write(linha)
                        #nao deixa as informações das linhas serem apagadas
        if not usuario_encontrado:
            print("\nUsuário não encontrado.")
            
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        arquivo.close()
        
        
#função delet cruD

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
                    print(f"\nEmpresa com CNPJ {cnpj} deletada com sucesso!")
                else:
                    arquivo.write(linha)
                    #nao deixa o arquivo ser apagado
        if not usuario_encontrado:
            print("CNPJ não encontrado.")
            
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")



# MENU PRINCIPAL QUE INTERAGE COM AS FUNÇÕES

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastro de Usuário")
    print("2. Login de Usuário")
    print("3. Configurações do Usuário")
    print("4. Menu")
    
    escolha = input("Opção: ")
    
    if escolha == "1":
        create_usuario()
        
    elif escolha == "2":
        login()

    elif escolha == "3":
        while True:
            print("\nEscolha uma opção para usuários:")
            print("6. Listar Usuários")
            print("7. Atualizar Usuário")
            print("8. Deletar Usuário")
            print("9. Voltar")
            
            escolha_usuarios = input("Opção: ")
            
            if escolha_usuarios == "6":
                read_usuarios()
            elif escolha_usuarios == "7":
                update_usuario()
            elif escolha_usuarios == "8":
                delet_usuario()
            elif escolha_usuarios == "9":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Escolha uma opção de 6 a 9.")
        
    elif escolha == "4":
        print("menu de carlos")
        
    #FALTA INTEGRAR ESSE COD COM O MENU
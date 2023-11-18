def criar_empresa():
    cnpj = input("Digite o CNPJ da empresa: ")
    nome = input("Digite o nome da empresa: ")
    senha = input("Digite a senha da empresa: ")

    with open("empresas.txt", "a") as arquivo:
        arquivo.write(f"CNPJ: {cnpj}, Nome: {nome}, Senha: {senha}\n")

    print("Empresa cadastrada com sucesso!")

def listar_empresas():
    try:
        with open("empresas.txt", "r") as arquivo:
            empresas = arquivo.readlines()
            if empresas:
                print("Lista de empresas cadastradas:")
                for empresa in empresas:
                    print(empresa)
            else:
                print("Não há empresas cadastradas.")
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")

def atualizar_empresa():
    cnpj = input("Digite o CNPJ da empresa que deseja atualizar: ")

    try:
        with open("empresas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("empresas.txt", "w") as arquivo:
            empresa_encontrada = False
            for linha in linhas:
                if f"CNPJ: {cnpj}" in linha:
                    empresa_encontrada = True
                    novo_nome = input("Digite o novo nome: ")
                    nova_senha = input("Digite a nova senha: ")
                    arquivo.write(f"CNPJ: {cnpj}, Nome: {novo_nome}, Senha: {nova_senha}\n")
                    print("Empresa atualizada com sucesso!")
                else:
                    arquivo.write(linha)
            if not empresa_encontrada:
                print("Empresa não encontrada.")
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")

def deletar_empresa():
    cnpj = input("Digite o CNPJ da empresa que deseja deletar: ")

    try:
        with open("empresas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("empresas.txt", "w") as arquivo:
            empresa_encontrada = False
            for linha in linhas:
                if f"CNPJ: {cnpj}" in linha:
                    empresa_encontrada = True
                    print(f"Empresa com CNPJ {cnpj} deletada com sucesso!")
                else:
                    arquivo.write(linha)
            if not empresa_encontrada:
                print("Empresa não encontrada.")
    except FileNotFoundError:
        print("Arquivo de empresas não encontrado.")

# Funções para cadastro de usuários
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    senha = input("Digite a senha do usuário: ")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}, E-mail: {email}, Senha: {senha}\n")

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            if usuarios:
                print("Lista de usuários cadastrados:")
                for usuario in usuarios:
                    print(usuario)
            else:
                print("Não há usuários cadastrados.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

def atualizar_usuario():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("usuarios.txt", "w") as arquivo:
            usuario_encontrado = False
            for linha in linhas:
                if f"E-mail: {email}" in linha:
                    usuario_encontrado = True
                    novo_nome = input("Digite o novo nome: ")
                    nova_senha = input("Digite a nova senha: ")
                    arquivo.write(f"Nome: {novo_nome}, E-mail: {email}, Senha: {nova_senha}\n")
                    print("Usuário atualizado com sucesso!")
                else:
                    arquivo.write(linha)
            if not usuario_encontrado:
                print("Usuário não encontrado.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

def deletar_usuario():
    email = input("Digite o e-mail do usuário que deseja deletar: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("usuarios.txt", "w") as arquivo:
            usuario_encontrado = False
            for linha in linhas:
                if f"E-mail: {email}" in linha:
                    usuario_encontrado = True
                    print(f"Usuário com e-mail {email} deletado com sucesso!")
                else:
                    arquivo.write(linha)
            if not usuario_encontrado:
                print("Usuário não encontrado.")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

# Menu principal para interagir com o CRUD de empresas e usuários
while True:
    print("\nEscolha uma opção:")
    print("1. Cadastro de Empresa")
    print("2. CRUD de Empresas")
    print("3. Cadastro de Usuário")
    print("4. CRUD de Usuários")
    print("5. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        criar_empresa()
    elif opcao == "2":
        while True:
            print("\nEscolha uma opção para empresas:")
            print("1. Listar Empresas")
            print("2. Atualizar Empresa")
            print("3. Deletar Empresa")
            print("4. Voltar")

            opcao_empresas = input("Opção: ")

            if opcao_empresas == "1":
                listar_empresas()
            elif opcao_empresas == "2":
                atualizar_empresa()
            elif opcao_empresas == "3":
                deletar_empresa()
            elif opcao_empresas == "4":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Escolha uma opção de 1 a 4.")
    elif opcao == "3":
        criar_usuario()
    elif opcao == "4":
        while True:
            print("\nEscolha uma opção para usuários:")
            print("1. Listar Usuários")
            print("2. Atualizar Usuário")
            print("3. Deletar Usuário")
            print("4. Voltar")

            opcao_usuarios = input("Opção: ")

            if opcao_usuarios == "1":
                listar_usuarios()
            elif opcao_usuarios == "2":
                atualizar_usuario()
            elif opcao_usuarios == "3":
                deletar_usuario()
            elif opcao_usuarios
            
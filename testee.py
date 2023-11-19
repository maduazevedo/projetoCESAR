def login():
    try:
        with open("usuarios.txt", "r") as arquivo:
            empresa = input("Digite o nome do seu empreendimento: ")
            cnpj = input("Digite o CNPJ: ")
            senha = input("Digite a senha (apenas letras): ")
            linhas=arquivo.readline()
            for linha in linhas:
                linha=linhas.split()
                
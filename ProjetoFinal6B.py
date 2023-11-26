import os
import datetime
import matplotlib.pyplot as plt
import numpy as np

def create_usuario():
    empresa = input("Digite a Razão Social: ")
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite a senha (apenas 3 caracteres especiais): ")
    print(f'Olá {empresa}, estamos felizes em te ter conosco!')

    arquivo_nome = f"{cnpj}_usuario.txt"

    with open(arquivo_nome, "w") as arquivo:
        linha = f'{empresa} {cnpj} {senha}\n'
        arquivo.write(linha)

    print("\nCadastro realizado com sucesso!")

def login():
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite a senha (apenas 3 caracteres especiais): ")

    arquivo_nome = f"{cnpj}_usuario.txt"

    try:
        with open(arquivo_nome, "r") as arquivo:
            info = arquivo.readline().split()

        if (cnpj and senha) in info:
            print(f'\nBem-vindo (a)! Login realizado.\n')
        else:
            print("\nInformação errada\n")

    except FileNotFoundError:
        print(f"\nUsuário com CNPJ {cnpj} não encontrado.")

def read_usuarios():
    for arquivo_nome in os.listdir("."):
        if arquivo_nome.endswith("_usuario.txt"):
            try:
                with open(arquivo_nome, "r") as arquivo:
                    dados_usuario = arquivo.read()
                    print(dados_usuario, "\n")
            except FileNotFoundError:
                print(f"Arquivo {arquivo_nome} não encontrado.")

def update_usuario():
    cnpj = input("Digite o CNPJ que deseja atualizar: ")

    arquivo_nome = f"{cnpj}_usuario.txt"

    try:
        with open(arquivo_nome, "r") as arquivo_leitura:
            linhas = arquivo_leitura.readlines()

        with open(arquivo_nome, "w") as arquivo_escrita:
            usuario_encontrado = False
            for linha in linhas:
                if cnpj in linha:
                    usuario_encontrado = True
                    empresa = input("Digite o novo nome: ")
                    senha = input("Digite a nova senha: ")
                    linha = f'{empresa} {cnpj} {senha}\n'
                    arquivo_escrita.write(linha)
                    print("\nInformações atualizadas com sucesso!")
                else:
                    arquivo_escrita.write(linha)

        if not usuario_encontrado:
            print("\nUsuário não encontrado.")

    except FileNotFoundError:
        print(f"Arquivo {arquivo_nome} não encontrado.")

def delet_usuario():
    cnpj = input("Digite o CNPJ que deseja deletar: ")
    arquivo_nome = f"{cnpj}_usuario.txt"

    try:
        if os.path.exists(arquivo_nome):
            os.remove(arquivo_nome)
            print(f"\nEmpresa com CNPJ {cnpj} deletada com sucesso!")
        else:
            print("CNPJ não encontrado.")

    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")


def adicionar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ")
    quantidade_maxima = int(input("Digite a quantidade máxima: "))
    quantidade_inicial = int(input("Digite a quantidade inicial (opcional, pressione Enter para 0): ") or 0)

    data_validade = None
    if quantidade_inicial != 0:
        data_validade = input("Digite a data de validade (formato YYYY-MM-DD): ")

    produto = {
        "nome": nome_produto,
        "quantidade_maxima": quantidade_maxima,
        "quantidade_atual": quantidade_inicial,
        "data_validade": datetime.datetime.strptime(data_validade, "%Y-%m-%d").date() if data_validade else None
    }

    estoque.append(produto)
    print(f"Produto {produto['nome']} adicionado ao estoque.")


def adicionar_quantidade_produto(estoque, nome_produto, quantidade, data_validade=None):
    for produto in estoque:
        if produto["nome"] == nome_produto:
            if data_validade:
                produto["data_validade"] = datetime.datetime.strptime(data_validade, "%Y-%m-%d").date()

            produto["quantidade_atual"] += quantidade
            print(f"Entrada de {quantidade} unidades de {produto['nome']} registrada.")

            if produto["quantidade_atual"] > produto["quantidade_maxima"]:
                print(f"ALERTA: A quantidade máxima para {produto['nome']} foi atingida!")

            break
    else:
        print(f"Erro: O produto {nome_produto} não existe no estoque.")

def registrar_saida_produto(estoque, nome_produto, quantidade):
    for produto in estoque:
        if produto["nome"] == nome_produto:
            if produto["quantidade_atual"] >= quantidade:
                produto["quantidade_atual"] -= quantidade
                print(f"Saída de {quantidade} unidades de {produto['nome']} registrada.")
            else:
                print("Erro: Quantidade de saída maior que a quantidade atual.")
            break
    else:
        print(f"Erro: O produto {nome_produto} não existe no estoque.")

def exibir_estoque(estoque):
    print("\nEstado atual do estoque:")
    for produto in estoque:
        print(f"\nProduto: {produto['nome']}")
        print(f"Quantidade Máxima: {produto['quantidade_maxima']}")
        print(f"Quantidade Atual: {produto['quantidade_atual']}")
        print(f"Data de Validade: {produto['data_validade']}")
        verificar_validade(produto)

    plotar_grafico_barras(estoque)

def verificar_validade(produto):
    if produto["data_validade"] and datetime.date.today() >= produto["data_validade"]:
        print(f"ALERTA: A data de validade para {produto['nome']} foi atingida!")

def plotar_grafico_barras(estoque):
    nomes_produtos = [produto["nome"] for produto in estoque]
    quantidades_maximas = [produto["quantidade_maxima"] for produto in estoque]
    quantidades_atuais = [produto["quantidade_atual"] for produto in estoque]

    x = np.arange(len(nomes_produtos))
    largura_barra = 0.35

    fig, ax = plt.subplots()
    barras_maximas = ax.bar(x - largura_barra / 2, quantidades_maximas, largura_barra, label='Quantidade Máxima')
    barras_atuais = ax.bar(x + largura_barra / 2, quantidades_atuais, largura_barra, label='Quantidade Atual')

    ax.set_xlabel('Produtos')
    ax.set_ylabel('Quantidades')
    ax.set_title('Quantidade Máxima e Atual por Produto')
    ax.set_xticks(x)
    ax.set_xticklabels(nomes_produtos)
    ax.legend()

    adicionar_rotulos_barras(ax, barras_maximas)
    adicionar_rotulos_barras(ax, barras_atuais)

    plt.show()

def adicionar_rotulos_barras(ax, barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

def obter_input(mensagem):
    return input(mensagem)

if __name__ == "__main__":
    estoque = []

    while True:
        print("\n1. Cadastro de Usuário")
        print("2. Login de Usuário")
        print("3. Configurações do Usuário")
        print("4. Cadastrar produto ao estoque")
        print("5. Adicionar quantidade a um produto")
        print("6. Registrar saída de um produto")
        print("7. Visualizar estado atual do estoque")
        print("8. Sair")

        escolha = obter_input("Escolha uma opção (1/2/3/4/5/6/7/8): ")

        if escolha == "1":
            create_usuario()

        elif escolha == "2":
            login()

        elif escolha == "3":
            while True:
                print("\nEscolha uma opção para usuários:")
                print("1. Listar Usuários")
                print("2. Atualizar Usuário")
                print("3. Deletar Usuário")
                print("4. Voltar")

                escolha_usuarios = input("Opção: ")

                if escolha_usuarios == "1":
                    read_usuarios()
                elif escolha_usuarios == "2":
                    update_usuario()
                elif escolha_usuarios == "3":
                    delet_usuario()
                elif escolha_usuarios == "4":
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Escolha uma opção de 1 a 4.")

        elif escolha == "4":
            adicionar_produto(estoque)

        elif escolha == "5":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser adicionada: "))
            data_validade = obter_input("Digite a data de validade (formato YYYY-MM-DD) ou pressione Enter para nenhum: ")
            adicionar_quantidade_produto(estoque, nome_produto, quantidade, data_validade)

        elif escolha == "6":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser registrada como saída: "))
            registrar_saida_produto(estoque, nome_produto, quantidade)

        elif escolha == "7":
            exibir_estoque(estoque)

        elif escolha == "8":
            break

        else:
            print("Escolha inválida. Tente novamente.")

import datetime
import matplotlib.pyplot as plt
import numpy as np


def create_usuario():
    empresa = input("Digite a Razão Social: ")
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite a senha (apenas 3 caracteres especiais): ")
    print(f'Olá {empresa}, estamos felizes em te ter conosco!')


    arquivo_nome = f"{cnpj}_usuario.txt"

    with open(arquivo_nome, "a") as arquivo:
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

class Produto:
    def __init__(self, nome, quantidade_maxima, data_validade=None, quantidade_inicial=0):
        self.nome = nome
        self.quantidade_maxima = quantidade_maxima
        self.quantidade_atual = quantidade_inicial
        self.data_validade = datetime.datetime.strptime(data_validade, "%Y-%m-%d").date() if data_validade else None

    def adicionar_quantidade(self, quantidade, data_validade=None):
        if data_validade:
            self.data_validade = datetime.datetime.strptime(data_validade, "%Y-%m-%d").date()

        self.quantidade_atual >= quantidade
        if self.quantidade_atual > self.quantidade_maxima:
            print(f"ALERTA: A quantidade máxima para {self.nome} foi atingida!")

    def registrar_saida(self, quantidade):
        if self.quantidade_atual >= quantidade:
            self.quantidade_atual -= quantidade
            print(f"Saída de {quantidade} unidades de {self.nome} registrada.")
        else:
            print("Erro: Quantidade de saída maior que a quantidade atual.")

    def verificar_validade(self):
        if self.data_validade and datetime.date.today() >= self.data_validade:
            print(f"ALERTA: A data de validade para {self.nome} foi atingida!")

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome not in self.produtos:
            if produto.quantidade_atual > 0:
                data_validade = obter_input(f"Digite a data de validade para {produto.nome} (formato YYYY-MM-DD): ")
                produto.adicionar_quantidade(produto.quantidade_atual, data_validade)
            self.produtos[produto.nome] = produto
            print(f"Produto {produto.nome} adicionado ao estoque.")
        else:
            print(f"Erro: O produto {produto.nome} já existe no estoque.")

    def adicionar_quantidade_produto(self, nome_produto, quantidade, data_validade=None):
        if nome_produto in self.produtos:
            self.produtos[nome_produto].adicionar_quantidade(quantidade, data_validade)
        else:
            print(f"Erro: O produto {nome_produto} não existe no estoque.")

    def registrar_saida_produto(self, nome_produto, quantidade):
        if nome_produto in self.produtos:
            self.produtos[nome_produto].registrar_saida(quantidade)
        else:
            print(f"Erro: O produto {nome_produto} não existe no estoque.")

    def exibir_estoque(self):
        print("\nEstado atual do estoque:")
        for produto in self.produtos.values():
            print(f"\nProduto: {produto.nome}")
            print(f"Quantidade Máxima: {produto.quantidade_maxima}")
            print(f"Quantidade Atual: {produto.quantidade_atual}")
            print(f"Data de Validade: {produto.data_validade}")
            produto.verificar_validade()


        self.plotar_grafico_barras()

    def plotar_grafico_barras(self):
        nomes_produtos = [produto.nome for produto in self.produtos.values()]
        quantidades_maximas = [produto.quantidade_maxima for produto in self.produtos.values()]
        quantidades_atuais = [produto.quantidade_atual for produto in self.produtos.values()]

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


        self.adicionar_rotulos_barras(ax, barras_maximas)
        self.adicionar_rotulos_barras(ax, barras_atuais)

        plt.show()

    def adicionar_rotulos_barras(self, ax, barras):
        for barra in barras:
            altura = barra.get_height()
            ax.annotate('{}'.format(altura),
                        xy=(barra.get_x() + barra.get_width() / 2, altura),
                        xytext=(0, 3),  # offset vertical
                        textcoords="offset points",
                        ha='center', va='bottom')


def obter_input(mensagem):
    return input(mensagem)


if __name__ == "__main__":
    estoque = Estoque()

    while True:
        
        print("\n1. Cadastro de Usuário")
        print("2. Login de Usuário")
        print("3. Configurações do Usuário")
        print("4. Adicionar produto ao estoque")
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
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade_maxima = int(obter_input("Digite a quantidade máxima: "))
            quantidade_inicial = int(obter_input("Digite a quantidade inicial (opcional, pressione Enter para 0): ") or 0)

            produto = Produto(nome_produto, quantidade_maxima, quantidade_inicial=quantidade_inicial)
            estoque.adicionar_produto(produto)

        elif escolha == "5":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser adicionada: "))
            data_validade = obter_input("Digite a data de validade (formato YYYY-MM-DD) ou pressione Enter para nenhum: ")
            estoque.adicionar_quantidade_produto(nome_produto, quantidade, data_validade)

        elif escolha == "6":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser registrada como saída: "))
            estoque.registrar_saida_produto(nome_produto, quantidade)

        elif escolha == "7":
            estoque.exibir_estoque()

        elif escolha == "8":
            break

        else:
            print("Escolha inválida. Tente novamente.")
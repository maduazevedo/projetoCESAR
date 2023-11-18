import datetime
import matplotlib.pyplot as plt
import numpy as np

class Produto:
    def __init__(self, nome, quantidade_maxima, data_validade=None, quantidade_inicial=0):
        self.nome = nome
        self.quantidade_maxima = quantidade_maxima
        self.quantidade_atual = quantidade_inicial
        self.data_validade = datetime.datetime.strptime(data_validade, "%Y-%m-%d").date() if data_validade else None

    def adicionar_quantidade(self, quantidade, data_validade=None):
        if data_validade:
            self.data_validade = datetime.datetime.strptime(data_validade, "%Y-%m-%d").date()

        self.quantidade_atual += quantidade
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

        # Adicionando código para exibir gráfico de barras
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

        # Adicionando rótulos nas barras
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

# Função para obter entrada do usuário
def obter_input(mensagem):
    return input(mensagem)

# Exemplo de uso interativo do programa
if __name__ == "__main__":
    estoque = Estoque()

    while True:
        print("\n1. Adicionar produto ao estoque")
        print("2. Adicionar quantidade a um produto")
        print("3. Registrar saída de um produto")
        print("4. Visualizar estado atual do estoque")
        print("5. Sair")

        escolha = obter_input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "1":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade_maxima = int(obter_input("Digite a quantidade máxima: "))
            quantidade_inicial = int(int(obter_input("Digite a quantidade inicial (opcional, pressione Enter para 0): ") or 0)/2)

            produto = Produto(nome_produto, quantidade_maxima, quantidade_inicial=quantidade_inicial)
            estoque.adicionar_produto(produto)

        elif escolha == "2":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser adicionada: "))
            data_validade = obter_input("Digite a data de validade (formato YYYY-MM-DD) ou pressione Enter para nenhum: ")
            estoque.adicionar_quantidade_produto(nome_produto, quantidade, data_validade)

        elif escolha == "3":
            nome_produto = obter_input("Digite o nome do produto: ")
            quantidade = int(obter_input("Digite a quantidade a ser registrada como saída: "))
            estoque.registrar_saida_produto(nome_produto, quantidade)

        elif escolha == "4":
            estoque.exibir_estoque()

        elif escolha == "5":
            break

        else:
            print("Escolha inválida. Tente novamente.")


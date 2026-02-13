from produtos import Produto
from banco_produtos import BancoProdutos
from rich import print
from rich.text import Text
from rich.panel import Panel
import os
import json

BP = BancoProdutos()
caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'produtos.json')

class Carrinho:
    def __init__(self):
        self.id_produto = []
        self.quantidade = []
        self.valor = 0
        pass

    def AdicionarCarrinho(self):
        """
        Docstring para AdicionarCarrinho
        
        Função para adicionar os produtos no carrinho
        """
        os.system('clear')

        BP.BuscarBanco("todos", 0)

        id = int(input("Digite o valor do id para adicionar no carrinho: "))
        quantidade = int(input("Quantos produtos deseja adicionar no carrinho: "))

        
        # proibindo a entrada de valores negativos ou zero, pois não faria sentido remover um produto com quantidade negativa ou zero
        if id <= 0 or quantidade <= 0:
            texto = Text.from_markup("ID e quantidade devem ser maiores que zero:sweat:", justify='center')
            panel = Panel(texto, title="Erro", style="red", width=34)
            print(panel)
            input("\nPressione Enter para continuar...")
            self.AdicionarCarrinho()
            return
        

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        achou_o_id_no_banco = False
        #precorendo todos os ids do meu banco
        for produto in dados['produtos']:
            if id == produto['id_produto']:
                achou_o_id_no_banco  = True

                #uma verificação pra saber se meu produto ja esta no carrinho
                achou_o_id_no_carrinho = False
                #uso essa estrutura de repetição pra conseguir saberem qual idice meu produto esta
                for indice, id_produto in enumerate(self.id_produto):
                    if id == id_produto:
                        indice_produto = indice
                        achou_o_id_no_carrinho = True

                #se a quantidade que eu quero do produto estiver em estoque
                if produto['estoque'] >= quantidade and produto['estoque'] > 0:
                    #eu verifico se tenho que adicionar essa quantidade a um novo produto
                    if not achou_o_id_no_carrinho:
                        self.quantidade.append(quantidade)
                        #ou apenas somar em um produt ja existente
                    else:
                        self.quantidade[indice_produto] += quantidade
                else:

                    #mensagem de erro caso o produto não estaja em estoque
                    texto = Text.from_markup("Produto fora de estoque:sweat:", justify='center')
                    panel = Panel(texto, title="Menssagem", style="red", width=34)
                    print(panel)

                    input("\nPressione Enter para continuar...")
                    return
                
                #aqui eu verifico se meu produto ja esta no carrinho, caso não esteja, eu adiciono
                if not achou_o_id_no_carrinho:
                    self.id_produto.append(id)
                self.valor += (produto['valor'] * quantidade)

        #mensagem de erro caso eu não ache o id no banco
        if not achou_o_id_no_banco:
            texto = Text.from_markup("ID inválido:sweat:", justify='center')
            panel = Panel(texto, title="Erro", style="red", width=34)
            print(panel)

            input("\nPressione Enter para continuar...")

            self.AdicionarCarrinho()
            return
        BP.BuscarBanco("todos", 0)
        pass

    def ExibirCarrinho(self):
        """
        Docstring para ExibirCarrinho
        
        função dedicada a exibir os produtos no meu carrinho
        """
        #eu vejo se tem algo no meu carrinho
        if len(self.id_produto) > 0:
            with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            
            #se tivbber eu vou comparando os ids que eu tenho com os do banco
            #se eu tiver um id do banco, eu exibo o produto
            for produto in dados['produtos']:
                for indice, id in enumerate(self.id_produto):
                    if id == produto['id_produto']:
                        print(f"id_produto: {produto["id_produto"]}, nome: {produto["nome"]}, valor: {produto["valor"]}, quantidade carrinho: {self.quantidade[indice]}")
        pass

    def RemoverCarrinho(self):
        """
        Docstring para RemoverCarrinho
        
        função criada com o intuito de acessar o carrinho e remover valores dele
        """
        os.system('clear')

        self.ExibirCarrinho()

        id = int(input("Digite o valor do id para remover do carrinho: "))
        quantidade = int(input("Quantos produtos deseja remover do carrinho: "))

        
        # proibindo a entrada de valores negativos ou zero, pois não faria sentido remover um produto com quantidade negativa ou zero
        if id <= 0 or quantidade <= 0:
            texto = Text.from_markup("ID e quantidade devem ser maiores que zero:sweat:", justify='center')
            panel = Panel(texto, title="Erro", style="red", width=34)
            print(panel)
            input("\nPressione Enter para continuar...")
            self.RemoverCarrinho()
            return
        

        #percorrendo o carrinho pra saber se o item que eu quero remover existe no carrinho 
        achou_o_id_no_carrinho = False
        for indice, id_produto in enumerate(self.id_produto):
            if id == id_produto:
                indice_produto = indice
                achou_o_id_no_carrinho = True

        #caso o item não exista, exibo uma menssagem de erro, e retomo a operação
        if not achou_o_id_no_carrinho:
            texto = Text.from_markup("Produto fora do carrinho:sweat:", justify='center')
            panel = Panel(texto, title="Erro", style="red", width=34)
            print(panel)

            input("\nPressione Enter para continuar...")

            self.RemoverCarrinho()
            return


        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        #percorrendo meu banco de produtos
        for produto in dados['produtos']:
            #procurando os item que estão no meu carrinho no banco
            if id == produto['id_produto']:

                #verifica se eu tenho essa quantidade que eu quero remover do carrinho
                if quantidade <= self.quantidade[indice_produto]:

                    #se tiver eu removo do carrinho e do valor
                    self.quantidade[indice_produto] -= quantidade
                    self.valor -= (produto['valor'] * quantidade)

                    #se não sobrar nenhum produto do tipo no meu carrinho, eu removo ele
                    if self.quantidade[indice_produto] == 0: 
                        self.id_produto.pop(indice_produto)
                        self.quantidade.pop(indice_produto)
                else:
                    texto = Text.from_markup("Quantidade inválida:sweat:", justify='center')
                    panel = Panel(texto, title="Erro", style="red", width=34)
                    print(panel)

                    input("\nPressione Enter para continuar...")

                    self.RemoverCarrinho()

        BP.BuscarBanco("todos", 0)
        pass

c = Carrinho()

while True:
    c.AdicionarCarrinho()

    c.RemoverCarrinho()
    print("\n")

    c.ExibirCarrinho()
    print(f"R${c.valor:,.2f}")

    input("\nPressione Enter para continuar...")
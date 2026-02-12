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
        self.valor = 0
        pass

    def AdicionarCarrinho(self):
        """
        Docstring para AdicionarCarrinho
        
        Função para adicionar os produtos no carrinho

        (ainda tem alguns problemas de logica com meu banco)
        """
        os.system('clear')

        BP.BuscarBanco("todos", 0)

        id = int(input("Digite o valor do id para adicionar no carrinho: "))

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        achou_o_id = False
        #precorendo todos os ids do meu banco
        for produto in dados['produtos']:
            if id == produto['id_produto']:
                achou_o_id = True

                #se eu achar o id e ele estiver em estoque no banco, eu removo e adiciono no carrinho
                #isso é um problema, pois se houver algum probelama antes de eu finalizar a compra
                #o produto vai sumir do meu banco, gerando prejuizos
                if produto['estoque'] > 0:
                    produto['estoque'] -= 1
                else:

                    #mensagem de erro caso o produto não estaja em estoque
                    texto = Text.from_markup("Produto fora de estoque:sweat:", justify='center')
                    panel = Panel(texto, title="Menssagem", style="red", width=34)
                    print(panel)

                    input("\nPressione Enter para continuar...")

                    return
                
                #adicionando os valores que eu preciso
                self.id_produto.append(id)
                self.valor += produto['valor']

        #mensagem de erro caso eu não ache o id no banco
        if not achou_o_id:
            texto = Text.from_markup("Produto fora de estoque:sweat:", justify='center')
            panel = Panel(texto, title="Menssagem", style="red", width=34)
            print(panel)

            input("\nPressione Enter para continuar...")

            self.AdicionarCarrinho()

        #caso tudo dê certo, eu atualizo o banco
        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

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
                for id in self.id_produto:
                    if id == produto['id_produto']:
                        print(produto)
        pass

    def RemoverCarrinho(self):
        os.system('clear')

        self.ExibirCarrinho()

        id = int(input("Digite o valor do id para remover do carrinho: "))

        achou_o_id = False
        for i in self.id_produto:
            if id == i:
                achou_o_id = True

        if not achou_o_id:
            texto = Text.from_markup("Produto fora de estoque:sweat:", justify='center')
            panel = Panel(texto, title="Menssagem", style="red", width=34)
            print(panel)

            input("\nPressione Enter para continuar...")

            self.RemoverCarrinho()


        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        for produto in dados['produtos']:
            if id == produto['id_produto']:
                produto['estoque'] += 1

                self.id_produto.remove(id)
                self.valor -= produto['valor']

        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        BP.BuscarBanco("todos", 0)
        pass

c = Carrinho()

c.AdicionarCarrinho()
#print(c.valor)

c.RemoverCarrinho()
#print(c.valor)
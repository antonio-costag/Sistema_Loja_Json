from produtos import Produto
from banco_produtos import BancoProdutos
from rich import print
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
        BP.BuscarBanco("todos", 0)

        id = int(input("Digite o valor do id: "))

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        for produto in dados['produtos']:
            if id == produto['id_produto']:
                self.id_produto.append(id)

                if produto['estoque'] > 0:
                    produto['estoque'] -= 1

                self.valor += produto['valor']

        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        BP.BuscarBanco("todos", 0)
        pass

    def ExibirCarrinho(self):
        if len(self.id_produto) > 0:
            with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            
            for produto in dados['produto']:
                if self.id_produto == produto['id_produto']:
                    print(produto)
        pass

    def RemoverCarrinho(self):
        pass

c = Carrinho()
c.AdicionarCarrinho()

for i in c.id_produto:
    print(i)

print(c.valor)
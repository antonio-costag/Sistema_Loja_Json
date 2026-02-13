from carrinho import Carrinho
import os
import json

caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'produtos.json')

class Vendas:
    def __init__(self):
        self.carrinho = Carrinho()
        self.id_venda = 0
        self.data = ""
        self.vendas = []
        pass
    
    def EfetuarVenda(self):
        self.data = input("Digite a data desta venda: ")

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        for produto in dados['produtos']:
            for index, id in enumerate(self.carrinho.id_produto):
                if id == produto['id_produto']:
                    nova_venda = {
                        'id_venda': self.id_venda,
                        'nome_produto': produto['nome'],
                        'valor_produto': produto['valor'],
                        'quantidade': self.carrinho.quantidade[index],
                        'data': self.data
                    }

                    self.vendas.append(nova_venda)
        pass
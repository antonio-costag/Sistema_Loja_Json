from carrinho import Carrinho
import os
import json

caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'produtos.json')

class Vendas:
    def __init__(self, id_venda, data, venda: list[int, str, str, int]):
        self.carrinho = Carrinho()
        self.id_venda = id_venda
        self.data = data
        self.venda = venda
        pass
    
    def EfetuarVenda(self):
        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        for produto in dados['produtos']:
            for index, id in enumerate(self.carrinho.id_produto):
                if id == produto['id_produto']:
                    nova_venda = {
                        'id_venda': self.id_venda,
                        'nome_produto': produto['nome'],
                        'data': self.data,
                        'venda':  (produto['valor'] * self.carrinho.quantidade[index])
                    }

                    self.venda.append(nova_venda)
        pass
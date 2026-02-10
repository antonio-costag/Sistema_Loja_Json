from produtos import Produto

class Carrinho:
    def __init__(self):
        self.produto = []
        pass

    def AdicionarCarrinho(self, produto: list[Produto]):
        self.produto.append[produto]
        pass

    def RemoverCarrinho(self, produto: list[Produto]):
        self.produto.remove[produto]
        pass
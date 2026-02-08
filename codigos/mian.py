from produtos import Produto
from gerente_banco import GerenteBanco

produto1 = Produto("coca cola", 10.50, "refrigerante")

gb = GerenteBanco()
gb.produto = produto1

gb.CadastrarProduto()

produto2 = Produto("puddim", 6.00, "bolo")
gb.produto = produto2

gb.CadastrarProduto()
from produtos import Produto
from gerente_banco import GerenteBanco
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import os

def TabelaBuscaProduto():
    #isso é só pra deixar mais bonito
    tabela_desig = Table(title="[yellow]Tabela de Busca[/]", style="yellow")

    tabela_desig.add_column("Opções", style="blue", width=30)

    tabela_desig.add_row("id_produto")
    tabela_desig.add_row("nome")
    tabela_desig.add_row("valor")
    tabela_desig.add_row("categoria")
    tabela_desig.add_row("estoque")
    tabela_desig.add_row("todos")

    print(tabela_desig)

    tabela = input("Escolha uma opção: ")

    list = ["id_produto", "nome", "valor", "categoria", "estoque", "todos"]

    #aqui que eu fiz esse ciclo de repetição pra ser mais rapido eu verificar se a opção existe
    achou_valor = False
    for i in list:
        if i == tabela:
            achou_valor = True
            break

    #se a opção não existe eu printo uma mensagem de erro e busco novamente 
    if not achou_valor:
        os.system('clear')

        texto = Text.from_markup("Opção invalida:sweat:", justify='center')
        panel = Panel(texto, title="Menssagem", style="red", width=34)
        print(panel)

        TabelaBuscaProduto()
    else:

        #caso que queira buscar todos os valores, o nome da busca se torna inutil
        nome_busca = 0
        if tabela != "todos":
            nome_busca = input(f"digite o(a) {tabela} do seu profuto: ")

        gb.BuscarProduto(tabela, nome_busca)

    pass

gb = GerenteBanco()

produto1 = Produto("bolo puddim", 6.00, "bolo", 8)
gb.produto = produto1
#gb.CadastrarProduto()

os.system('clear')
TabelaBuscaProduto()
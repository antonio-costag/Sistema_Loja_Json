from produtos import Produto
from banco_produtos import BancoProdutos
from banco_vendas import BancoVendas
from carrinho import Carrinho
from vendas import Vendas
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import os

gb = BancoProdutos()

def TelaInicial():
    os.system('clear')

    tabela_desig = Table(title="[yellow]Tabela de Inicial[/]", style="yellow")

    tabela_desig.add_column("[yellow]Opções[/]", style="blue", width=30)

    tabela_desig.add_row("cadastrar produto")
    tabela_desig.add_row("buscar produto")
    tabela_desig.add_row("Sair")

    print(tabela_desig)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "cadastrar produto":
            TabelaCadastroProduto()
        case "buscar produto":
            TelaBuscaProduto()
        case "sair":
            os.system('clear')

            texto = Text.from_markup("bya:sweat:", justify='center')
            panel = Panel(texto, title="Menssagem", style="blue", width=34)
            print(panel)

            return
        case _:
            texto = Text.from_markup("Opção invalida:sweat:", justify='center')
            panel = Panel(texto, title="Menssagem", style="red", width=34)
            print(panel)

            input("\nPressione Enter para continuar...")
            TelaInicial()
    pass

def TabelaCadastroProduto():
    os.system('clear')

    texto = Text.from_markup("Cadastro de Porduto:+1:", justify='center')
    panel = Panel(texto, title="Menssagem", style="yellow", width=34)
    print(panel)

    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    categoria = input("Digite a categoria do produto: ")
    estoque = int(input("Digite o estoque do produto: "))

    produto = Produto(nome, valor, categoria, estoque)
    gb.produto = produto
    gb.CadastrarProduto()

    input("\nPressione Enter para continuar...")
    TelaInicial()

    pass

def TelaBuscaProduto():
    os.system('clear')

    #isso é só pra deixar mais bonito
    tabela_desig = Table(title="[yellow]Tabela de Busca[/]", style="yellow")

    tabela_desig.add_column("[yellow]Opções[/]", style="blue", width=30)

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
        texto = Text.from_markup("Opção invalida:sweat:", justify='center')
        panel = Panel(texto, title="Menssagem", style="red", width=34)
        print(panel)

        input("\nPressione Enter para continuar...")

        TelaBuscaProduto()
    else:

        #caso que queira buscar todos os valores, o nome da busca se torna inutil
        nome_busca = 0
        if tabela != "todos":
            nome_busca = input(f"digite o(a) {tabela} do seu profuto: ")

        gb.BuscarBanco(tabela, nome_busca)

        input("\nPressione Enter para continuar...")
        TelaInicial()

    pass


#TelaInicial()

carrinho = Carrinho()

banco_vendas = BancoVendas()

carrinho.AdicionarCarrinho()
carrinho.AdicionarCarrinho()
carrinho.AdicionarCarrinho()

#venda.carrinho = carrinho
#venda.EfetuarVenda()

venda = Vendas()
banco_vendas.vendas = venda
banco_vendas.vendas.carrinho = carrinho
banco_vendas.vendas.EfetuarVenda()

banco_vendas.RegistrarVenda()

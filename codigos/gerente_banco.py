from rich import print
from rich.panel import Panel
from produtos import Produto
from rich.text import Text
import os
import json

#__file__ (Onde eu estou?): uma variável do Python. Ela contém o caminho completo do meu compras.py.

#os.path.dirname(__file__): (Qual é a minha pasta?) A função dirname pega o caminho completo do meu compras.py e retorna apenas a parte da pasta onde ele está localizado.
#os.path.dirname(os.path.dirname(__file__)) faz a mesma coisa, so que com a pasta que ta guardando o compras.py

#'compras.json': (Qual é o nome do arquivo?) É o nome do arquivo JSON onde eu quero armazenar os dados das compras.

caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'produtos.json')

class GerenteBanco:
    """
    Docstring para Compras

    Essa função vai ser responsavel por efetuar uma compra

    A unica função dessa classe que deve ser usado é "EfetuarCompra"
    A outras função são apenas para garantir que o "EfetuarCompra" ocorra sem problemas

    o usuario apenas declara ela declarando deus valores e depois chama "EfetuarCompra"
    """
    
    def __init__(self):
        self.produto = Produto("", 0, "", 0)

        pass

    def _VerificarExistenciaBanco(self, tabela):
        """
        Docstring para VerificarExistenciaBanco
        
        essa função vai criar um novo branco caso ele não exista
        """


        #aqui eu volto um nivel, sainda de "compras.json" e indo pra "banco de dados"
        pasta_banco = os.path.dirname(caminho_banco)

        #se ela não exister, eu crio uma nova
        os.makedirs(pasta_banco, exist_ok=True)

        #vericando se meu banco não existe
        if not os.path.exists(caminho_banco):

            #se ele não existir, eu crio uma estrutura vazia pra minha lista de compras
            compras = {
                tabela:[ 
                ]
            }

            #aqui eu crio um novo aquivo .json e escrevo minha estrutura
            with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
                json.dump(compras, arquivo, indent=4, ensure_ascii=False)

        pass

    def _AutoIncremetarID(self, tabela, id_tabela):
        """
        Docstring para AutoIncremetarID
        
        Essa função é fundamental para que meu banco não apresente graver problemas
        ela vai cuidar para criar os id's das minhas compras, assim evitando
        que aja repetição de id
        """

        #vou pegar e ler meu banco
        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        #se o que estiver escrito dentro dele for apenas []
        #significa que ele ta vazio
        if json.dumps(dados[tabela]) == "[]":
            if tabela == 'produtos':
                #assim então, esse é o primeiro item a entrar no banco
                self.produto.id_produto = 1

        else:
            # se não for o primeiro
            novo_id = 0

            #eu percorro todos os id's so meu banco
            for id in dados[tabela]:
                novo_id = id[id_tabela]

            if tabela == 'produtos':
                #pego o ultimo e incremento +1, assim progredindo a ordem
                self.produto.id_produto = novo_id + 1
        
        pass

    def AtualizarEstoqueProduto(self):
        """
        Docstring para AtualizarEstoqueProduto

        função que previni o cadastro de um produto que ja existe no banco
        previnindo a duplicidade de informação

        ela so atualiza o estoque se o produto ja existe, (provavelmente vai passar por alterações)
        """
        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        #percorrendo todos os valores da minha lista
        for produto in dados['produtos']:

            #seu eu ja achar o produto que eu quero cadastrar
            if self.produto.nome == produto['nome']:

                #então eu so atualizo meu estoque
                produto['estoque'] += self.produto.estoque

                # e reescrevo o banco novamente
                with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

                os.system('clear')
                
                texto = Text.from_markup("Produto ja está de estoque, estoque atualizado:flushed:", justify='center')
                panel = Panel(texto, title="Menssagem", style="yellow", width=34)
                print(panel)

                #se retornar true, ele incerra a operação de cadastro, pq não vai ser necessario
                return True

    def CadastrarProduto(self):
        """
        Docstring para EfetuarCompra
        
        Essa é a função que vai efetuar a compra e guardar ela no banco
        """
        self._VerificarExistenciaBanco('produtos')
        self._AutoIncremetarID('produtos', 'id_produto')

        if self.AtualizarEstoqueProduto():
            return

        #criando uma nova lista
        novo_produto = {
            'id_produto': self.produto.id_produto,
            'nome': self.produto.nome,
            'valor': self.produto.valor,
            'categoria': self.produto.categoria,
            'estoque': self.produto.estoque
        }

        #aqui eu vou pegar o meu banco (que é uma lista de lista)
        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        #e colocar um novo valor dentro dele (que é uma lista)
        dados['produtos'].append(novo_produto)

        #depois eu reescrevo meu novo branco, com as atualizações feitas
        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        os.system('clear')
        #assim é printado um painel confirmando que a ação foi bem sucedida
        texto = Text.from_markup("Cadastro efetudo com sucesso:grin:", justify='center')
        panel = Panel(texto, title="Menssagem", style="green", width=34)
        print(panel)
        pass

    def BuscarProduto(self, tabela, nome_busca):
        """
        Docstring para BuscarProduto

        Função destinada a encontrar os produtos no banco de dados
        
        :param tabela: a tipo de informação que o usuario deseja usar pra realizar uma busca
        :param produto_busca: O nome da informaçõa que o usuario deseja usar para achar o item 
        """
        achou_produto = False

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        for produto in dados['produtos']:

            #caso eu queira buscar todas as tabelas do meu banco
            if tabela == "todos":
                print(produto)
                achou_produto = True
            else:
                #aqui eu faço uma verificação pra saber se o item da minha tabela é um numero
                if isinstance(produto[tabela], (int, float)):
                    #se for qualquer tipo de numero eu converto pra float mesmo, pq linguagem faz conversão implicita e não atrapla na comparação com inteiro
                    nome_busca = float(nome_busca)

                    #aqui eu vou exibir apenas as informações que contem o que eu busco
                if  nome_busca == produto[tabela]:
                    print(produto)
                    achou_produto = True

        #mensagem de erro caso o produto que eu queira achar não estiver disponivel no meu banco
        if not achou_produto:
            os.system('clear')
        
            texto = Text.from_markup("Produto fora de estoque:sweat:", justify='center')
            panel = Panel(texto, title="Menssagem", style="red", width=34)
            print(panel)
        pass

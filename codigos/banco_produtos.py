from banco_basico import BancoBasico
from rich import print
from rich.text import Text
from rich.panel import Panel
import os
import json

caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'produtos.json')

class BancoProdutos(BancoBasico):
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
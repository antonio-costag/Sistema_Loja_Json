from produtos import Produto
import os
import json

class BancoBasico:
    """
    Docstring para Compras

    Essa função vai ser responsavel por efetuar uma compra

    A unica função dessa classe que deve ser usado é "EfetuarCompra"
    A outras função são apenas para garantir que o "EfetuarCompra" ocorra sem problemas

    o usuario apenas declara ela declarando deus valores e depois chama "EfetuarCompra"
    """
    
    def __init__(self):
        from vendas import Vendas
        self.produto = Produto("", 0, "", 0)
        self.vendas = Vendas()

        pass

    def _VerificarExistenciaBanco(self, tabela, caminho_banco):
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

    def _AutoIncremetarID(self, tabela, id_tabela, caminho_banco):
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
                self.vendas.id_venda = 1

        else:
            # se não for o primeiro
            novo_id = 0

            #eu percorro todos os id's so meu banco
            for id in dados[tabela]:
                novo_id = id[id_tabela]

            if tabela == 'produtos':
                #pego o ultimo e incremento +1, assim progredindo a ordem
                self.produto.id_produto = novo_id + 1
            else:
                self.vendas.id_venda = novo_id + 1
        
        pass

from rich import print
from rich.panel import Panel
import os
import json

#__file__ (Onde eu estou?): uma variável do Python. Ela contém o caminho completo do meu compras.py.

#os.path.dirname(__file__): (Qual é a minha pasta?) A função dirname pega o caminho completo do meu compras.py e retorna apenas a parte da pasta onde ele está localizado.
#os.path.dirname(os.path.dirname(__file__)) faz a mesma coisa, so que com a pasta que ta guardando o compras.py

#'compras.json': (Qual é o nome do arquivo?) É o nome do arquivo JSON onde eu quero armazenar os dados das compras.


caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'compras.json')

class Compras:
    """
    Docstring para Compras

    Essa função vai ser responsavel por efetuar uma compra

    A unica função dessa classe que deve ser usado é "EfetuarCompra"
    A outras função são apenas para garantir que o "EfetuarCompra" ocorra sem problemas

    o usuario apenas declara ela declarando deus valores e depois chama "EfetuarCompra"
    """
    def __init__(self, produto, valor, data):
        self._id = 0
        self._produto = produto
        self._valor = valor
        self._data = data
        pass

    def _VerificarExistenciaBanco(self):
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
                'compras':[ 
                ]
            }

            #aqui eu crio um novo aquivo .json e escrevo minha estrutura
            with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
                json.dump(compras, arquivo, indent=4, ensure_ascii=False)

        pass

    def _AutoIncremetarID(self):
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
        if json.dumps(dados['compras']) == "[]":
            #assim então, esse é o primeiro item a entrar no banco
            self._id = 1
        else:
            # se não for o primeiro
            novo_id = 0

            #eu percorro todos os id's so meu banco
            for id in dados['compras']:
                novo_id = id['id']

            #pego o ultimo e incremento +1, assim progredindo a ordem
            self._id = novo_id + 1
        
        pass

    def EfetuarCompra(self):
        """
        Docstring para EfetuarCompra
        
        Essa é a função que vai efetuar a compra e guardar ela no banco
        """
        self._VerificarExistenciaBanco()
        self._AutoIncremetarID()

        #criando uma nova lista
        nova_compra = {
            'id': self._id,
            'produto': self._produto,
            'valor': self._valor,
            'data': self._data
        }

        #aqui eu vou pegar o meu banco (que é uma lista de lista)
        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        #e colocar um novo valor dentro dele (que é uma lista)
        dados['compras'].append(nova_compra)

        #depois eu reescrevo meu novo branco, com as atualizações feitas
        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        #assim é printado um painel confirmando que a ação foi bem sucedida
        caixa = Panel("Compra efetuada com sucesso:+1:", title="Menssagem", style="red", width=33)
        print(caixa)
        pass

compra1 = Compras("Biscoito", 10.00, "7/2/2026")
compra1.EfetuarCompra()

compra2 = Compras("Coco", 7.80, "8/2/2026")
compra2.EfetuarCompra()

from banco_basico import BancoBasico
import os
import json

caminho_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'banco de dados', 'vendas.json')

class BancoVendas(BancoBasico):
    def RegistrarVenda(self):
        self._VerificarExistenciaBanco('vendas', caminho_banco)

        with open(caminho_banco, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        id_correcao_pro_vetor = 0

        for indice, nova_venda in enumerate(self.vendas.vendas):

            if indice == 0:
                self._AutoIncremetarID('vendas', 'id_venda', caminho_banco)
                id_correcao_pro_vetor = self.vendas.id_venda
            else:
                id_correcao_pro_vetor += 1
            
            nova_venda['id_venda'] = id_correcao_pro_vetor

            dados['vendas'].append(nova_venda)

        with open(caminho_banco, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        pass
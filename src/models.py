from abc import ABC

from repository import Registro_dados


class Produto:
    def __init__(self, nome, data, tipo_prod, quant):
        self._nome = nome
        self._data = data
        self._tipo_prod = tipo_prod
        self._quant = quant

    def estrutura(self, nome, data, tipo_prod, quant):
        estr_lista = {
            "tipo_produto": tipo_prod,
            "nome": nome,
            "quantidade": quant,
            "data": data,
        }
        return estr_lista


# OBSERVAÇAO EU PODERIA SIMPLESMENTE TER FEITO ESSA LISTA DE INFORMAÇÕES NO EXCEL E CONVERTIDO EM EM UM DATAFRAME
# OU DIRETAMENTE EM UM OUTRO FORMATO .CSV OU .JSON
# nesse caso leve em consideração que é como se o sistema tivesse dados padrões contidos nele , se tivesse em um outro arquivo por exemplo, é como se dados
# da qual o sistema usa pra funcionar tivesse em outro arquivo

from abc import ABC


class Produto(ABC):
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

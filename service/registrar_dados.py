from ast import Raise
from multiprocessing import Value
from re import error

import pandas as pd
from models.type import Produto
from datetime import datetime, date, timedelta


class Validar_Dados_registro(Produto):
    def __init__(self, tipo_prod, nome, quantidade, data) -> None:
        super().__init__(tipo_prod, nome, quantidade, data)  # paramos aqui!!!

    def validar(self, tipo_prod, nome, quantidade, data):
        try:
            data_atual = [datetime.now().year, datetime.now().month, datetime.now().day]
            data_convert = datetime.fromisoformat(data)
            data_prod = [
                data_convert.year,
                data_convert.month,
                data_convert.day,
            ]  # corrir aqui!!! mgoogle
            if len(nome) > 40:
                raise TypeError

            elif data_prod[0] >= data_atual[0]:
                if data_prod[1] > data_atual[1]:
                    raise ValueError
                elif data_prod[2] > data_atual[2]:
                    raise ValueError
                else:
                    return True

        except (TypeError, ValueError) as erro:
            if erro == TypeError:
                return "Erro: Nome muito grande"
            else:
                return "Erro: Data inccorreta"

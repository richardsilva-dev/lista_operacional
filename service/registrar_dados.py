from ast import Raise
from multiprocessing import Value
from re import error

import pandas as pd
from models.type import Produto
from datetime import datetime, date, timedelta
import service.erro_tratamento


class Validar_Dados_registro(Produto):
    def __init__(self, tipo_prod, nome, quantidade, data) -> None:
        super().__init__(tipo_prod, nome, quantidade, data)

    def validar(self, tipo_prod, nome, quantidade, data):
        try:
            if not all([tipo_prod, nome, quantidade, data]):
                raise service.erro_tratamento.Str_Vazia

            data_atual = date.today()
            data_convert = datetime.fromisoformat(data).date()
            if data_convert > data_atual:
                raise ValueError
            if len(nome) > 40 or len(tipo_prod) > 40:
                raise service.erro_tratamento.Str_Longa

        except (TypeError, ValueError) as erro:
            if erro == service.erro_tratamento.Str_Longa:
                return "Erro: Nome muito grande"
            elif erro == service.erro_tratamento.Str_Vazia:
                return "Erro: Existe um dado vazio"
            else:
                return "Erro: Data inválida"

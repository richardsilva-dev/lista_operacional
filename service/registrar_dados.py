from ast import Raise
from multiprocessing import Value
from re import error

import pandas as pd
from datetime import datetime, date
from models.type import List_Dictionary


class Validar_Dados_registro:
    def validar(self, list_dict):
        df = pd.DataFrame(list_dict)
        caracteres = df.iloc[:, 0].str.len() < 50
        caracteres2 = df.iloc[:, 2].str.len() < 50
        valid_colunas = caracteres & caracteres2
        validando_caract = (~valid_colunas).any()
        assert not validando_caract, "ERRO: string muito grande!"

        data_convert = pd.to_datetime(df.iloc[:, 1])
        data_atual = date.today()
        limite = pd.to_datetime(data_atual)
        validando_data = data_convert < limite
        # ex: [True, False, True ...] se a data for menor que a atual e não ultrapassada

        verificar_data = (~validando_data).any()
        # qualquer False será True com a converção (~) e vice-versa
        # any() identifica algum True convertido
        assert not verificar_data, "ERRO: Data inválida!"

        valor_vazio = df.isna().any().any()
        assert not valor_vazio, "ERRO: Existem valore(s) vázio(s)"

        valores_num_convert = pd.to_numeric(df.iloc[:, 3], errors="coerce")
        validando_inteiro = valores_num_convert.isna().any()
        assert (
            not validando_inteiro
        ), 'ERRO: existe um valor não númerico ou não inteiro na coluna "Quantidade"'

        return list_dict

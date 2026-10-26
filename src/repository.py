from zipfile import BadZipFile

from iniconfig import ParseError

import pandas as pd

from pandas.testing import assert_frame_equal

import os

import tests.test_data_register_all


class Registro_Dados:
    def __init__(self, list_dict=[{}]):
        self.list_dict = list_dict

    def adicionando_csv(self, list_dict):
        dir_atual = os.getcwd()
        if not os.access(dir_atual, os.W_OK):
            raise PermissionError("Não tem permissão para escrita no diretorio atual")

        try:
            dados = pd.DataFrame(list_dict)
            dados.to_csv("dados_registros.csv", index=False)
        except ParseError as e:
            return "Dados mal formatados"
        else:
            return "Dados salvos!"


class Buscar_Dados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def buscando_dados_base(self):

        if not os.path.exists(self.arquivo):
            raise FileNotFoundError(f"arquivo: {self.arquivo} não encontrado")
        # verficação de antemão se o arquivo existe

        if not os.access(self.arquivo, os.R_OK):
            raise PermissionError(
                f"não á permissão para acessar o arquivo: {self.arquivo}"
            )
        # verificar se tem permissão para leitura, evitando o Permission erro futuramente

        if tests.test_data_register_all.test_verificar_xlsx_valido is True:
            raise BadZipFile("Falha no processamento do arquivo")

        try:
            df = pd.read_excel(self.arquivo)
            return df
        except PermissionError:
            print(" O arquivo está aberto ou protegido. Feche-o e tente novamente.")
        except BadZipFile:
            print("Erro : arquivo corrompido")
        except ImportError:
            print("instale dependencias : openpyxl")

from gzip import BadGzipFile
from zipfile import BadZipFile

from iniconfig import ParseError
import pandas as pd
from pandas.testing import assert_frame_equal
import os

from param import DataFrame
from ..test import test_data_register_All


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
    @staticmethod
    def buscando_dados_base():
        arquivo = "dados_base_estoque.xlsx"

        if not os.path.exists(arquivo):
            raise FileNotFoundError(f"arquivo: {arquivo} não encontrado")
        # verficação de antemão se o arquivo existe

        if not os.access(arquivo, os.R_OK):
            raise PermissionError(f"não á permissão para acessar o arquivo: {arquivo}")
        # verificar se tem permissão para leitura, evitando o Permission erro futuramente

        if test_data_register_All.test_verificar_xlsx_valido is not True:
            raise BadZipFile("Falha no processamento do arquivo")

        try:
            df = pd.read_excel("dados_base_estoque.xlsx", engine="openpyxl")
            return df
        except PermissionError:
            print(
                " O arquivo está aberto no Excel ou protegido. Feche-o e tente novamente."
            )
        except BadZipFile:
            df = pd.read_csv("dados_base_estoque.csv")
            return df
        except ImportError:
            print("instale dependencias : openpyxl")

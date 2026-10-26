import pandas as pd
from pandas.testing import assert_frame_equal
import zipfile
import os
from openpyxl import load_workbook


def test_comparando():
    test_list = [
        {"1": "test1", "2": "test2", "3": 32, "4": "2026-10-11"},
        {"1": "test3", "2": "test4", "3": 33, "4": "2026-09-11"},
        {"1": "test5", "2": "test6", "3": 34, "4": "2026-08-11"},
        {"1": "test7", "2": "test8", "3": 35, "4": "2026-07-11"},
    ]
    dados = pd.DataFrame(test_list)
    dados.to_csv("test_dados.csv", index=False)
    dados_recuperacao = pd.read_csv(
        "test_dados.csv",
        dtype={"Quantidade": int, "Data": str, "tipo_prod": str, "nome": str},
    )

    assert_frame_equal(dados, dados_recuperacao)


def test_verificar_xlsx_valido():
    """
    Verifica se um arquivo XLSX é um ZIP válido e pode ser aberto pelo openpyxl.
    Retorna True se válido, False caso contrário.
    """
    caminho_arquivo = "src/dados_base_estoque.xlsx"
    # Testa se é um ZIP válido
    try:
        with zipfile.ZipFile(caminho_arquivo, "r") as zip_ref:
            teste = zip_ref.testzip()  # Retorna None se não houver erro
            if teste is not None:
                print(f"Arquivo corrompido: problema no arquivo interno {teste}")
                return False
    except zipfile.BadZipFile:
        print("Erro: O arquivo XLSX não é um ZIP válido.")
        return False

    # Testa se openpyxl consegue abrir
    try:
        wb = load_workbook(caminho_arquivo)
        return False
    except Exception as e:
        return True

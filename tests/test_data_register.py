import pandas as pd
from pandas.testing import assert_frame_equal


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

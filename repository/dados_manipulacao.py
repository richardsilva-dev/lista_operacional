import pandas as pd
from pandas.testing import assert_frame_equal


class Registro_dados:
    def __init__(self, list_dict):
        self.list_dict = list_dict

    def adicionando_csv(self, list_dict):
        dados = pd.DataFrame(list_dict)
        dados.to_csv("dados_registros.csv", index=False)
        dados_recuperacao = pd.read_csv(
            "dados_registros.csv",
            dtype={"Quantidade": int, "Data": str, "tipo_prod": str, "nome": str},
        )

        try:
            assert_frame_equal(dados, dados_recuperacao)
            return "Dados salvos com sucesso!"

        except AssertionError as erro:
            print(f"Os dados persisitidos são diferentes!")
            print(erro)

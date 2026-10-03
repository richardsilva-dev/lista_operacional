import pandas as pd
from pandas.testing import assert_frame_equal


class Registro_dados:
    def __init__(self, estrutura):
        self.estrutura = estrutura

    def adcionando_csv(self, estrutura):

        dados = pd.DataFrame(estrutura)
        dados.to_csv("dados_registros.csv", index=False)
        dados_recuperacao = pd.read_csv(
            "dados_registros.csv", dtype={"Quantidade": "int64", "Data": "String"}
        )

        try:
            assert_frame_equal(dados, dados_recuperacao)
            return "Dados salvos com sucesso!"

        except AssertionError as erro:
            print(f"Os dados persisitidos são diferentes!")
            print(erro)

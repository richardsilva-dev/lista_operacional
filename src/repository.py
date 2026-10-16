import pandas as pd
from pandas.testing import assert_frame_equal


class Registro_dados:
    def __init__(self, list_dict):
        self.list_dict = list_dict

    def adicionando_csv(self, list_dict):
        dados = pd.DataFrame(list_dict)
        dados.to_csv("dados_registros.csv", index=False)
        return "Dados salvos!"
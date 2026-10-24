from models import Produto
import datetime
from repository import Registro_Dados
from service import Validar_Dados_registro
import pandas as pd


def main():
    print("""<><><> PROJETO CRUD <><><> \n\n[]Levantamento de bebidas-Pizzaria""")
    print(
        """ -Menu\n[1]-Registrar dados\n[2]-Consultar dados\n[3]-Atualizar\n[4]-Excluir"""
    )

    df_estoque = Registro_Dados().buscando_dados_base()
    data_atual = datetime.date.today()
    data_formatada = data_atual.isoformat()
    meus_produtos = []
    enter_salv = 0

    while enter_salv != 2:
        items_por_coluna = df_estoque.iloc[:, 0]
        for i in 
        df_estoque

        print(
            "\n---------------\n|1.Salvar Dados |\n---------------\n---------------\n|2.Cancelar   |\n---------------\n"
        )

        enter_salv = int(input("> "))
        while enter_salv > 2 or enter_salv == 0:
            print("Entrada invàlida tente novamente!")
            enter_novamente = int(input("> "))
            enter_salv = enter_novamente

        if enter_salv == 1:
            valid_dados = Validar_Dados_registro().validar(meus_produtos)
            if valid_dados:
                persis_dados = Registro_dados(meus_produtos).adicionando_csv(
                    meus_produtos
                )
                print(persis_dados)


(main())

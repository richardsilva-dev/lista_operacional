from models import Produto
import datetime
import repository
from validation_data.service import Validar_Dados_registro
import pandas as pd


def main():
    print("""<><><> PROJETO CRUD <><><> \n\n[]Levantamento de bebidas-Pizzaria\n""")

    df_estoque = repository.Buscar_Dados(
        "dados_base_estoque.xlsx"
    ).buscando_dados_base()
    data_atual = datetime.date.today()
    data_formatada = data_atual.isoformat()
    list_obj = []
    enter_salv = 0

    print("\n\n--ADICIONE A QUANTIDADE DE CADA ITÉM--\n\n")

    while enter_salv != 2:
        for celula in df_estoque.itertuples():
            enter_quant = int(input(f"[]{celula.Produto}: "))
            criando_obj = Produto(
                celula.Produto, data_formatada, celula.Categoria, enter_quant
            ).estrutura(celula.Produto, data_formatada, celula.Categoria, enter_quant)
            list_obj.append(criando_obj)
        print(
            "\n---------------\n|1.Salvar Dados |\n---------------\n---------------\n|2.Cancelar   |\n---------------\n"
        )

        enter_salv = int(input("> "))
        while enter_salv > 2 or enter_salv == 0:
            print("Entrada invàlida tente novamente!")
            enter_novamente = int(input("> "))
            enter_salv = enter_novamente

        if enter_salv == 1:
            valid_dados = Validar_Dados_registro().validar(list_obj)
            if valid_dados:
                persis_dados = repository.Registro_Dados(list_obj).adicionando_csv(
                    list_obj
                )
                print(persis_dados)
                print(pd.DataFrame(list_obj))
                enter_salv = 2
        else:
            enter_saida = 0
            while enter_saida > 2 or enter_saida == 0:
                print("\n\n[1]-retornar o processo\n[2]sair\n\n")
                enter_saida = int(input("> "))
                if enter_saida > 2 or enter_saida == 0:
                    print("\nEntrada inválida! Tente novamente")

            if enter_saida == 2:
                enter_salv = 2
                break
            else:
                enter_salv = 1


main()

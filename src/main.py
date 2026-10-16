from models import Produto, Estoque
import datetime
from repository import Registro_dados


def main():
    print("""<><><> PROJETO CRUD <><><> \n\n[]Levantamento de bebidas-Pizzaria""")
    print(
        """ -Menu\n[1]-Registrar dados\n[2]-Consultar dados\n[3]-Atualizar\n[4]-Excluir"""
    )

    meu_estoque = Estoque().dados_base()
    data_atual = datetime.date.today()
    data_formatada = data_atual.isoformat()
    meus_produtos = []
    enter_salv = 0

    while enter_salv != 2:
        for i, j in meu_estoque[0].items():
            print(f"__{i}__\n")
            for y in j:
                entrada_quant = int(input(f"[o]{y}: "))
                minha_lista = Produto(y, data_formatada, i, entrada_quant).estrutura(
                    y, data_atual, i, entrada_quant
                )
                meus_produtos += minha_lista

        print(
            "\n---------------\n|1.Salvar Dados |\n---------------\n---------------\n|2.Cancelar   |\n---------------\n"
        )

        enter_salv = int(input(" > "))
        while enter_salv != 1 or 2:
            print("Entrada invàlida tente novamente!")
            enter_novamente = enter_salv
            enter_salv = enter_novamente

        if enter_salv == 1:
            valid_dados = Validar_Dados_registro().validar(meus_produtos)
            if valid_dados == meus_produtos:
                persis_dados = Registro_dados(meus_produtos).adicionando_csv(
                    meus_produtos
                )
                print(persis_dados)

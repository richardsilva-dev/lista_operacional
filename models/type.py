class Produto:
    def __init___(self, tipo_prod, nome, quantidade, data):
        self.tipo_prod = tipo_prod
        self.nome = nome
        self.quantidade = quantidade
        self.data = data

    def estrutura(self, tipo_bebida, nome, quantidade, data):
        tabela_prods = [
            {
                "Tipo_produto": {
                    tipo_bebida: {
                        "Nome": [nome],
                        "Quantidade": [quantidade],
                        "Data": [data],
                    }
                }
            }
        ]
        return tabela_prods

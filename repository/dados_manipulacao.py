


class Registro_dados:
   def __init__(self, estrutura):
       self.estrutura = estrutura

    def adcionando_csv(self, estrutura):
          assert estrutura == [], "Erro! estrutura vazia"
          for i in estrutura[0].value():
            for e in i.value():
                if not e:
                    raise TypeError

          dados = pd.DataFrame(estrutura[0])
          dados.to_csv("dados_registros.cvs", index= False)
          dados_recuperacao = pd.read_csv("dados_registros.csv", dtype = {"Quantidade": "int64",
                                                                          "Data": "String"}) 

          try:
             assert_frame_equal(dados, dados_recuperacao)    
             return "Dados salvos com sucesso!"
    
          except AssertionError as erro:
              print(f"Os dados persisitidos são diferentes!")
              print(erro)

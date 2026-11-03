# Lista Operacional

Sistema desenvolvido em Python para registrar e organizar quantidades de produtos, permitindo transformar os dados inseridos em uma tabela e armazená-los em um arquivo CSV.

## 📌 Sobre o projeto

O **Lista Operacional** é uma aplicação voltada ao registro e à organização de informações operacionais de produtos.

O sistema permite inserir produtos e suas respectivas quantidades. Após a entrada dos dados, as informações são organizadas utilizando a biblioteca Pandas e exportadas para um arquivo CSV.

O projeto tem como objetivo facilitar o registro de quantidades, manter os dados organizados e permitir seu armazenamento em um formato que pode ser aberto em ferramentas como Microsoft Excel e Google Sheets.

## ⚙️ Funcionalidades

- Registro de produtos e suas respectivas quantidades.
- Organização dos dados em uma estrutura tabular.
- Conversão dos dados para um DataFrame utilizando Pandas.
- Exportação das informações para arquivos CSV.
- Armazenamento dos dados para consulta posterior.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade                                |
| ---------- | ----------------------------------------- |
| Python     | Desenvolvimento da aplicação.             |
| Pandas     | Organização e manipulação dos dados.      |
| CSV        | Armazenamento das informações em arquivo. |

## 🔄 Funcionamento

O funcionamento da aplicação segue este fluxo:

1. O usuário informa os produtos e suas respectivas quantidades.
2. Os dados inseridos são organizados em uma estrutura de dados.
3. As informações são convertidas para um DataFrame utilizando Pandas.
4. O DataFrame é exportado para um arquivo CSV.
5. O arquivo CSV armazena as informações registradas.

## 📊 Exemplo dos dados

Os dados armazenados seguem uma estrutura semelhante a esta:

| produto   | quantidade |
| --------- | ---------: |
| Coca-Cola |         15 |
| Sprite    |         10 |
| Guaraná   |          8 |

Exemplo de representação em CSV:

```csv
produto,quantidade
Coca-Cola,15
Sprite,10
Guaraná,8
```

## 💾 Armazenamento dos dados

As informações são armazenadas em um arquivo CSV.

**Comportamento atual:** quando o arquivo de armazenamento já existe, os novos dados inseridos substituem o conteúdo anterior.

Portanto, o sistema não mantém automaticamente um histórico das operações anteriores.

## 🚀 Como executar

### 1. Pré-requisitos

- Python instalado.
- Biblioteca Pandas.

### 2. Instalar a dependência

```bash
pip install pandas
```

### 3. Executar a aplicação

No terminal, acesse a pasta do projeto e execute o arquivo principal:

```bash
python nome_do_arquivo_principal.py
```

Substitua `nome_do_arquivo_principal.py` pelo nome real do arquivo de entrada da aplicação.

## 📈 Melhorias futuras

Possíveis melhorias para versões futuras:

- Evitar a substituição acidental de informações anteriores.
- Permitir adicionar novos registros sem apagar os existentes.
- Implementar um histórico de registros.
- Melhorar o tratamento de exceções.
- Implementar testes automatizados.
- adicionar novos recursos que permitem uma análise de dados aprofundada, e a exibição de informações relevantes sobre.

## 📂 Status do projeto

Projeto em desenvolvimento.

---

**Lista Operacional** — Aplicação desenvolvida para praticar Python, manipulação de dados e armazenamento de informações utilizando CSV e Pandas.

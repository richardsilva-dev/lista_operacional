# Lista Operacional

## 1. Visão geral

O **Lista Operacional** é um software de automação desenvolvido para facilitar o levantamento de quantidades de produtos de uma pizzaria, especialmente bebidas e outros itens organizados por categorias.

O projeto surgiu de uma necessidade observada no ambiente de trabalho: o levantamento de estoque era realizado manualmente, utilizando folhas de papel impressas com os nomes dos produtos e espaços para registrar suas respectivas quantidades.

Com o software, o funcionário pode realizar esse mesmo procedimento digitalmente, selecionando ou preenchendo as quantidades dos produtos apresentados pelo sistema. Os dados são processados e registrados em um arquivo CSV, reduzindo a necessidade de escrever as informações manualmente e facilitando a organização dos registros.

A versão atual foi desenvolvida especificamente para uma empresa, utilizando sua lista de produtos como base.

## 2. Problema que o software busca resolver

O processo manual de levantamento de estoque exige que o funcionário:

1. Consulte a lista impressa de produtos.
2. Conte as unidades de cada produto disponível.
3. Escreva a quantidade correspondente na folha.
4. Entregue o levantamento ao responsável pela empresa.
5. Permita que o gerente ou proprietário consulte as quantidades para planejar as compras.

Esse procedimento depende de papel e impressão, além de exigir o preenchimento manual de cada registro.

O Lista Operacional busca simplificar esse processo, permitindo que as quantidades sejam digitadas diretamente no software. A aplicação pode ser adaptada para uso em dispositivos móveis, desde que sua interface e implementação ofereçam suporte a esses dispositivos.

## 3. Objetivo principal

Digitalizar e simplificar o levantamento periódico de produtos da empresa, utilizando dados previamente cadastrados para apresentar uma lista estruturada de itens e permitir o registro de suas quantidades.

## 4. Escopo da versão atual

A primeira versão possui um escopo deliberadamente limitado.

### Funcionalidades implementadas

- Leitura dos dados-base dos produtos a partir de um arquivo Excel (`.xlsx`).
- Utilização dos nomes e das categorias dos produtos previamente cadastrados.
- Apresentação dos produtos para preenchimento das quantidades.
- Registro das quantidades informadas pelo usuário.
- Associação de cada registro à data correspondente.
- Organização dos dados em uma estrutura de objetos.
- Validação dos registros antes da persistência.
- Transformação dos registros em um DataFrame utilizando Pandas.
- Exportação dos dados processados para um arquivo CSV.
- Separação das responsabilidades entre os módulos do projeto.
- Testes automatizados com Pytest para verificar o comportamento e a validade dos dados.

### Limitações conhecidas

A versão atual não oferece:

- Cadastro de novos produtos pela interface.
- Cadastro de novas categorias de produtos.
- Histórico de levantamentos anteriores.
- Comparação entre levantamentos de datas diferentes.
- Relatórios estatísticos sobre as quantidades registradas.
- Identificação automática do produto com maior ou menor quantidade.
- Cálculo de médias ou outros indicadores de estoque.
- Garantia de preservação dos levantamentos anteriores quando o arquivo de saída é sobrescrito.

O sistema utiliza uma base de produtos específica da empresa. Portanto, sua configuração atual não foi projetada para atender diretamente a qualquer empresa sem adaptações.

## 5. Origem e organização dos dados

O software trabalha com duas categorias de dados.

### 5.1. Dados-base

Os dados-base contêm as informações que identificam os produtos disponíveis para levantamento.

Esses dados são obtidos de um arquivo Excel (`.xlsx`) e incluem, entre outros campos:

- Nome do produto.
- Categoria ou tipo do produto, como refrigerantes, vinhos, bebidas e polpas.

Essa base funciona como um catálogo de referência. Na versão atual, o usuário não precisa cadastrar esses produtos a cada utilização.

### 5.2. Dados do levantamento

Durante o levantamento, o usuário informa a quantidade correspondente a cada produto.

Essas informações são organizadas internamente em registros que contêm:

- Nome do produto.
- Tipo ou categoria do produto.
- Quantidad
e informada.
- Data do registro.

Cada registro representa um produto contabilizado no levantamento.

## 6. Fluxo de processamento dos dados

O fluxo principal da aplicação pode ser descrito da seguinte forma:

1. **Leitura da base:** o sistema obtém os produtos e suas categorias a partir do arquivo Excel.
2. **Entrada de dados:** o usuário informa as quantidades dos produtos apresentados.
3. **Modelagem:** os dados são organizados em objetos com atributos definidos.
4. **Validação:** o módulo de serviço verifica os registros antes de permitir sua persistência.
5. **Persistência:** o repositório recebe os registros validados, organiza os dados em um DataFrame e exporta o resultado para CSV.
6. **Finalização:** o processo termina após o registro dos dados, sem gerar relatórios analíticos na versão atual.

## 7. Arquitetura do projeto

O projeto está dividido em módulos com responsabilidades distintas.

### `main.py` — Orquestração da aplicação

É o ponto de entrada do software e coordena o fluxo principal: leitura ou obtenção dos dados necessários, interação com o usuário e encaminhamento dos registros para processamento.

### `model.py` — Modelagem dos registros

Define a estrutura dos objetos utilizados para representar os produtos contabilizados, incluindo nome, categoria, quantidade e data.

Essa separação permite representar os dados de forma consistente antes de sua validação e persistência.

### `service.py` — Regras e validação

Responsável pelas regras de processamento e validação dos registros.

Essa camada permite verificar se os dados atendem aos critérios definidos pela aplicação antes que sejam encaminhados ao repositório.

### `repository.py` — Acesso e persistência dos dados

Responsável pelas operações relacionadas aos arquivos de dados, conforme a implementação atual, incluindo a leitura da base de produtos e a gravação dos registros do levantamento.

O módulo utiliza Pandas para transformar os registros em um DataFrame e exportá-los para CSV.

### Testes com Pytest

O projeto utiliza Pytest para automatizar verificações do comportamento do código e da validade dos dados.

Os testes ajudam a identificar erros e a preservar o funcionamento esperado durante futuras alterações.

## 8. Persistência e sobrescrita dos dados

Na versão atual, os registros processados são exportados para um arquivo CSV de saída.

Quando a operação de gravação utiliza o modo de escrita que substitui o conteúdo existente, uma nova execução pode sobrescrever o levantamento anterior.

Isso significa que o arquivo de saída não funciona como um histórico de levantamentos. Ele representa apenas o conjunto de dados da última gravação.

A base Excel utilizada como fonte dos produtos é distinta do arquivo CSV de saída. Portanto, a sobrescrita do resultado não implica, por si só, a substituição do catálogo original.

## 9. Possibilidades de evolução

O projeto pode evoluir gradualmente, preservando a estrutura já desenvolvida.

### Histórico de levantamentos

Cada levantamento poderá ser salvo como um registro independente, identificado por data e, se necessário, por um identificador próprio. Isso permitirá consultar levantamentos anteriores sem sobrescrever os dados históricos.

### Análises e relatórios

Com um histórico consistente, o sistema poderá gerar informações como:

- Produto com maior quantidade registrada.
- Produto com menor quantidade registrada.
- Média das quantidades, com critérios de cálculo definidos.
- Variações nas quantidades entre levantamentos.
- Comparações entre períodos.
- Relatórios para apoiar o planejamento de compras.

Essas análises deverão considerar as diferenças entre quantidade contabilizada, consumo, reposição e estoque efetivamente disponível.

### Cadastro de produtos e categorias

Uma versão futura poderá permitir que o usuário cadastre produtos e categorias, em vez de depender exclusivamente de um catálogo previamente definido em Excel.

### Importação de catálogos externos

O sistema poderá aceitar arquivos fornecidos pelo usuário, como planilhas Excel ou arquivos CSV, para construir a lista de produtos de diferentes empresas.

Essa funcionalidade exigirá validação das colunas, dos tipos de dados e da estrutura dos arquivos importados.

### Interface adaptada a dispositivos móveis

Uma interface apropriada para celulares poderá tornar o levantamento mais prático, permitindo o preenchimento das quantidades diretamente no local de trabalho.

## 10. Tecnologias e conhecimentos aplicados

O projeto trabalha com conceitos e ferramentas importantes para o desenvolvimento de software em Python:

- Python.
- Pandas e DataFrames.
- Manipulação de arquivos Excel e CSV.
- Estruturas de dados e listas de objetos.
- Modelagem de dados.
- Persistência de dados.
- Validação de entradas.
- Tratamento de exceções.
- Organização modular do código.
- Separação de responsabilidades.
- Testes automatizados com Pytest.
- Git e GitHub para versionamento e apresentação do projeto.

## 11. Propósito educacional e profissional

Além de resolver um problema operacional concreto, o Lista Operacional funciona como um projeto prático de desenvolvimento de software.

Seu desenvolvimento permite estudar como receber dados, representá-los internamente, validar registros, separar responsabilidades e persistir informações em arquivos estruturados.

O projeto também oferece uma base para estudar evolução de requisitos, manutenção de código, testes e análise de dados.

## 12. Considerações finais

O Lista Operacional é uma primeira versão funcional voltada à digitalização do levantamento de produtos de uma pizzaria.

Seu objetivo atual é tornar a coleta e o registro das quantidades mais diretos. Recursos como histórico, relatórios, comparação entre levantamentos e cadastro dinâmico de produtos fazem parte de possíveis evoluções, e não devem ser considerados funcionalidades já disponíveis enquanto não forem implementados e testados.
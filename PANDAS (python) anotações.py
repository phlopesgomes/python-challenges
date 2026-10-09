### MANIPULAÇÃO E ANÁLISE DE DADOS (PANDAS)

### Pandas é uma biblioteca Python de código aberto para análise de dados.
## Ela fornece ferramentas poderosas e fáceis de usar para manipulação e análise de dados em formatos de tabelas, como CSV, Excel, SQL e muitos outros.

### Com Pandas, podemos carregar dados de várias fontes em um objeto chamado DataFrame, que é uma tabela de dados semelhante a uma planilha do Excel.
## Em seguida, podemos trabalhar com esses dados, realizando operações como filtrar, ordenar, agregar e transformar.

### A biblioteca Pandas é amplamente utilizada em aplicações de ciência de dados, aprendizado de máquina, finanças e análise de negócios.
## Ela é uma ferramenta essencial para profissionais que trabalham com dados, como analistas de dados, cientistas de dados e engenheiros de dados.

## Para utilizar a biblioteca, é necessário importá-la no código Python:
import pandas as pd


#################################################################################################


### Importação de bases de dados;

## Para importar uma base de dados, é necessário informar o caminho do arquivo (path) ou a URL do arquivo (quando o arquivo estiver hospedado na internet).
url = 'link_do_arquivo' 
# Repare que utilizamos uma variável para armazenar a URL do arquivo, assim, caso seja necessário alterar o caminho do arquivo, basta alterar apenas nesta linha de código.

### O Pandas fornece diversas funções para importar e exportar dados em diferentes formatos. 
## As principais funções do Pandas para importar dados são as seguintes:

read_csv() ## Essa função é usada para ler arquivos CSV (Comma Separated Values), que são arquivos de texto que contêm dados separados por vírgulas. É possível passar diversos parâmetros para personalizar a leitura do csv, como delimitador, cabeçalho, tipo de encoding, entre outros.

read_excel() ## Essa função é usada para ler arquivos do Excel (.xls ou .xlsx) e criar um DataFrame a partir dos dados.

read_json() ## Essa função é usada para ler arquivos JSON (JavaScript Object Notation), que são arquivos de texto que contêm dados em formato de objeto JavaScript.

read_html() ## Essa função é usada para ler tabelas HTML, que são estruturas de dados organizadas em formato de tabela em uma página da web.

read_sql() ## Essa função é usada para ler dados de um banco de dados relacional, como o MySQL, PostgreSQL e SQL Server. O Pandas é capaz de importar dados de diferentes formas, permitindo ajustar parâmetros como a consulta, o nome da tabela e o tipo de dados das colunas.

### Utilizando uma função das citadas acima para importar uma base de dados CSV.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)
# Utilizamos a variável url como parâmetro da função pd.read_csv() para informar o caminho do arquivo CSV que queremos ler (é a variável que definimos anteriormente).)

## Por padrão, a função considera que o separador de colunas é a vírgula (,).
# Quando o arquivo utiliza ponto e vírgula (;) como separador, os dados ficam concentrados em uma só coluna se lidos sem especificar o separador.

## Exemplo informando o parâmetro sep=';' para organizar as colunas corretamente:
dados = pd.read_csv(url, sep=';')
dados
# Neste caso, o Pandas entende que o separador de colunas é o ponto e vírgula (;), logo, ele organiza os dados em colunas corretamente.

## type() = verifica o tipo de estrutura da variável armazenada
type(dados)
## Ficará assim no terminal:
# pandas.core.frame.DataFrame


#################################################################################################


### Visualização inicial dos dados (.head() e .tail());

## .head() = exibe por padrão os 5 primeiros registros da base de dados
dados.head()

## É possível passar como parâmetro a quantidade de linhas iniciais desejadas:
dados.head(3) # Exibe os 3 primeiros registros

############################

## .tail() = exibe por padrão os 5 últimos registros da base de dados
dados.tail()

## É possível passar como parâmetro a quantidade de linhas finais desejadas:
dados.tail(3) # Exibe os 3 últimos registros


#################################################################################################


### Inspeção da dimensão e estrutura dos dados (.shape, .columns e .info());

## .shape = atributo que retorna uma tupla (linhas, colunas) com as dimensões do DataFrame
dados.shape
## Ficará assim no terminal:
# (32960, 9)
# O primeiro valor (32960) é a quantidade de linhas; o segundo (9) é a quantidade de colunas.

############################

## .columns = atributo que exibe os nomes de todas as colunas da base de dados
dados.columns
## Ficará assim no terminal:
# Index(['Tipo', 'Bairro', 'Quartos', 'Vagas', 'Suites', 'Area', 'Valor', 'Condominio', 'IPTU'], dtype='object')

# Descrição das colunas:
# Tipo: tipo de imóvel
# Bairro: bairro de localização
# Quartos: quantidade de quartos
# Vagas: quantidade de vagas de garagem
# Suites: quantidade de suítes
# Area: área do imóvel em m²
# Valor: valor do aluguel
# Condominio: valor mensal do condomínio
# IPTU: valor do IPTU'

############################

## .info() = método que exibe o resumo geral do DataFrame
# Informa a quantidade total de registros, valores não nulos (Non-Null Count) e o tipo de dado de cada coluna (Dtype).
dados.info()
## Ficará assim no terminal:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 32960 entries, 0 to 32959
#Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
 # 0   Tipo        32960 non-null  object 
 # 1   Bairro      32960 non-null  object 
 # 2   Quartos     32960 non-null  int64  
 # 3   Vagas       32960 non-null  int64  
 # 4   Suites      32960 non-null  int64  
 # 5   Area        32960 non-null  int64  
 # 6   Valor       32943 non-null  float64
 # 7   Condominio  28867 non-null  float64
 # 8   IPTU        22723 non-null  float64
# dtypes: float64(3), int64(4), object(2)
# memory usage: 2.3+ MB


#################################################################################################


### Tipos de dados no Pandas (dtypes);

## Os principais tipos de dados utilizados no Pandas:
# - object: texto (string) ou colunas com tipos de dados mistos
# - string: tipo estendido exclusivo para texto (mais eficiente que 'object')
# - int64: números inteiros (não aceita valores nulos/NaN)
# - Int64: inteiro estendido do Pandas que aceita valores nulos (NaN)
# - float64: números decimais (ponto flutuante)
# - bool / boolean: valores lógicos (True ou False)
# - datetime64[ns]: datas e horários completos
# - timedelta64[ns]: intervalos ou diferenças entre duas datas
# - category: dados categóricos/rótulos repetidos (otimiza o uso de memória)

############################

## Verificação e conversão de tipos de dados;

## .dtypes = atributo que retorna apenas o tipo de dado de cada coluna
dados.dtypes

############################

## .astype() = método utilizado para converter o tipo de dado de uma coluna

# Exemplo 1: Convertendo a coluna "Quartos" de inteiro (int64) para decimal (float64)
dados['Quartos'] = dados['Quartos'].astype(float)

# Exemplo 2: Convertendo a coluna "Tipo" para o tipo categórico (category)
dados['Tipo'] = dados['Tipo'].astype('category')

############################

## pd.to_datetime() = função recomendada para converter colunas de datas
# dados['Data'] = pd.to_datetime(dados['Data'])


#################################################################################################


### Seleção de colunas e estruturas do Pandas (Series vs DataFrame);

## Seleção de uma única coluna:
# Basta passar o nome do DataFrame e o nome da coluna entre colchetes ['coluna'].
dados['Tipo']
# Retorna uma Series: estrutura unidimensional do Pandas composta por índices e valores.
# Exemplo: dados da coluna "Tipo" são textuais (object / string).

############################

## Seleção de duas ou mais colunas:
# Passa-se uma lista com o nome das colunas dentro de colchetes duplos [['coluna1', 'coluna2']].
dados[['Quartos', 'Valor']]
# Retorna um DataFrame (estrutura bidimensional).
# Exemplo de tipos observados nesta seleção:
# - "Quartos": int64 (números inteiros)
# - "Valor": float64 (números decimais)
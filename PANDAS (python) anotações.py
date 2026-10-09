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


#################################################################################################


### Análise estatística e agrupamento de dados (.mean(), .groupby(), .sort_values() e .plot());

## .mean() = calcula a média dos valores numéricos de uma coluna ou de todo o DataFrame

# Exemplo 1: Média de uma coluna específica (retorna um único número)
dados['Valor'].mean()

# Exemplo 2: Média de todas as colunas numéricas do DataFrame (retorna uma Series com as médias)
dados.mean(numeric_only=True)
# O parâmetro 'numeric_only=True' é utilizado para garantir que apenas as colunas numéricas sejam consideradas no cálculo da média, ignorando colunas de texto ou categóricas.


############################


### Método .groupby() e seus parâmetros;
## .groupby() = divide os dados em grupos com base em uma ou mais colunas para aplicar funções de agregação (como .mean(), .sum(), .count())

# Exemplo 1: Seleção com colchetes simples ['Valor'] -> Retorna uma Series agrupada
dados.groupby('Tipo')['Valor'].mean()
# Neste exemplo, o resultado é uma Series com os tipos de imóveis como índice e a média do valor de aluguel como valores.

# Exemplo 2: Seleção com colchetes duplos [['Valor']] -> Retorna um DataFrame agrupado
dados.groupby('Tipo')[['Valor']].mean()
# Neste exemplo, o resultado é um DataFrame com os tipos de imóveis como índice e a média do valor de aluguel como valores.

### Parâmetros do método .groupby():

## 'by': especifica a coluna ou a lista de colunas usadas para realizar o agrupamento

# Exemplo 1: Agrupando por apenas uma coluna ('Tipo')
dados.groupby(by='Tipo').mean(numeric_only=True)

# Exemplo 2: Agrupando por múltiplas colunas em lista ('Tipo' e 'Bairro')
dados.groupby(by=['Tipo', 'Bairro']).mean(numeric_only=True)


## 'axis': especifica o eixo ao longo do qual os dados serão agrupados (0 para linhas, 1 para colunas)

# Exemplo 1: Agrupando ao longo das linhas (eixo 0 - comportamento padrão)
dados.groupby('Tipo', axis=0).mean(numeric_only=True)

# Exemplo 2: Agrupando ao longo das colunas pelo tipo de dado (eixo 1)
dados.groupby(by=dados.dtypes, axis=1).first()
# Neste exemplo, o DataFrame é agrupado pelo tipo de dado de cada coluna (object, int64, float64), e a função .first() retorna o primeiro valor de cada grupo de colunas.

## 'sort': define se os rótulos dos grupos serão ordenados alfabeticamente/numericamente (True por padrão)

# Exemplo 1: Agrupamento ordenando os nomes dos grupos em ordem alfabética (sort=True)
dados.groupby('Tipo', sort=True).mean(numeric_only=True)

# Exemplo 2: Agrupamento mantendo a ordem original de aparição dos grupos na base (sort=False)
dados.groupby('Tipo', sort=False).mean(numeric_only=True)


## 'dropna': controla se os valores ausentes (NaN) na coluna de agrupamento serão excluídos ou mantidos como um grupo (True por padrão)

# Exemplo 1: Ignorando registros que possuem valor nulo/NaN na coluna de agrupamento (dropna=True)
dados.groupby('Bairro', dropna=True).mean(numeric_only=True)

# Exemplo 2: Incluindo valores nulos (NaN) como uma categoria de grupo própria no resultado (dropna=False)
dados.groupby('Bairro', dropna=False).mean(numeric_only=True)


############################


### .sort_values() = ordena os valores do resultado agrupado;

# Exemplo 1: Ordenação crescente (da menor média de valor para a maior)
dados.groupby('Tipo')[['Valor']].mean().sort_values(by='Valor', ascending=True)

# Exemplo 2: Ordenação decrescente (da maior média de valor para a menor)
dados.groupby('Tipo')[['Valor']].mean().sort_values(by='Valor', ascending=False)


############################


### Visualização gráfica com .plot() = gera gráficos diretamente a partir do DataFrame agrupado;

# Armazenando o resultado agrupado e ordenado em uma variável:
df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Exemplo 1: Plotando um gráfico de barras horizontais ('barh') na cor roxa
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple');
# O parâmetro 'figsize' define o tamanho da figura (largura, altura) em polegadas; o parâmetro 'color' define a cor das barras do gráfico.

# Exemplo 2: Plotando um gráfico de barras verticais ('bar') na cor azul
df_preco_tipo.plot(kind='bar', figsize=(12, 6), color='blue');

### Caso queira aprender mais sobre esse método, deixo a sugestão de dois artigos:

## Pandas GroupBy: Your Guide to Grouping Data in Python (https://realpython.com/pandas-groupby/);
## Pandas Groupby: 5 métodos para conhecer em Python (https://builtin.com/data-science/pandas-groupby).


#################################################################################################


### Notação de ponto, valores únicos (.unique());

## Notação de ponto (.coluna) = forma alternativa e direta de selecionar uma coluna específica do DataFrame (sem usar colchetes)

# Exemplo 1: Selecionando a coluna 'Tipo' utilizando notação de ponto
dados.Tipo

# Exemplo 2: Aplicando métodos diretamente na coluna selecionada por ponto
dados.Bairro.head(3)


### .unique() = retorna um array/lista com todos os valores únicos (sem repetições) de uma coluna ou Series

# Exemplo 1: Visualizando todos os tipos de imóveis únicos presentes na base original
dados.Tipo.unique()

# Exemplo 2: Visualizando todos os bairros únicos cadastrados no DataFrame
dados.Bairro.unique()


#################################################################################################


### .query() = permite filtrar linhas de um DataFrame utilizando uma expressão/condição em formato de texto (string)

## Símbolo '@' no .query() = deve ser colocado antes do nome de uma variável do Python para que o Pandas consiga reconhecê-la dentro da expressão em string

## Operadores 'in' e 'not in' no .query() = verificam se os valores da coluna pertencem ('in') ou não pertencem ('not in') a uma lista de valores


# Definindo a lista de tipos de imóveis comerciais que serão filtrados:
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Hotel', 'Indústria']


# Exemplo 1: Usando 'in' com '@' para selecionar APENAS as linhas que contêm imóveis da lista 'imoveis_comerciais'
dados.query('@imoveis_comerciais in Tipo')


# Exemplo 2: Usando 'not in' com '@' para REMOVER os imóveis comerciais e manter apenas os residenciais em um novo DataFrame
df = dados.query('@imoveis_comerciais not in Tipo')


############################


### Verificação do resultado e re-plotagem com a base filtrada;

# Exemplo 1: Verificando se restaram apenas imóveis residenciais no novo DataFrame 'df'
df.Tipo.unique()

# Exemplo 2: Re-plotando o gráfico de média de valores de aluguel por tipo sem a interferência dos imóveis comerciais
df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple');


#################################################################################################


### Contagem de frequências e percentuais (.value_counts());

### .value_counts() = conta a frequência de ocorrência de cada valor em uma coluna/Series

# Exemplo 1: Contagem absoluta do total de imóveis por tipo
df['Tipo'].value_counts()

# Exemplo 2: Contagem de ocorrências incluindo valores nulos caso existam (dropna=False)
df['Tipo'].value_counts(dropna=False)


############################


### Parâmetro 'normalize': quando True, calcula a proporção/percentual relativo de cada valor (de 0.0 a 1.0) em vez da contagem bruta

# Exemplo 1: Calculando o percentual de cada tipo de imóvel na base de dados
df['Tipo'].value_counts(normalize=True)

# Exemplo 2: Calculando o percentual de imóveis por bairro
df['Bairro'].value_counts(normalize=True)


#################################################################################################


### .to_frame() = converte uma Series (como a retornada pelo .value_counts()) em um DataFrame

# OBSERVAÇÃO (Pandas v2.0+): Ao aplicar .value_counts(normalize=True).to_frame(), a coluna contendo 
# as proporções é nomeada automaticamente como 'proportion' (em versões antigas mantinha o nome original).

# Exemplo 1: Convertendo a Series de percentuais em DataFrame e ordenando pela coluna 'proportion'
df['Tipo'].value_counts(normalize=True).to_frame().sort_values('proportion')

# Exemplo 2: Convertendo uma contagem absoluta em DataFrame
df['Tipo'].value_counts().to_frame()


#################################################################################################


### Renomeando colunas do DataFrame (.rename());
### .rename() = permite alterar os nomes de colunas ou índices do DataFrame a partir de um dicionário de mapeamento


## Parâmetro 'columns': recebe um dicionário mapeando o nome antigo para o novo nome {'nome_antigo': 'nome_novo'}

# Exemplo 1: Renomeando uma única coluna de 'proportion' para 'Percentual'
df_percentual = df['Tipo'].value_counts(normalize=True).to_frame()
df_percentual.rename(columns={'proportion': 'Percentual'})

# Exemplo 2: Renomeando múltiplas colunas simultaneamente em um DataFrame
dados.rename(columns={'Valor': 'Preco_Aluguel', 'Condominio': 'Taxa_Condominio'})


############################


## Parâmetro 'inplace': define se a alteração será aplicada diretamente no próprio DataFrame original (True) sem precisar reatribuir a variável (o padrão é False)

# Exemplo 1: Aplicando a alteração diretamente no DataFrame original sem reatribuição (inplace=True)
df_percentual.rename(columns={'proportion': 'Percentual'}, inplace=True)

# Exemplo 2: Mantendo inplace=False (padrão), o que exige atribuir o resultado de volta à variável
df_percentual = df_percentual.rename(columns={'Tipo': 'Percentuais'}, inplace=False)


#################################################################################################


### Customização de gráficos (.plot()));

## Parâmetros de customização do método .plot():
# - kind='bar': gera um gráfico de barras verticais
# - edgecolor: define a cor da linha de contorno/borda das barras
# - xlabel: define o rótulo/texto exibido no eixo X
# - ylabel: define o rótulo/texto exibido no eixo Y

# Exemplo 1: Plotando gráfico de barras verticais verde com bordas pretas e rótulos nos eixos
df_percentual_tipo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('proportion')
df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color='green', edgecolor='black', xlabel='Tipos', ylabel='Percentual');

# Exemplo 2: Plotando gráfico de barras verticais azuis com bordas vermelhas para a coluna Bairro
df_bairro = df['Bairro'].value_counts(normalize=True).head(5).to_frame()
df_bairro.plot(kind='bar', figsize=(10, 5), color='blue', edgecolor='red', xlabel='Bairros', ylabel='Proporção');


#################################################################################################


## Filtragem por igualdade exata de texto com .query();
# Regra das aspas: ao filtrar valores de texto (string), alterne o tipo de aspas! 
# Se a expressão principal usar aspas simples '...', use aspas duplas "..." no valor procurado (ou vice-versa).

# Exemplo 1: Selecionando apenas os registros cujo tipo é exatamente "Apartamento"
df = df.query('Tipo == "Apartamento"')

# Exemplo 2: Selecionando apenas os imóveis localizados no bairro "Centro"
df_centro = df.query('Bairro == "Centro"')


#################################################################################################


### Verificação e identificação de dados nulos (.isnull() e .isnull().sum());
# O tratamento de dados nulos é fundamental para análises e Machine Learning, já que valores ausentes causam erros ou viés nos modelos.

## .isnull() = retorna um DataFrame/Series booleano com True para posições com dados nulos (NaN) e False para dados preenchidos

# Exemplo 1: Gerando a matriz booleana de verificação de nulos para o DataFrame inteiro
df.isnull()
# Essa função irá retornar um DataFrame do mesmo tamanho do original, mas com valores booleanos (True/False) indicando a presença de nulos.

# Exemplo 2: Verificando se há valores nulos em uma coluna específica
df['Valor'].isnull()


############################


## .sum() aplicado ao .isnull() = como True vale 1 e False vale 0, realiza a soma dos booleanos retornando o total de nulos por coluna

# Exemplo 1: Verificando a quantidade total de valores nulos em cada coluna do DataFrame
df.isnull().sum()

# Exemplo 2: Verificando o total de nulos em uma coluna específica do DataFrame
df['IPTU'].isnull().sum()


#################################################################################################


### Estratégias de tratamento de dados nulos no Pandas;

## 1. Remoção de dados nulos (.dropna()):
# Assim como vimos anteriormente em parâmetros de outras funções, o método .dropna() remove as linhas ou colunas que contenham valores nulos.

## 2. Preenchimento de valores nulos (.fillna()): substitui os valores nulos por um valor fixo ou por métodos de propagação

# Exemplo 1: Preenchendo todos os nulos do DataFrame com o valor 0 e salvando na variável
df = df.fillna(0)

# Exemplo 2: Preenchendo valores nulos de uma coluna específica com o valor 0
df['Condominio'] = df['Condominio'].fillna(0)

############################

## Parâmetro 'method' no .fillna(): permite propagar valores existentes para preencher as lacunas nulas
# - method='ffill' (forward fill): propaga o último valor válido anterior para cobrir o nulo
# - method='bfill' (backward fill): propaga o próximo valor válido posterior para cobrir o nulo

# Exemplo 1: Preenchendo nulos da coluna 'Valor' propagando o valor da linha anterior (ffill)
df['Valor'].fillna(method='ffill')

# Exemplo 2: Preenchendo nulos da coluna 'IPTU' propagando o valor da linha posterior (bfill)
df['IPTU'].fillna(method='bfill')


############################


## 3. Interpolação de dados nulos (.interpolate()): preenche os valores ausentes calculando valores intermediários com base nos vizinhos

# Exemplo 1: Aplicando a interpolação linear nos valores nulos de uma coluna numérica
df['Valor'] = df['Valor'].interpolate()

# Exemplo 2: Aplicando a interpolação em todas as colunas numéricas do DataFrame
df = df.interpolate()


#################################################################################################


### Identificação de índices (.index);

## .index = atributo que retorna os índices (rótulos das linhas) do DataFrame ou Series. É muito útil em conjunto com filtros (como .query()) para capturar os índices de registros específicos que precisam ser isolados ou removidos.

# Exemplo 1: Capturando os índices das linhas que atendem a uma condição e armazenando em uma variável
registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

# Exemplo 2: Visualizando os índices de todas as linhas presentes no DataFrame
df.index

 
#################################################################################################


### Removendo linhas ou colunas do DataFrame (.drop());

## .drop() = método utilizado para remover/deletar linhas ou colunas de um DataFrame.

# Exemplo 1: Removendo do DataFrame as linhas cujos índices foram armazenados na variável
df.drop(registros_a_remover, axis=0, inplace=True)
# O parâmetro 'inplace=True' garante que a alteração seja aplicada diretamente no DataFrame original sem a necessidade de reatribuir a variável.

# Exemplo 2: Removendo uma coluna específica do DataFrame por conter apenas um único valor/categoria
df.drop('Tipo', axis=1, inplace=True)

# Exemplo 3: Removendo múltiplas linhas passando um array/lista com os índices desejados
df.drop([0, 1, 5], axis=0, inplace=True)
# Neste exemplo, as linhas com índices 0, 1 e 5 serão removidas do DataFrame.

# Exemplo 4: Removendo múltiplas colunas simultaneamente passando um array/lista com os nomes das colunas
df.drop(['Tipo', 'IPTU'], axis=1, inplace=True)
# Neste exemplo, as colunas 'Tipo' e 'IPTU' serão removidas do DataFrame.
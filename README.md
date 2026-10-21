# 🐍 Algoritmos, Estrutura de Dados & Análise de Dados

Este repositório contém minhas anotações práticas, rotinas de código e exercícios desenvolvidos durante o curso de **Ciência de Dados para Negócios na FATEC Sebrae e Alura**. O objetivo é documentar de forma estruturada todo o aprendizado — desde a lógica de programação até o tratamento avançado de dados e matemática computacional.

---

## 📝 Conteúdo dos Estudos

### 1️⃣ Fundamentos e Operadores
- **Entrada e Saída:** Interação via terminal com `input()` e `print()`.
- **Aritmética e Operadores:** Operações com divisão inteira (`//`), resto (`%`), potenciação (`**`) e operadores lógicos/comparativos.
- **Estruturas de Controle:** Lógica condicional (`if`, `elif`, `else`) e laços de repetição (`for`, `while`, `break`, `continue`).

### 2️⃣ Estruturas de Dados e Algoritmos
- **Listas e Tuplas:** Operações de fatiamento (*slicing*), ordenação, inserção e remoção.
- **Filas e Pilhas:** Implementação da lógica LIFO (*Stack*) e FIFO (*Queue*).
- **Tipos Abstratos de Dados (TAD):** POO aplicada a classes (`Retangulo`, `Data`), gerenciamento de Nós (`No`) e **Listas Encadeadas**.
- **Recursividade:** Fatorial e sequência de Fibonacci (versões iterativas e recursivas).

### 3️⃣ Análise e Manipulação de Dados (Pandas)
- **Importação e Exportação:** Leitura e salvamento de dados em múltiplos formatos (`CSV`, `Excel`, `JSON`, `HTML`, `SQL`).
- **Inspeção e Estruturas:** Manipulação de `Series` e `DataFrames`, inspeção com `.head()`, `.tail()`, `.info()`, `.shape` e tratamento de tipos de dados (`dtypes`, `.astype()`).
- **Tratamento de Dados Ausentes:** Identificação e tratamento de valores nulos (`.isnull()`, `.fillna()`, `.dropna()`, `.replace()`, `.interpolate()`).
- **Filtragem e Consultas:** Seleção por condições booleanas (`&`, `|`) e queries em texto com `.query()`.
- **Agrupamento e Estatística:** Agregações complexas com `.groupby()`, ordenação (`.sort_values()`), frequências absolutas e relativas (`.value_counts(normalize=True)`).
- **Visualização Gráfica:** Customização completa de gráficos integrados (`.plot()`) — barras verticais e horizontais, linhas com marcadores, paletas de cores, limites, legendas e rotação de eixos.
- **Engenharia de Recursos:** Operações vetorizadas, concatenação de texto e criação de colunas condicionais via `.apply()`, funções `lambda` e mapeamentos (`.map()`).

### 4️⃣ Álgebra Linear Computacional (Matrizes)
- **Criação de Matrizes:** Matriz Identidade (`np.eye`), Nula (`np.zeros`), Linha, Coluna e Quadrada via NumPy.
- **Operações Matriciais:** Transposição (`.T`), multiplicação matricial (`@`), potenciação (`matrix_power`), determinante (`np.linalg.det`) e matriz inversa (`np.linalg.inv`).
- **Cálculo Simbólico:** Resolução de equações algébricas e matrizes com variáveis utilizando SymPy.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.x**
- **Pandas** (Análise, manipulação e visualização de dados)
- **NumPy** (Processamento numérico e computação matricial)
- **SymPy** (Matemática simbólica e resolução de equações)

---

## 📂 Organização do Repositório

```text
.
├── ANOTAÇÕES/
│   ├── PYTHON anotações.py           # Algoritmos, Lógica, Listas e POO
│   ├── PANDAS (python) anotações.py  # Guia completo de manipulação com Pandas
│   └── MATRIZES LINEAR (python)...  # Álgebra Linear e Matrizes com NumPy e SymPy
├── .gitignore                        # Proteção de dados e exclusão de arquivos sensíveis
└── README.md                         # Documentação oficial do repositório

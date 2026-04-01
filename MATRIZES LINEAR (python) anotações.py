### ÁLGEBRA LINEAR (PYTHON);

### MATRIZES;
## Matriz é uma tabela de números, organizada em linhas e colunas.
## Matriz é um tipo de estrutura de dados, que pode ser usada para armazenar e manipular dados de forma eficiente.
## Matriz é uma estrutura de dados bidimensional, ou seja, tem duas dimensões: linhas e colunas.
## Matriz é uma estrutura de dados que pode ser usada para representar sistemas lineares, transformações lineares, entre outros conceitos da álgebra linear.
## Matriz é uma estrutura de dados que pode ser usada para representar gráficos, imagens, entre outros tipos de dados.
## Matriz é uma estrutura de dados que pode ser usada para representar dados em forma de tabela, como por exemplo, uma planilha do Excel.

### Para criar uma matriz em Python, podemos usar a biblioteca NumPy, que é uma biblioteca de álgebra linear e manipulação de arrays. 
# A seguir, um exemplo de como criar uma matriz usando NumPy:
import numpy as np

# Criando uma matriz 2x3
matriz = np.array([[1, 2, 3], # array é uma função da biblioteca NumPy que cria um array (matriz) a partir de uma lista de listas.
                   [4, 5, 6]])

print(matriz)

# A saída será:
# [[1 2 3]
#  [4 5 6]]

#################################################################################################

### MATRIZ LINHA;
## Matriz linha é uma matriz que tem apenas uma linha, ou seja, tem apenas uma dimensão.

## Exemplo de matriz linha:
matriz_linha = np.array([[1, 2, 3]]) # matriz linha

print(matriz_linha)

# A saída será:
# [[1 2 3]]

#################################################################################################

### MATRIZ COLUNA;
## Matriz coluna é uma matriz que tem apenas uma coluna, ou seja, também tem apenas uma dimensão.

## Exemplo de matriz coluna:
matriz_coluna = np.array([[1],
                          [2],
                          [3]]) # matriz coluna

print(matriz_coluna)

# A saída será:
# [[1]
#  [2]
#  [3]]

#################################################################################################

### MATRIZ QUADRADA;
## Matriz quadrada é uma matriz que tem o mesmo número de linhas e colunas, ou seja, tem a mesma dimensão.

## Exemplo de matriz quadrada (2x2):
matriz_quadrada = np.array([[1, 2],
                            [3, 4]]) # matriz quadrada

print(matriz_quadrada)

# A saída será:
# [[1 2]
#  [3 4]]

#######################

## Outro exemplo de matriz quadrada (3x3):
matriz_quadrada_2 = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]) # matriz quadrada

print(matriz_quadrada_2)

# A saída será:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

#################################################################################################

### MATRIZ IDENTIDADE;
## Matriz identidade é uma matriz quadrada que tem 1's na diagonal principal e 0's em todas as outras posições. 
# A matriz identidade é representada pela letra I.

## Exemplo de matriz identidade:
I = np.eye(3)
print (I)

# A saída será:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

## Dimensão da matriz identidade realizada acima:
I.shape # O 'shape' significa que a matriz identidade acima tem 3 linhas e 3 colunas, ou seja, é uma matriz quadrada de ordem 3.

# A saída será:
# (3, 3)

#######################

## Outro exemplo de matriz identidade:
U= np.eye(4)
print (U)

# A saída será:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

## Dimensão da matriz identidade realizada acima:
U.shape # O 'shape' significa que a matriz identidade acima tem 4 linhas e 4 colunas, ou seja, é uma matriz quadrada de ordem 4.

# A saída será:
# (4, 4)

##################################################################################################

### MATRIZ NULA;
## Matriz nula é uma matriz que tem todos os seus elementos iguais a zero.

## Exemplo de matriz nula:
matriz_nula = np.zeros((2, 3)) # matriz nula de 2 linhas e 3 colunas

print(matriz_nula)

# A saída será:
# [[0. 0. 0.]
#  [0. 0. 0.]]

## Outro exemplo de matriz nula:
matriz_nula_2 = np.zeros((3, 3)) # matriz nula de 3 linhas e 3 colunas

print(matriz_nula_2)

# A saída será:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

##################################################################################################

### MATRIZ TRANSPOSTA;
## Matriz transposta é uma matriz que é obtida a partir da troca das linhas pelas colunas de uma matriz.
# A matriz transposta é representada pela letra T.

# Exemplo de matriz transposta:
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# O atributo .T realiza a transposição: a 1ª linha de A vira a 1ª coluna de A.T
print(A.T)

# A saída será:
# [[1 4]
#  [2 5]
#  [3 6]]

## Dimensão da matriz original e da transposta:
print(A.shape)   # Saída: (2, 3) -> 2 linhas e 3 colunas
print(A.T.shape) # Saída: (3, 2) -> 3 linhas e 2 colunas

#######################

## Outro exemplo de matriz transposta (Matriz Coluna para Linha):
# A transposição de uma matriz coluna (nx1) sempre resulta em uma matriz linha (1xn).

B = np.array([[10], 
              [20], 
              [30]]) # Matriz coluna 3x1

# Transpondo a matriz coluna
B_transposta = B.T

print("Matriz Coluna B (3x1): ", B.shape)
print(B)

print("\nMatriz Linha B.T (1x3): ", B_transposta.shape)
print(B_transposta)

# A saída será:
# [[10 20 30]]

##################################################################################################

### MULTIPLICAÇÃO DE MATRIZES;
## Para multiplicar matrizes no NumPy, usamos o operador '@' ou a função np.dot().
# Importante: A ordem importa! A * B é diferente de B * A.

A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

resultado = A @ B 

print("Resultado da Multiplicação A @ B:")
print(resultado)

# A saída será:
# [[19 22]
#  [43 50]]

#######################

## Outro exemplo de multiplicação de matrizes:
# Multiplicando uma matriz 2x2 por uma 2x1 (como no Exercício 65)
M_a = np.array([[2, 1], 
                [3, 2]])
M_b = np.array([[2], 
                [1]])

resultado_65 = M_a @ M_b
print("65. Resultado da multiplicação: ", resultado_65)

# A saída será:
# [[5]
#  [8]]
##################################################################################################

### MATRIZ INVERSA;
## Uma matriz A tem inversa se for quadrada e seu determinante for diferente de zero.
# Usamos np.linalg.inv() para calcular.

A = np.array([[2, -5], 
              [-1, 3]])

# Calculando a inversa (como no Exercício 58 da sua aula)
A_inv = np.linalg.inv(A)

print("Matriz Inversa de A:")
print(A_inv)

## Verificação: A @ A_inv deve resultar na Identidade
print("\nVerificando (A @ A_inv):")
print(np.round(A @ A_inv)) # Usamos round para limpar resíduos numéricos

#######################

## Outro exemplo de matriz inversa (3x3):
# Calculando a inversa de uma matriz de ordem 3 (como no Exercício 66)
X66 = np.array([[1, 0, 2], 
                [0, 3, 0], 
                [2, 0, 1]])

X66_inv = np.linalg.inv(X66)
print("66. Inversa da Matriz 3x3: ", X66_inv)

# Dica: Use np.round(X66 @ X66_inv) para confirmar que volta para a Identidade.

##################################################################################################

### INTERPRETAÇÃO GEOMÉTRICA;
## Matrizes podem ser vistas como transformações lineares.
# Multiplicar um vetor por uma matriz identidade não muda sua posição.
# Multiplicar por uma matriz diagonal pode esticar ou encolher o vetor.

vetor = np.array([1, 2])
transformacao = np.array([[2, 0], 
                         [0, 2]]) # Dobra o tamanho em ambos os eixos

novo_vetor = transformacao @ vetor
print("Vetor original:", vetor)
print("Vetor transformado (esticado):", novo_vetor) # [2, 4]

#######################

## Outro exemplo de interpretação geométrica (Reflexão):
# Uma matriz que inverte o sinal de X faz uma reflexão no eixo Y.
vetor_p = np.array([5, 3])
reflexao_y = np.array([[-1, 0], 
                       [ 0, 1]])

vetor_refletido = reflexao_y @ vetor_p
print("Vetor original: ", vetor_p)
print("Vetor após reflexão no eixo Y: ", vetor_refletido) # Saída: [-5, 3]

##################################################################################################

### DETERMINANTE;
## O determinante é um valor numérico associado a uma matriz quadrada.
# Usamos np.linalg.det() para calcular.

# Exemplo de matriz 3x3 (como na Questão 6a da sua lista)
M = np.array([[3, 2, 1], 
              [1, 2, 5], 
              [1, -1, 0]])

det = np.linalg.det(M)

print("Determinante da matriz M:")
print(round(det)) # O round ajuda a mostrar o valor inteiro (ex: 34)

#######################

## Outro exemplo de determinante (Matriz Triangular):
# Em matrizes triangulares, o det é o produto da diagonal principal (Exercício 16c)
M16c = np.array([[5, 1, 8, 6],
                 [0, 3, 7, 5],
                 [0, 0, 2, 2],
                 [0, 0, 0, -2]])

det_16c = np.linalg.det(M16c)
print("16c. Determinante (5 * 3 * 2 * -2): ", round(det_16c))

# A saída será: -60

##################################################################################################

### VARIÁVEIS SIMBÓLICAS;
## Quando precisamos resolver equações ou lidar com letras (x, a, b), usamos a biblioteca SymPy.
import sympy as sp

# Definindo o símbolo x
x = sp.Symbol('x')

# Criando uma matriz com x (como na Questão 3 da sua lista)
matriz_x = sp.Matrix([[x, x+2], 
                      [5, 3]])

# Calculando o determinante simbólico
det_simbolico = matriz_x.det()

print("Determinante Simbólico:")
print(det_simbolico) # Saída: 3*x - 5*(x + 2)

# Resolvendo a equação det = x
equacao = sp.Eq(det_simbolico, x)
solucao = sp.solve(equacao, x)

print("\nSolução da equação para x:")
print(solucao)

#######################

## Outro exemplo de variáveis simbólicas (Equação de 2º grau):
# Resolvendo determinante que resulta em equação (como no Exercício 2)
x_sym = sp.Symbol('x')
matriz_eq = sp.Matrix([[x_sym, -3], 
                       [x_sym + 2, x_sym - 2]])

# Resolvendo: det(matriz) = 8
solucao_eq2 = sp.solve(sp.Eq(matriz_eq.det(), 8), x_sym)
print("2. Raízes de x para det=8: ", solucao_eq2)

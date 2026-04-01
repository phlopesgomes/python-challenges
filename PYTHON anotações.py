### ALGORITMOS E ESTRUTURA DE DADOS (PYTHON);

# print serve para o usuário rodar o programa e ver o resultado
# input serve para o usuário digitar algo no programa (terminal)

# + serve para somar números
# - serve para subtrair números
# * serve para multiplicar números 
# / serve para dividir números (com vírgula, número decimal) (5 / 2 = 2.5)
# // serve para dividir números inteiros (sem vírgula, arredondado para baixo) (5 // 2 = 2, porque 5 dividido por 2 é 2,5, arredondado para baixo é 2)
# % serve para mostrar o resto da divisão entre dois números (5 % 2 = 1, porque 5 dividido por 2 é 2, com resto 1)
# ** serve para elevar um número a uma potência (2**3 = 2 elevado a 3 = 8)
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# float serve para o usuário digitar números com vírgula
# int serve para o usuário digitar números inteiros
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("\nIsso é tudo, pessoal!")

x = float(input("Digite o valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x))) # "1." é o mesmo que "1.0"
print("y =", y) # sempre digitar o que o usuário digita e o resultado

name = input("Digite seu nome: ")
print("Olá, " + name + ". Prazer em conhecê-lo!")
 
print("\nPressione Enter para finalizar o programa.")
input()
print("O FIM.")
 
x = int(input("Digite um número: ")) # O usuário digita 2
print(x * "5")

#################################################################################################

## Operadores de comparação;

# == igual a
# != diferente de
# < menor que
# <= menor ou igual a
# > maior que
# >= maior ou igual a
2 == 2 # True
2 == 2.0 # True
2 == 3 # False
2 != 3 # True
2 < 3 # True
2 <= 3 # True
2 > 3 # False 
2 >= 3 # False
2 < 2 # False
2 <= 2 # True

var = 0 # Atribuindo 0 a var
print(var == 0)

var = 1 # Atribuindo 1 a var
print(var == 0)

n = int(input("Digite um número: ")) 
print(n >= 100) 

# Criando variáveis booleanas
the_weather_is_good = True
tickets_are_available = False
table_is_available = False

def go_for_a_walk():
    print("Vou dar um passeio!")

def go_to_the_theater():
    print("Vou ao teatro!")

def go_for_lunch():
    print("Vou almoçar!")

def play_chess_at_home():
    print("Vou jogar xadrez em casa!")

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

    #Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)
 
############################

# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)

############################

# Usar "largest_number" para o maior número e "smallest_number" para o menor número
smallest_number = number1
if number2 < smallest_number:
    smallest_number = number2
if number3 < smallest_number:
    smallest_number = number3
print("O menor número é:", smallest_number)

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir para a linha 02
 
# Também usar "max()" para o maior número e "min()" para o menor número

#################################################################################################

## Estruturas de controle de fluxo ("if", "elif", "else", "while", "for", "break", "continue");

## "if" = se
## "elif" = senão se
## "else" = senão
name = input("Insira o nome da flor: ")
if name == "Spathiphyllum":
    print("Sim - Spathiphyllum é a melhor planta de todos os tempos!")
elif name == "spathiphyllum":
    print("Não, eu quero uma grande Spathiphyllum!")
else:
    print("Spathiphyllum! Não", name + "!")

    secret_number = 777

user_number = int(input("Insira um número: "))

############################

## while = enquanto
codigo_secreto = "chupacabra"
palavra = ""  # só para inicializar

# Enquanto a palavra não for igual ao código secreto
while palavra != codigo_secreto:
    palavra = input("Digite uma palavra para sair do loop: ")
    if palavra != codigo_secreto:
        print("Errado! Tente novamente.")

print("Você saiu do loop com sucesso!")

# finge que o número secreto é 777
while True:
    if user_number != secret_number:
        print("Ha ha! Você está preso no meu loop!")
        user_number = int(input("Tente novamente: "))
    else:
        print("Muito bem, trouxa! Você está livre agora.")

############################

## for = loop para uma quantidade específica de vezes (pode contar mais de um argumento)
## range = intervalo de números (começa do 0, vai até o número antes do final)
for i in range(5):
    print("i é igual a", i)
# range(5) = 0, 1, 2, 3, 4 (5 números, não inclui o 5)

# range(2, 5) = 2, 3, 4 (não inclui o 5)
for i in range(2, 5):
    print("i é igual a", i)

# range(2, 10, 3) = 2, 5, 8 (começa em 2, vai até 10, contando de 3 em 3)
for i in range(2, 10, 3):
    print("i é igual a", i)

# a função "range()" não aceita números com vírgula (float), também não aceita o argumento "start" maior que o argumento "stop"

power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2

############################

## power significa potência
## expo significa expoente
# *= significa "multiplicado por igual a" (power = power * 2)
# /= significa "dividido por igual a" (power = power / 2)
# += significa "mais igual a" (power = power + 2)
# -= significa "menos igual a" (power = power - 2)
# **= significa "elevado a igual a" (power = power ** 2)
# //= significa "dividido inteiro por igual a" (power = power //
# %= significa "resto da divisão por igual a" (power = power % 2)

############################

## break = sair do loop
## continue = pular para a próxima iteração do loop
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i , "é um número ímpar")
    if i == 7:
        break
# i % 2 == 0 significa que i é par
# i % 2 != 0 significa que i é ímpar
# i % 2 == 1 também significa que i é ímpar
# i % 2 != 1 também significa que i é par

## Usando o "while true" para criar um loop infinito
codigo_secreto = "chupacabra"

while True:  # loop infinito
    secreto = input("Digite uma palavra para sair do loop: ")
    if secreto == codigo_secreto:   # se acertar, sai do loop
        print("Você saiu do loop com sucesso!")
        break   # encerra o loop
    else:
        print("Errado! Tente novamente.")

#################################################################################################

## Listas;

## listas são coleções de itens (números, palavras, etc)
## listas são mutáveis (podem ser alteradas)
## [n°] = acessar item na posição n (começa do 0) 
    lista = [1, 2, 3]
    lista.append(4)
    print(lista) # imprime [1, 2, 3, 4]
    lista.remove(2)
    print(lista) # imprime [1, 3, 4]
    print(lista[0]) # imprime 1 (primeiro item da lista)
    print(lista[1]) # imprime 3 (segundo item da lista)
    print(lista[-1]) # imprime 4 (último item da lista)
    print(len(lista)) # imprime 3 (número de itens na lista)
# len() = comprimento da lista

############################
 
## remove() = remover item da lista / del() = deletar item da lista
## "del hat_list[0] ="remove o primeiro item da lista

## .pop() = remover e retornar o último item da lista
hat_list = [1, 2, 3, 4, 5]  # lista original
hat_list[2] = int(input("Digite um número inteiro para substituir o do meio: ")) # índices começam em 0, então 2 é o terceiro item
hat_list.pop()
print("Comprimento da lista:", len(hat_list))
print("Lista atual:", hat_list)

## append() = adicionar item no final da lista
## insert() = adicionar item em uma posição específica da lista
numbers = [111, 7, 2, 1]

print(len(numbers)) # Mostra o comprimento da lista (número de itens na lista)

print(numbers)

numbers.append (4) # Adiciona o número 4 no final da lista

print(len(numbers)) # Agora o comprimento da lista é 5, porque adicionamos um número no final

print(numbers)

numbers.insert (0, 222) # 0 é a posição, 222 é o número a ser inserido

print(len (numbers)) # Agora o comprimento da lista é 6, porque adicionamos um número no início
print(numbers)

############################

# Usando "for" e "range()" no exemplo de "append()"";
my_list = [] # Criando uma lista vazia.

for i in range(5):
   my_list.append (i + 1)

print (my_list)

############################

# Usando "for" e "range()" no exemplo de "insert()";
my_list = []  # Criando uma lista vazia.
 
for i in range(5): 
    my_list.insert(0, i + 1) # Inserindo no início da lista.  
 
print(my_list) # A lista agora é [5, 4, 3, 2, 1]

############################

# Você também pode trocar itens na lista de lugar
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)
my_list[0], my_list[4] = my_list[4], my_list[0]  # Troca o primeiro e o último item
print("Lista após a troca:", my_list)

############################

# Outro exemplo;
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0] # Troca o primeiro e o último item
my_list[1], my_list[3] = my_list[3], my_list[1] # Troca o segundo e o penúltimo item
 
print(my_list) # A lista agora é [5, 3, 8, 1, 10]

############################

# Novo exemplo de lista (os Beatles);

# Etapa 1
beatles = [] # cria uma lista vazia
print("Etapa 1:", beatles)


# Etapa 2
beatles.append("John Lennon") # adiciona "John Lennon" no final da lista
beatles.append("Paul McCartney") # adiciona "Paul McCartney" no final da lista
beatles.append("George Harrison") # adiciona "George Harrison" no final da lista
print("Etapa 2:", beatles)


# Etapa 3
for i in range(2):  # vamos pedir 2 vezes
    novo_membro = input("Digite o nome do novo membro: ") # Serão "Pete Best" e "Stu Sutcliffe"
    beatles.append(novo_membro)
print("Etapa 3:", beatles)


# Etapa 4
del beatles[-1]  # remove o último (Pete Best)
del beatles[-1]  # remove o penúltimo (Stu Sutcliffe)
print("Etapa 4:", beatles)

# Etapa 5
beatles.insert(0, "Ringo Starr") # adiciona "Ringo Starr" no início da lista
print("Etapa 5:", beatles)

print("O fabuloso", len(beatles)) # testando o tamanho da lista

############################

# Agora colocando uma lista em ordem crescente
my_list = [3, 2, 5, 4, 1]
my_list.sort() # coloca a lista em ordem crescente
print(my_list) # imprime [1, 2, 3, 4, 5]

############################

# Exemplo de acordo com o curso;
my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

############################

## reverse() = inverte a ordem dos itens na lista
my_list = [1, 2, 3, 4, 5]
my_list.reverse() # inverte a ordem dos itens na lista
print(my_list) # imprime [5, 4, 3, 2, 1]

############################

## fatiamento de listas (slicing)
# a função [:] cria uma cópia rasa (shallow copy) da lista, ou seja, uma nova lista com os mesmos itens, mas em um local diferente na memória
list_1 = [1]            # list_1 = [1]
list_2 = list_1[:]      # list_2 = [1] (cópia)
list_1[0] = 2           # list_1 agora é [2], list_2 continua [1]
print(list_2)           # imprime [1]

# exemplo de fatiamento (slicing)
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])  # imprime [1, 2, 3] (do índice 1 ao 3)
print(my_list[:3])   # imprime [0, 1, 2] (do início ao índice 2)
print(my_list[3:])   # imprime [3, 4, 5] (do índice 3 ao fim)
print(my_list[:])    # imprime [0, 1, 2, 3, 4, 5] (cópia da lista inteira)

############################

# "in" e "not in" = verificar se um item está ou não na lista ("in" está na lista, "not in" não está na lista)
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#################################################################################################
 
## Funções; 

## função = quando você quer reutilizar um pedaço de código várias vezes, você define uma função e depois chama essa função quando precisar
## def() = define uma função
def message(): # define a função "message", vale ressaltar que uma função deve ter parênteses e dois pontos no final
    print("Entre um valor: ")
 
print("Começamos aqui.")
message() # aqui eu chamei a função "message", então ela vai imprimir "Entre um valor: "
print("terminamos aqui.")

# Ficará assim no terminal:
# Começamos aqui.
# Entre um valor:
# terminamos aqui.

# Você não pode chamar uma função antes de defini-la
# Você pode definir várias funções e chamá-las na ordem que quiser
# Você também pode usar funções em um arquivo com variáveis e listas, mas não pode ter o mesmo nome para uma variável e uma função

def hello(name): # definindo uma função
    print("Olá,", name) # o corpo da função
 
 
name = input("Entre um valor: ")
 
hello(name) # chamando a função

# Ficará assim no terminal:
# Entre um valor: (usuário digita algo, por exemplo: "Ana")
# Olá, Ana

############################

############################

# pass = quando você quer definir uma função, mas ainda não tem código para colocar dentro dela, você pode usar "pass" para indicar que a função está vazia por enquanto;
# Exemplo de função com "pass":
def message(number):
    pass # ainda não tem código para colocar aqui, mas a função está definida

print("A função message foi definida, mas ainda não faz nada.")

# Ficará assim no terminal:
# A função message foi definida, mas ainda não faz nada.


# parâmetros = valores que você passa para a função quando a chama
def message(number): # "number" é um parâmetro da função "message"
    print("Digite um número:", number) 
 
message(1) # chamando a função com o argumento 1, ou seja, "number" vai valer 1

# Ficará assim no terminal:
# Digite um número: 1 

############################

# Outro exemplo de função com parâmetros:
def message(number):
    print("Digite um número:", number)
 
message(1)
message(2)

# Ficará assim no terminal:
# Digite um número: 1
# Digite um número: 2 

############################

# É possível ter uma variável com o mesmo nome do parâmetro da função?
def message(number):
    print("Digite um número:", number)
 
number = 1234 # variável com o mesmo nome do parâmetro
message(1)
print(number)

# Ficará assim no terminal:
# Digite um número: 1
# 1234
# a variável "number" não interfere no parâmetro "number" da função

############################

# Também podemos ter mais de um parâmetro na função
def message(number1, number2): # dois parâmetros
    print("Número 1:", number1)
    print("Número 2:", number2)

message(1, 2) # dois argumentos 

# Ficará assim no terminal:
# Número 1: 1
# Número 2: 2

############################

# Outro exemplo de função com mais de um parâmetro:
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 
# Ficará assim no terminal:
# Olá meu nome é Luke Skywalker
# Olá meu nome é Jesse Quick
# Olá meu nome é Clark Kent

############################

# Também podemos fazer assim;
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# Ficará assim no terminal:
# Olá meu nome é James Bond
# Olá meu nome é Luke Skywalker

# Dessa forma, a ordem dos argumentos não importa quando usamos os nomes dos parâmetros

############################

# A função "adding()" é utilizada para somar números
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

# Ficará assim no terminal:
# 1 + 2 + 3 = 6

############################

# Também podemos fazer assim;
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    adding(c = 1, a = 2, b = 3)

# Ficará assim no terminal:
# 2 + 3 + 1 = 6 , porque a ordem dos argumentos não importa quando usamos os nomes dos parâmetros

############################

# Podemos definir valores padrão para os parâmetros da função;
def introduction(first_name, last_name="Smith"): # "last_name" tem valor padrão "Smith"
    print("Olá meu nome é", first_name, last_name)

introduction("John") # só passamos o argumento para "first_name" 

# Ficará assim no terminal:
# Olá meu nome é John Smith

############################

# Outro exemplo de função com valor padrão:
def introduction(first_name="Jane", last_name="Smith"): # ambos os parâmetros têm valores padrão
    print("Olá meu nome é", first_name, last_name)

introduction() # não passamos nenhum argumento, então ambos os parâmetros usam seus valores padrão

# Ficará assim no terminal:
# Olá meu nome é Jane Smith

############################

# return = quando você quer que a função devolva um valor para quem a chamou, você usa o "return"
# Exemplo de função com return:
def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes: # se "wishes" for False, sai da função
        return 
 
    print("Feliz Ano Novo!")
 
happy_new_year() # chama a função sem argumentos, então "wishes" vale True

# Ficará assim no terminal:
# Três...
# Duas...
# Uma...
# Feliz Ano Novo!

############################

# Agora usando com o argumento False;
def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes: # se "wishes" for False, sai da função
        return 
 
    print("Feliz Ano Novo!")

happy_new_year(False) # chama a função com o argumento False, então "wishes" vale False

# Ficará assim no terminal:
# Três...
# Duas...
# Uma...
# (não imprime "Feliz Ano Novo!" porque "wishes" é False e a função saiu antes disso)

############################

# função return com expressão;
def boring_function(): # define a função
    return 123 # retorna o valor 123 para quem chamou a função, no caso "boring_function()"

x = boring_function() # chama a função e armazena o valor retornado em "x" (lembrando que "x" é uma variável), que vale 123

print("A função boring_function retornou seu resultado. Isso é:", x)

# Ficará assim no terminal:
# A função boring_function retornou seu resultado. Isso é: 123

############################

# valor "None";
def boring_function(): # define a função
    return # não retorna nada, então retorna "None"

x = boring_function() # chama a função e armazena o valor retornado em "x" (lembrando que "x" é uma variável), que vale None
print("A função boring_function retornou seu resultado. Isso é:", x)

# Ficará assim no terminal:
# A função boring_function retornou seu resultado. Isso é: None

############################

# Outro exemplo de função com return e valor None;
def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # saídas: 12
 
 
def multiply(a, b):
    return # não retorna nada, então retorna "None"
 
print(multiply(3, 4)) # saídas: None
 
# Ficará assim no terminal:
# 12
# None

############################

# Outro exemplo de função com return e valor None;
def is_int(data):
    if type(data) == int: # se o tipo de "data" for inteiro
        return True
    elif type(data) == float: # se o tipo de "data" for float (número com vírgula)
        return False
 
print(is_int(5)) # chama a função com o argumento 5, que é inteiro, então retorna True
print(is_int(5.0)) # chama a função com o argumento 5.0, que é float, então retorna False
print(is_int("5")) # chama a função com o argumento "5", que é string, então retorna None

# Ficará assim no terminal:
# True
# False
# None

############################

# Funções com listas;
def strange_list_fun(n):
	strange_list = [] # cria uma lista vazia, depois adiciona números nela
	
	for i in range(0, n): # de 0 até n-1
		strange_list.insert(0, i) # insere o número i na posição 0 da lista (sempre no início)
	
	return strange_list 

print(strange_list_fun(5)) # chama a função com o argumento 5, então a lista terá os números de 0 a 4, sempre inseridos no início da lista

# Ficará assim no terminal:
# [4, 3, 2, 1, 0] (a lista tem 5 números, de 0 a 4, mas como sempre inserimos no início, o 4 fica na frente)

############################

# Exemplo de função com lista, definindo anos bissextos;
def is_year_leap(year): # define a função com o parâmetro "year"
 if year % 4 != 0: # se o ano não for divisível por 4, não é bissexto, ou seja, retorna False
    return False
 elif year % 100 != 0: # se o ano for divisível por 4, mas não por 100, é bissexto, ou seja, retorna True
    return True
 elif year % 400 != 0: # se o ano for divisível por 100, mas não por 400, não é bissexto, ou seja, retorna False
    return False
 else: # se o ano for divisível por 400, é bissexto, ou seja, retorna True
    return True


test_data = [1900, 2000, 2016, 1987] # anos para testar a função
test_results = [False, True, True, False] # resultados esperados para os anos (1900 não é bissexto, 2000 é bissexto, 2016 é bissexto, 1987 não é bissexto)
for i in range(len(test_data)): # para cada índice na lista de anos
    yr = test_data[i] # pega o ano na posição i da lista, que são 1900, 2000, 2016 e 1987 e armazena na variável "yr"
    print(yr,"-> ",end="") # imprime o ano e a seta "-> ", sem pular linha (end="") 
    
    result = is_year_leap(yr) # chama a função com o ano "yr" e armazena o resultado na variável "result"
    if result == test_results[i]: # se o resultado for igual ao esperado na lista "test_results"
        print("OK") # imprime "OK"
    else: # se o resultado for diferente do esperado
        print("Fracassado") # imprime "Fracassado"

# Ficará assim no terminal:
# 1900 -> OK               (porque 1900 não é bissexto)
# 2000 -> OK               (porque 2000 é bissexto)
# 2016 -> OK               (porque 2016 é bissexto)
# 1987 -> OK               (porque 1987 não é bissexto)

############################

# Outro exemplo de função com lista;
def even_num_lst(ran): # define a função com o parâmetro "ran"
    lst = [] # cria uma lista vazia
    for num in range(ran): # para cada número de 0 até ran-1 
        if num % 2 == 0: # se o número for par (divisível por 2)
            lst.append(num) # adiciona o número na lista
    return lst # retorna a lista com os números pares
 
print(even_num_lst(11)) # chama a função com o argumento 11, então a lista terá os números pares de 0 a 10

# Ficará assim no terminal:
# [0, 2, 4, 6, 8, 10]            (números pares de 0 a 10)

#################################################################################################

## Escopo de variáveis (local e global);
def my_function():
    var = 2 # variável local, só existe dentro da função
    print("Eu conheço aquela variável?", var) # imprime o valor da variável local, que é 2
 
var = 1 # variável global, existe fora da função, não tem relação com a variável local
my_function() # chama a função, que imprime o valor da variável local
print(var) # imprime o valor da variável global

# Ficará assim no terminal:
# Eu conheço aquela variável? 2
# 1

############################

# Usando "global" para modificar uma variável global dentro de uma função;
def my_function():
    global var # diz que vamos usar a variável global "var" dentro da função
    var = 2
    print("Eu conheço aquela variável?", var)

var = 1 # variável global, se modificada dentro da função, o valor muda para 2
my_function()
print(var)

# Ficará assim no terminal:
# Eu conheço aquela variável? 2
# 2               (agora a variável global foi modificada para 2 dentro da função)

############################

# Mais um exemplo de escopo de variáveis, sem ativar o "global";
def my_function(n): # define a função com o parâmetro "n"
 print("Eu obtive", n) # imprime o valor de "n"
 n += 1 # n = n + 1
 print("Eu tenho", n) # imprime o valor de "n" + 1


var = 1
my_function(var) # chama a função com o argumento "var", que vale 1
print(var)

# Ficará assim no terminal:
# Eu obtive 1
# Eu tenho 2
# 1               (a variável global "var" continua 1, porque a variável "n" é local e não modifica "var")

############################

# Exemplos de escopos usando "global";
a = 1
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
fun() # chama a função antes de modificar a variável global "a" para 2
a = 3 
print(a)
 
# Ficará assim no terminal:
# 2
# 3               (a variável global "a" foi modificada para 2 dentro da função, depois foi modificada para 3 fora da função)

############################

# Este próximo exemplo é parecido, mas não igual;
a = 1
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
a = 3
fun() # chama a função, que modifica a variável global "a" para 2
print(a)
 
# Ficará assim no terminal:
# 2
# 2              (a variável global "a" foi modificada para 2 dentro da função, depois a função foi chamada e imprimiu 2, depois imprimiu 2 novamente, porque "a" já era 2)

#################################################################################################

## Fatorial;
# fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n, ele é representado por "n!"
# Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120

# 0! = 1 
# 1! = 1
# 2! = 1 * 2 
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4

# exemplo de função para calcular o fatorial de um número;
def factorial_function(n): # define a função "factorial_function" com o parâmetro "n"
    if n < 0: # se n for negativo, não existe fatorial
        return None
    if n < 2: # se n for 0 ou 1, o fatorial é 1
        return 1
 
    product = 1 # inicializa a variável "product" com 1
    for i in range(2, n + 1): # para cada número de 2 até n (incluindo n)
        product *= i # multiplica "product" pelo número i (product = product * i)
    return product # retorna o valor de "product", que é o fatorial de n
 
 
for n in range(1, 6): # testando a função com os números de 1 a 5
    print(n, factorial_function(n)) # chama a função com o argumento n, que vale de 1 a 5

# Ficará assim no terminal:
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120

############################

# Exemplo de função recursiva para calcular o fatorial de um número;
def fatorial(n): # define a função "fatorial" com o parâmetro "n"
    if n == 0: # se n for 0, o fatorial é 1
        return 1
    else: # se n for maior que 0, calcula o fatorial
        return n * fatorial(n - 1) # chama a função recursivamente, multiplicando n pelo fatorial de n-1

print(fatorial(5)) # chama a função com o argumento 5, então calcula 5 * 4 * 3 * 2 * 1 = 120

# Ficará assim no terminal:
# 120

############################

# Fatorial em prática;
def fatorial(n):
    if n == 0 or n == 1: # Caso base
        return 1
    return n * fatorial(n - 1) # Passo recursivo

print(fatorial(5)) # 120

# ficará assim no terminal:
# 120

#################################################################################################

## números de Fibonacci;
# a sequência de Fibonacci é uma sequência infinita de números inteiros, onde cada número é a soma dos dois anteriores
# a sequência começa com 0 e 1, então os próximos números são 1,(1+1) 2,(1+2) 3,(2+3) 5,(3+5) 8,(5+8) 13,(8+13) 21,(13+21) 34, etc
def fibonacci(n): # define a função "fibonacci" com o parâmetro "n"
    if n == 0: # se n for 0, o resultado é 0
        return 0
    elif n == 1: # se n for 1, o resultado é 1
        return 1
    else: # se n for maior que 1, calcula o n-ésimo número de Fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2) # chama a função recursivamente

for i in range(10): # testando a função com os primeiros 10 números de Fibonacci
    print(fibonacci(i))

# Ficará assim no terminal:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

############################

# Exemplo da função Fibonacci;
def fib(n):
    if n < 1: # se n for menor que 1, não existe Fibonacci
        return None
    if n < 3: # se n for 1 ou 2, o resultado é 1
        return 1

    elem_1 = elem_2 = 1 # os dois primeiros elementos da sequência são 1 (elem_1 e elem_2 são variáveis que armazenam os dois últimos números da sequência)
    the_sum = 0 # inicializa a variável "the_sum" com 0 (essa variável vai armazenar o próximo número da sequência)
    for i in range(3, n + 1): # para cada número de 3 até n (incluindo n)
        the_sum = elem_1 + elem_2 # calcula o próximo número da sequência (a soma dos dois últimos números)
        elem_1, elem_2 = elem_2, the_sum # atualiza os dois últimos números (elem_1 recebe o valor de elem_2, e elem_2 recebe o valor de the_sum)
    return the_sum
 
 
for n in range(1, 10):  # testando a função com os números de 1 a 9
    print(n, "->", fib(n)) # chama a função com o argumento n, que vale de 1 a 9
 
# Ficará assim no terminal:
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34

############################

# recursividade de cauda (tail recursion);
# uma função é recursiva de cauda quando a chamada recursiva é a última operação realizada pela função (ela chama a si mesma como seu último ato)
def tail_fib(n, elem_1=1, elem_2=1): # define a função "tail_fib" com o parâmetro "n" e os parâmetros padrão "elem_1" e "elem_2"
    if n < 1: # se n for menor que 1, não existe Fibonacci
        return None
    if n < 3: # se n for 1 ou 2, o resultado é 1
        return 1
    if n == 3: # se n for 3, o resultado é a soma dos dois últimos números (elem_1 + elem_2)
        return elem_1 + elem_2
    return tail_fib(n - 1, elem_2, elem_1 + elem_2) # chama a função recursivamente, diminuindo n em 1, atualizando os dois últimos números (elem_2 e a soma dos dois últimos números)

for n in range(1, 10): # testando a função com os números de 1 a 9
    print(n, "->", tail_fib(n)) # chama a função com o argumento n, que vale de 1 a 9

# Ficará assim no terminal:
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34

############################

# Outro exemplo de função recursiva para calcular o n-ésimo número de Fibonacci;
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
 
for n in range(1, 10):
    print(n, "->", fib(n))

# Ficará assim no terminal:
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34

############################

# Recursividade em prática;
def contagem_regressiva(n):

    if n == 0: # Caso base​
        print("Fim!")
    else:
        print(n)
        contagem_regressiva(n - 1) # Passo recursivo


contagem_regressiva(5)

# Ficará assim no terminal:
# 5
# 4
# 3
# 2
# 1
# Fim!

############################

# Recursivo

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6)) # 8 é o 6 valor calculado​

############################

# Iterativo

def fibonacci_iterativo(n):

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterativo(6)) # 8

# ficará assim no terminal:
# 8

############################

# Tipos abstratos de dados (ADT - Abstract Data Types);
class Data:  # define a classe "Data"

    def __init__(self):  # define o construtor da classe
        self.dia = 0  # inicializa o atributo "dia" com 0
        self.mes = 0  # inicializa o atributo "mes" com 0
        self.ano = 0  # inicializa o atributo "ano" com 0

############################

# Um Tipo Abstrato de Dados também pode possuir operações (funções);
class Retangulo: # define a classe "Retangulo"
    def __init__(self): # definindo a função com parâmetro construtora da classe
        self.altura = 0 # inicializa o atributo "altura" com 0
        self.largura = 0 # inicializa o atributo "largura" com 0

    # funções(operações)
    def perimetro(self): # define a função "perimetro" com o parâmetro "self" (que representa a instância da classe)
        return (self.altura * 2) + (self.largura * 2) # retorna o perímetro do retângulo

    def area(self): # define a função "area" com o parâmetro "self"
        return self.altura * self.largura # retorna a área do retângulo


ret = Retangulo() # cria um objeto "ret" da classe "Retangulo"

ret.altura = 10 # atribui o valor 10 ao atributo "altura" do objeto "ret"
ret.largura = 5 # atribui o valor 5 ao atributo "largura" do objeto "ret"

print("Perimetro = ",ret.perimetro())

print("Area = ",ret.area())

# Ficará assim no terminal:
# Perimetro =  30
# Area =  50

#################################################################################################

# como instalar módulos (bibliotecas) no Python;
# pip install nome_do_módulo
# instalar pandas;
# escreva no terminal "pip install pandas" para instalar o módulo pandas
import pandas as pd # importa o módulo pandas e o renomeia para "pd"

#################################################################################################

## Estruturas de dados de pilha (stack) e fila (queue);
# Em termos de programação, colocar um item no topo da pilha é chamado de push e remover um item é chamado de pop 
stack = [] # cria uma lista vazia para representar a pilha

# Push
stack.append('A')
stack.append('B')
stack.append('C')

print("Stack: ", stack)

Stack: ['A', 'B', 'C'] # imprime a pilha

############################

# As operações básicas que podemos fazer em uma pilha são:​
# Push: Adiciona um novo elemento na pilha.​
# Pop: remove e retorna o elemento do topo da pilha.​
# Peek: Retorna o primeiro (último) elemento da pilha.​
# isEmpty: Verifica se a pilha está vazia.​
# Size: Encontra o número de elementos na pilha.

############################

# Encontrar um elemento;
topElement = stack[-1]
print("Peek: ", topElement)

Peek: C

poppedElement = stack.pop()
print("Pop: ", poppedElement)

Pop: C

print("Stack after Pop: ", stack)

############################

# criando uma pilha usando uma classe;
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()

print(s.isEmpty())

s.push(4)

s.push('dog')

print(s.peek())

s.push(True)

print(s.size())

print(s.isEmpty())

s.push(8.4)

print(s.pop())

print(s.pop())

print(s.size())

# Ficará assim no terminal:
# True
# dog
# 4
# False
# 8.4

#################################################################################################

# Estruturas Dinâmicas em Python​;
# List (lista): tamanho flexível, permite inserções e remoções.​
# Dict (dicionário): armazenamento chave-valor.​
# Classes personalizadas: permitem criar estruturas como listas encadeadas, árvores, etc.​


# Listas Encadeadas – Exemplo de Alocação Dinâmica​
# Conceito:​

# Cada elemento é um nó (Node).​

# Cada nó guarda um valor e a referência (ponteiro) para o próximo nó
# Definição do Nó​

class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# Alocação Estática: memória definida antes da execução .​
# Alocação Dinâmica: memória alocada em tempo de execução → flexível e adaptável.​
# Em Python, o interpretador gerencia a memória.​

# Existe coletor de lixo (garbage collector) para liberar memória automaticamente.

# Alocação estática (simulação com lista fixa)​
array = [0] * 5
print(array)

# Ficará assim no terminal:
# [0, 0, 0, 0, 0]

# Alocação dinâmica (expansível)​
lista = []

lista.append(10)

lista.append(20)

print(lista)

# Ficará assim no terminal:
# [10, 20]

############################

# Lista Encadeada​

class ListaEncadeada:

    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, dado):
        novo = No(dado)
        novo.proximo = self.cabeca
        self.cabeca = novo

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual and atual.dado != valor:
            anterior = atual
            atual = atual.proximo
        if not atual:
            return False
        if anterior:
            anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo
        return True

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


#################################################################################################

## Exercício de fatorial;

# implementar fatorial recursivo com intereção.
def fatorial(n):
    if n == 0 or n == 1: # Caso base
        return 1
    return n * fatorial(n - 1) # Passo recursivo

# implementar fatorial iterativo
def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(fatorial(5)) # 120
print(fatorial_iterativo(5)) # 120

# Ficará assim no terminal:
# 120
# 120

#################################################################################################

## Exercício de Fibonacci;

# Fibonacci recursivo com intereção com usuário
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Digite um número para calcular o Fibonacci: "))
print("Fibonacci:", fibonacci(n))

############################

# Fibonacci iterativo com intereção com usuário
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("Digite um número para calcular o Fibonacci: "))
print("Fibonacci:", fibonacci_iterativo(n))


# Ficará assim no terminal:
# Digite um número para calcular o Fibonacci: (digitei 6)
# Fibonacci: 8
# Digite um número para calcular o Fibonacci: (digitei 6)
# Fibonacci: 8

#################################################################################################

## Para passarmos um código do Github (já conectado) a plataforma que estou gerando algoritmos, 
## utilizamos esta função no terminal: 
git pull origin main 

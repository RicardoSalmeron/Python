#Funções
#Para organizar o código
#Para reaproveitamento
#Primo pobre do microservico
from openpyxl.styles.builtins import total


#Sintaxe
#def nome_funcao(parametros separados por vírgula)
#   instruções
#   return expressao

#Primeiro passo é a definicao da funcao
#Segundo passo é o uso

#Primeiro passo
def _olaMundo ():
    print("Olá Mundo")


#Segundo passo
_olaMundo()


#Função com parâmetros
#Definimos o parametro apenas dizendo o seu nome
#Não é necessário definir o tipo do parametro

def _soma(p1,p2):
    total = p1+p2
    print(total)

print("O total é:", end=" ")
_soma(5,6)

print("\nFunção com parâmetro e uso nomeado")
def _subtracao(p1,p2):
    total= p1-p2
    print(total)
print("Posicional")
print("O total é:", end=" ")
_subtracao(5,6)

print("Nomeado")
print("O total é:", end=" ")
_subtracao(p2=8, p1=5)


#Escopo
#No python e em qlqr linguagem há uma discussão sobre escopo
#O escopo é a visibilidade da variável
#Existem variáveis de escopo GLOBAL e variáveis de escopo LOCAL
#Escopo GLOBAL as variáveis são definidas no programa principal
clima= 'inverno' #O clima é de escopo global
def _mostraClima():
#Percebemos que mesmo dentro da função conseguimos acessar o valor da variável "clima"
    print(f'O clima de hoje é de {clima}')

_mostraClima()

#A única regra é que a variável global não pode estar definida depois da função
#Se chamarmos a função antes da definição da variável, a função não funciona

clima= 'inverno' #O clima é de escopo global
def _mostraClima():
    clima2= "verão"
#Percebemos que mesmo dentro da função conseguimos acessar o valor da variável "clima"
    print(f'O clima de hoje é de {clima}')

_mostraClima()

def _saudacao (nome):
    return "Bom dia" + nome + "!"

print(_saudacao("Francesco VIRGULLINI"))
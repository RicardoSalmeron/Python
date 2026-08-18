#Lambda
    #função anônima (pequena - de uma linha só - função inline)
#A criação da função está próxima do seu uso
#Versáteis 
#Cuidado que temos que ter, é NÃO RESOLVER TUDO COM LAMBIDA
#Programa ilegível com alto níveis de lambda

# def dobro(n:int) -> int :
#     return n * 2

#Transformar em Lambda
#sintaxe lambda <argumentos/parâmetros> : <expressão de retorno>
#Lambda sempre tem return
dobro = lambda n : n*2

#Uso mais comum

print((lambda n: n*2) (69))

#Lambda condicional 
#Tem if imbutido

#função que decide qual o maior de 2 números
# def maior(x:int,y:int)->int:
#     if x > y:
#         return x
#     else: return y

# lambda x,y: x if x > y else y
# print((lambda x,y: x if x>y else y) (52, 89))

#Pode utilizar print dentro do lambda
#Sim, porém com cuidado

# lmenor = lambda x,y: print(x) if x< y else print(y)
# xpto = lmenor(9,65)
# print(lmenor(9,65))

# lmenor2 = lambda x,y: \
#     f'ente {x} e {y} o menor é {x}' \
#     if x < y else \
#     f'entre {x} e {y} o menor é {y}'
# print(lmenor2(8,20))

#Map é uma funcionalidade do python que permite aolicar uma função em todos os elementos de uma lista

def dobro (n:int)-> int:
    return n * 2
numeros = [7,87,90,-23,-4,0]

#Tradicional
dobrados = []
for n in numeros:
    dobrados.append(dobro(n))


#Com o map
#Sintaxe map(função, iteravel)

print(list(map(dobro, numeros)))
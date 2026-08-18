from functools import reduce

#ex 1
dobro = lambda x: x*2
#ex 2
par_ou_impar = lambda  x : f'{x} é par' if x % 2 == 0 else f"{x} é ímpar"






#ex 3
precos = [100.0, 250.0, 39.90]

# desconto = lambda preco: preco*0.9
map((lambda preco: preco*0.9), precos)
#ex 4
nomes = ["ana", "bruno", 'carla']
def para_maiuscula (nomes:str)->str:
    return nomes.upper()

print(list(map(para_maiuscula, nomes)))


#ex 5
numeros = [2,3,4,5]
print(reduce((lambda x, y: x if x> y else y ), numeros))
#ex 6
lista_quadrados=[i**2 for i in range (1,11)]
print(lista_quadrados)
#ex 7
numeros = [3,8,15,22,7,40,11]
lista_pares=[i for i in numeros if i%2==0]
#ex 8
numeros2 = [3,8,15,22,7]
lista_par_impar=["par" if i%2==0  else "impar" for i in numeros]
#ex 9
NOME, PRECO, ESTOQUE = 0, 1, 2
produtos = [
["Caderno", 12.50, 5],
["Caneta", 2.30, 100],
["Mochila", 89.90, 3],
["Estojo", 15.00, 8],
]
menores_que_10=[produto[NOME] for produto in produtos if produto[ESTOQUE] < 10]

#ex 10
precos = [100.0, 250.0, 39.90]
descontos =[0.1,0.2,0.05]

precos_descontados=list(map((lambda descontos,precos: round(precos*(1-descontos),2)),precos,descontos))

#Exercício 1
notas = (7.5, 8.0, 6.5, 9.0)
print(f"A 1ª nota é: {notas[0]}")
print(f"A última nota: {notas[-1]}")

#Exercício 2
numeros = (12, 45, 7, 23, 9, 31)
soma = 0
for i in numeros:
    soma +=i
print(soma)

#Exercício 3 
def contar_pares (numeros: tuple)-> int:
    pares = 0
    for i in numeros:
        if i%2==0:
            pares+=1
    print(pares)

contar_pares((1, 2, 3, 4, 5))

#Exercício 4
produtos_loja1 = ("Caneta", "Caderno", "Mochila")
produtos_loja2 = ("Estojo", "Régua")
todos_produtos = produtos_loja1 + produtos_loja2
print(todos_produtos)

#Exercício 5
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
a = tupla[0:4] 
b = tupla[len(tupla)-3: len(tupla) ]
c = tupla[::1]
print(a,b,c)

#Exercício 6 
def calcular_maior_menor (numeros:tuple)->tuple:
    maior = 0
    menor = numeros[0]
    for numero in numeros:
        if numero< menor:
            menor = numero
        if numero > maior:
            maior = numero
    return(menor, maior)

print(calcular_maior_menor((1,2,3,4,5,6)))

#Exercício 7
lista_nomes = ["Ana", "Bruno", "Carla"]
tupla_nomes = tuple(lista_nomes)
temp = list(tupla_nomes)
temp.append("Diego")
tupla_nomes2= tuple(temp)
print(tupla_nomes2)
del temp

#Exercício 8
notas = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0))
def media_aluno(notas, indice_aluno):
    soma = 0
    for nota in notas[indice_aluno]:
        soma += nota
    media = soma/len(notas[indice_aluno])
    return round(media,2)
print(media_aluno(notas, 0))
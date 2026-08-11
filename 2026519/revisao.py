import random

minhaLista= ["café", "açúcar","água"]
print(minhaLista)

print(f"Primeiro elemento: {minhaLista[0]}")
print(f"Último elemento (indíce negativo): {minhaLista[-1]}")
print(f"Último elemento (indíce positivo): {minhaLista[2]}")
print("\n\n")

minhaLista= ["café", "açúcar","água", "chantily", "canela"]
print(minhaLista)
#slicing
#Sintaxe lista[inicio:fim-1:pulo]
parteLista= minhaLista[2:4+1]
print(f"parte a lista {parteLista}")

print(f"Equivale a fazer sem o final: {minhaLista[2:]}")
print(f"Equivale no lado negativo: {minhaLista[-3:]}")
print(f"Invertendo: {minhaLista[3:1-1:-1]}")
print(f"pulando: {minhaLista[0::2]}")

#juntar duas listas
complementos = ["raspas de limão"]
minhaLista = minhaLista + complementos
print(minhaLista)

maiselementos = ["pimenta"]
minhaLista.extend(maiselementos)
print(minhaLista)

print("\nAleterando um elemento")
minhaLista[5]="raspas de laranja"
print(minhaLista)
#Inclusao
print('\nIncluindo')
print('append - insere no final')
minhaLista.append('gengibre')
print(minhaLista)
print('insert - insere em uma posicao 3')
minhaLista.insert(3, 'chocolate em po')
print(minhaLista)
#Exclusao
minhaLista.pop()
print(minhaLista)
minhaLista.pop(3)
print(minhaLista)
del minhaLista
#Sort
minhaLista =["café","açúcar","água","chantilly","canela","raspas de limão"]
print(minhaLista)
minhaLista.sort()
print(minhaLista)

teste = ["água","açúcar","canela","chantilly","pimenta","raspas de laranja"]
print(teste)
print(f"tamanho: {len(teste)}")
aleatorio=[]
indices_sorteados=[]
while len(aleatorio) != len(teste):
    indice_sorteado=random.randint(0,6)
    if indice_sorteado not in indices_sorteados:
        aleatorio.append(teste[indice_sorteado])
    indices_sorteados.append(indice_sorteado)
print(aleatorio)

matriz = [[0,1,2],[3,4,5]]
print(matriz)
matriz[0][2] = 8
print(matriz)

for linha in matriz:
    for coluna in linha:
        print(coluna)
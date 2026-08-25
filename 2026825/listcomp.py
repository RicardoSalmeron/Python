print('Revisão Map')
def dobro (n:int)->int:
    return n*2
numeros = [7, 87, 90, -23, 4, 0]

numeros_dobrados = print(list(map(dobro, numeros)))
print(numeros_dobrados)

def mult (n:int, m:int) ->int:
    return n * m 

numeros =[7, 87, 90, -23, 4, 0]
multiplicadores = [2, 3, 4, 5, 6, 7]

multiplicados=(list(map(mult, numeros, multiplicadores)))
print(multiplicados)

multiplicados2 = list(map((lambda m, n : n*m), numeros, multiplicadores))
print(multiplicados2)

print("\nList Comprehension")

#Lista Comprehension
#feito para simplificar o map
#retorna uma lista
numeros = [7, 87, 90, -23, 4, 0]
dobrados = []
for n in numeros:
    dobrados.append(n*2)

print(dobrados)

dobrads = [n*2 for n in numeros]
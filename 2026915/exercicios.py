from functools import reduce

# Exercício 1

# arqNum = open('numeros.txt', 'w')

# for i in range(10):
#     num = int(input("Informe um número: "))
#     arqNum.write(f'{str(num)}\n')

# Exercício 2


# arqNum = open('numeros.txt', 'r')
# numeros = arqNum.readlines()
# soma = 0
# for num in numeros:
#     soma += int(num)

# print(soma)

# Exercício 3

# arqTXT = open('arquivo.txt', 'w')
# i = input("Digtie a informação desejada: ")
# while i !="0":
#     i = input("Digtie a informação desejada: ")
#     arqTXT.write(f"{i}\n")
 
# Exercício 4

# arqPares = open('arquivoPares.txt', 'w')
# arqImpares = open('arquivoImpares.txt', 'w')
# i = True
# while True:
#     if i == 0:
#             break
#     else:
#         i = int(input("Digtie o número desejado: "))
#         if i % 2 == 0:
#             arqPares.write(f"{str(i)}\n")
#         else:
#             arqImpares.write(f"{str(i)}\n")
        

# Exercício 5

# arqPares = open('arquivoPares.txt', 'r')
# arqImpares = open('arquivoImpares.txt', 'r')
# arqOdernado = open('numerosOrdenados.txr', 'w')
# listaUm = [int(x) for x in arqPares.readlines() + arqImpares.readlines()]
# listaOrdenada = listaUm.sort()
# arqOdernado.write(f'{listaUm}')

# Exercício 6

# arqNotas = open('notas.txt', 'r')
# for linha in arqNotas.readlines():
#     notas = linha.split(',')
#     media = (reduce(lambda a, b: float(a) + float(b), notas[2:])/len(notas[2:]))
#     print(f'Média do Aluno {notas[1]} RM({notas[0]}): {media:.2f}')

# Exercício Complementar 1

# arqIP = open('ips.txt', 'r').readlines()
# ips_unicos = set(arqIP)
# arqIP_unicos = open('ipsUnicos.txt', 'w')
# arqIP_unicos.write(f'{ips_unicos}')

# Exercício Complementar 2

# arqAprovados = open('aprovados.txt', 'w')
# arqReprovados = open('reprovados.txt', 'w')
# arqNotas = open('notas.txt', 'r')
# for linha in arqNotas.readlines():
#     notas = linha.split(',')
#     media = (reduce(lambda a, b: float(a) + float(b), notas[2:])/len(notas[2:]))
#     if media >= 6:
#         arqAprovados.write(f"Aluno {notas[1]} RM({notas[0]}): {round(media,2)}")
#     else:
#         arqReprovados.write(f"Aluno {notas[1]} RM({notas[0]}): {round(media,2)}")


# Exercício Complementar 3

# arqFoods = open("foods.txt", 'r')
# comidas = [linha.split(',')[2].strip() for linha in arqFoods]
# comidasUnicas = set(comidas)

# maior = 0
# maior_nome = ''
# for comida in comidasUnicas:
#     if comidas.count(comida) > maior:
#         maior = comidas.count(comida)
#         maior_nome = comida

# print(f'A comida preferida pela maioria das pessoas é {maior_nome}')

# Exercício Complementar 4

arqRace = open("race.txt", 'r')
lista_consumo = [float(coluna.split(',')[4].strip()) for coluna in arqRace]
media_consumo = (reduce(lambda a, b: float(a) + float(b), lista_consumo)/len(lista_consumo))
print(f'A média de consumo de energia é de {media_consumo:.2f}kWh.')

arqRace.seek(0)
menor_consumo = min(lista_consumo)
menor_consumo_piloto = arqRace.readlines()[lista_consumo.index(menor_consumo)].split(',')[0].strip()
print(f'O piloto com o menor consumo de energia é {menor_consumo_piloto}.')

arqRace.seek(0)
lista_tempo = [float(coluna.split(',')[2].strip()) for coluna in arqRace]
maior_tempo = max(lista_tempo)
arqRace.seek(0)
maior_tempo_piloto = arqRace.readlines()[lista_tempo.index(maior_tempo)].split(',')[0].strip()
print(f'O piloto com o maior tempo de volta é {maior_tempo_piloto}.')
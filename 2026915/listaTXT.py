from functools import reduce

def adicionarTexto(arquivo, texto):
    arquivoTxt = open(arquivo, 'a')
    
    arquivoTxt.write(f'{texto}\n')

# Exercício 1
# arqNum = open('numeros.txt', 'w')

# try:
#     for i in range (10):
#         num = int(input(f"Informe o {i + 1}º número: "))
#         arqNum.write(f'{str(num)}\n')
#     arqNum.close()
# except ValueError:
#     print("Informe um número inteiro.")
# except Exception as erro:
#     print(f'Ocorreu um erro na linha {erro}')
    
# Exercício 2
# arqNum = open('numeros.txt', 'r')
# numeros = arqNum.readlines()
# soma = 0

# for num in numeros:
#     soma += int(num)

# print(soma)

# Exercício 3
# arqTxt = open('arquivo.txt', 'w')

# while True:
#     texto = input("Insira um texto. Caso queira encerrar o programa, digite 0: ")
    
#     if texto == "0":
#         break
    
#     adicionarTexto('arquivo.txt', f'{texto}')
    
# Exercício 4
# pares = open('pares.txt', 'w')
# impares = open('impares.txt', 'w')
# while True:
#     num = int(input("Infome um número (0 Encerra o programa.): "))
    
#     if num == 0:
#         break
    
#     if num % 2 == 0:
#         adicionarTexto('pares.txt', str(num))
#     else:
#         adicionarTexto('impares.txt', str(num))

# Exercício 5
# pares = open('pares.txt', 'r')
# impares = open('impares.txt', 'r')
# numeros_ordenados = open('numeros_ordenados.txt', 'w')

# listaNum = pares.readlines() + impares.readlines()
# listaNum.sort()

# for num in listaNum:
#     adicionarTexto('numeros_ordenados.txt', int(num))
    
# Exercício 6
# arqNotas = open('notas.txt', 'r')

# for linha in arqNotas.readlines():
#     notas = linha.split(',')
#     media = (float(notas[2]) + float(notas[3]) + float(notas[4]) + float(notas[5]))/4
#     print(f'Média do Aluno {notas[1]} RM({notas[0]}): {media:.2f}')

# Exercício Complementar 1
# arqIpsUnicos = open('ips_unicos.txt', 'w')
# listaIp = open('ips.txt', 'r').readlines()
# listaIpsUnicos = []

# for ip in listaIp:
#     if ip not in listaIpsUnicos:
#         listaIpsUnicos.append(ip.replace('\n', ''))
#         adicionarTexto('ips_unicos.txt', ip)

# Exercício Complementar 2
# arqNotas = open('notas.txt', 'r')
# arqAprovados = open('aprovados.txt', 'w')
# arqReprovados = open('reprovados.txt', 'w')

# for linha in arqNotas.readlines():
#     notas = linha.split(',')
#     media = (float(notas[2]) + float(notas[3]) + float(notas[4]) + float(notas[5]))/4
    
#     if media >= 6:
#         adicionarTexto('aprovados.txt', f'{notas[0]}, {notas[1]}, {round(media, 2)}')
#     else:
#         adicionarTexto('reprovados.txt', f'{notas[0]}, {notas[1]}, {round(media, 2)}')

# Exercício Complementar 3
# arqComidas = open('foods.txt', 'r')
# comidas = [linha.split(',')[2].strip() for linha in arqComidas]
# comidasUnicas = []

# for comida in comidas:
#     if comida not in comidasUnicas:
#         comidasUnicas.append(comida)

# maior = 0
# maior_nome = ''
# for comida in comidasUnicas:
#     if comidas.count(comida) > maior:
#         maior = comidas.count(comida)
#         maior_nome = comida

# print(f'A comida preferida pela maioria das pessoas é {maior_nome}')

# Exercício Complementar 4
arqCorridas = open('race.txt', 'r')
lista_consumo = [float(coluna.split(',')[4].strip()) for coluna in arqCorridas]
media_consumo = (reduce(lambda a, b: float(a) + float(b), lista_consumo)/len(lista_consumo))
print(f'A média de consumo de energia é de {media_consumo:.2f}kWh.')

arqCorridas.seek(0)
menor_consumo = min(lista_consumo)
menor_consumo_piloto = arqCorridas.readlines()[lista_consumo.index(menor_consumo)].split(',')[0].strip()
print(f'O piloto com o menor consumo de energia é {menor_consumo_piloto}.')

arqCorridas.seek(0)
lista_tempo = [float(coluna.split(',')[2].strip()) for coluna in arqCorridas]
maior_tempo = max(lista_tempo)
arqCorridas.seek(0)
maior_tempo_piloto = arqCorridas.readlines()[lista_tempo.index(maior_tempo)].split(',')[0].strip()
print(f'O piloto com o maior tempo de volta é {maior_tempo_piloto}.')
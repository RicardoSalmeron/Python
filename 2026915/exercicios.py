#Exercício 1

# arqNum = open('numeros.txt', 'w')

# for i in range(10):
#     num = int(input("Informe um número: "))
#     arqNum.write(f'{str(num)}\n')

#Exercício 2


# arqNum = open('numeros.txt', 'r')
# numeros = arqNum.readlines()
# soma = 0
# for num in numeros:
#     soma += int(num)

# print(soma)

#Exercício 3

# arqTXT = open('arquivo.txt', 'w')
# i = input("Digtie a informação desejada: ")
# while i !="0":
#     i = input("Digtie a informação desejada: ")
#     arqTXT.write(f"{i}\n")

#Exercício 4

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
        

# #Exercício 5

# arqPares = open('arquivoPares.txt', 'r')
# arqImpares = open('arquivoImpares.txt', 'r')
# arqOdernado = open('numerosOrdenados.txr', 'w')
# listaUm = [int(x) for x in arqPares.readlines() + arqImpares.readlines()]
# listaOrdenada = listaUm.sort()
# arqOdernado.write(f'{listaUm}')

#Exercício 6


15 a
12 b
21
21
210
362
55
31231

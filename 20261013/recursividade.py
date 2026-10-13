#Recyrsividade é a estrategia de quebrar um problema em partes menores até um problema conhecido
#EX 5! =>5x4!; 4!=> 4x3!; 3!=> 3x2!; 2!= 2x1!; 1!=> 1x0!; 0!=1
#0! condição base

def fatorial(n):
    if n ==0:
        return 1
    else:
        return n*(fatorial(n-1))

#Somar os elementos de uma lista
#Fazer uma função recursiva

lista = [3,5,678,3,78,90]
# def soma_lista_sem_recursao(lista):
#     total =0
#     for elemento in lista:
#         total +=elemento
#     return total
# print(soma_lista_sem_recursao(lista))


def soma_lista_recursao(lista):
    if len(lista) ==0:
        return 0
    else:
        return lista[0] + soma_lista_recursao(lista[1:])
print(soma_lista_recursao(lista))


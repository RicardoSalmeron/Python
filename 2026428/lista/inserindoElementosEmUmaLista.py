titulo="Cadastro de uma lista"
print(f"{titulo:^30}")

#lista vazia
numeros= []
#cadastro com while True / break
while True:
    n = int(input("Informe um número ou zero para sair: "))
    if n == 0:
        break
    numeros.append(n)
    print(numeros)
    #Imprimir a coleção com os elementos lado a lado
    for item in numeros:
        print(item, end= ", ")
        print('\b\b')
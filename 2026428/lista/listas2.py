minhaLista= [] #Lista

#Acrescentar valores na lista
#Append
minhaLista.append("Café")

#Lista permite elementos heterogeneos
minhaLista.append(12)

print(minhaLista)

#Recuperando um valor de uma determinada posição
print(f'segundo elemento: {minhaLista[1]}')

#Juntando duas listas (com extend)
complemento = ["açúcar","água quente","canela"]
print("\n")
print(complemento)

#Aqui acrescenta os elementps da lista "complemento" para a lista na "minhaLista"
minhaLista.extend(complemento)
print(minhaLista)

#Localizando um elemento pelo indice e recuperando o indice
print(f"A água quente está na posição: {minhaLista.index("água quente")}")

#apagando um elemento
#através do indice
minhaLista.pop(3) #indice da água quente
print(minhaLista)

#remover pelo próprio elemento
minhaLista.remove(12) #aqui é o elemento "12" e não o indice
print(minhaLista)

#Alterando o conteúdo de um elemento

minhaLista[0]= "cafe"
print(minhaLista)

#tentando acessar um indice que não existe
#print(minhaLista[5])

#inserindo um elemento em uma determinada posição
#['cafe','açúcar','canela']
#['cafe','açúcar','chantilly','canela']
minhaLista.insert(2,'chantilly')
print(minhaLista)

#ordenação da lista
#dois tipos de ordenação
#ordenação que é uma função nativa do python
#ordenação da propria classe list
#o que elas diferem?

print("\n Ordenação com função nativa do python")
print(minhaLista)
print(sorted(minhaLista)) #Troca a ordem temporiariamente
print('\n')
print(minhaLista)
print("\n Ordenação com função nativa do python")
print(minhaLista)
minhaLista.sort() #Troca a ordem permanentemente
print(minhaLista)

print('\n Com números')
meusNumeros = [1, 4, 6, 0, 0, 0, 0, 23, -1, 8, 0, 76, 2]
print(meusNumeros)
print("Ordenando temporariamente so para a impressão com o SORTED")
print(sorted(meusNumeros))
print("Ordenando para todod sempre com o .sort")
meusNumeros.sort()
print(meusNumeros)
print("Ordenando para todo sempre INVERSO com o .sort")
meusNumeros.sort(reverse=True)
print(meusNumeros)
meusNumeros=[1, 4, 6, 23, 0, -1, 8, 0, 76, 0, 2]
print(meusNumeros)
print(f'Qtos zeros tem na lista: {meusNumeros.count(0)}')
print(f'Onde esta o primeiro zero na lista: {meusNumeros.index(0)}')
print(f'Onde esta o segundo zero na lista: {meusNumeros.index(0, meusNumeros.index(0)+1)}')


#tamanho
print(f"Tamanho dos meusNumeros: {len(meusNumeros)}")
#min
print(f'Mínimo dos meusNumeros: {min(meusNumeros)}')
#max
print(f'Máximo dos meusNumeros: {max(meusNumeros)}')



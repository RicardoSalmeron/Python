#Coleções (variáveis de memória que possuem múltiplos valores,
# cada valor é chamado de item (ou elemento) que podem ser do msm tipo de dado
# ou tipos diferentes: homogeneas ou heterogeneas respectivamente
# TODA coleção é um elemento ITERAVEL
# significa que pode ir de um em um que é percorrível
#Há vários tipos de coleções: LISTAS, CONJUNTOS(SET), TUPLAS, DICIONÁRIOS(FORMULÁRIO), chave/valor

#Lista
#Características
#poderosa, flexível, perfomática, conjunto de comandos para manipulação completas
'''
MUTÁVEL: depois de criada, a lista permite acressentar, retirar, modificar elementos
EXPANSÍVEL: pode aumentar o seu conjunto de dados a partir de outra lista
ACEITA TIPOS DIFERENTES DE DADOS
IDEXADA: cada elemento tem uma POSIÇÃO dentro da LISTA
PERMITE DUPLICADOS
ORDENÁVEIS --> a ordenação natural só acontece se todos os elementos forem do msm tipo
SÍMBOLO: []
'''

titulo = 'Listas'
print(f"{titulo:^30}")
minhaLista=["café", "água","açúcar"]
print(minhaLista)

#E se eu quisesse imprimir somente o café
#Entender como acessar cada elemento pelo índice
#Toda coleção idexada começa no zero
#podemos acessar os indices de trás para frente com números negativos  começando por -1 no último indice
minhaLista=["café", "água","açúcar", "canela", "café"]
print(f'primeiro elemento: {minhaLista[0]}')
print(f'segundo elemento: {minhaLista[1]}')
print(f"tamanho da lista:{len(minhaLista)}")
print(f'o último elemento: {minhaLista[4]}')


print(f'o último elemento: {minhaLista[-1]}')
print(f'primeiro elemento: {minhaLista[-5]}')



#tentando acessar im indice que n existe (erro de indice)

#como acrescentar itens numa lista
#o método append faz isso
print('\n')
print(minhaLista)
minhaLista.append("chantily")
minhaLista.append("especiarias")
print(minhaLista)

#para remover itens da lista
#usamos o método pop
#ele sem parametro remove do FIM da lista
minhaLista.pop()
print(minhaLista)
#posso remover itens expecíficos com o pop
#basta colocar o indice
minhaLista.pop(2)
print(minhaLista)

#TODO ELEMENTO ITERÁVEL podemos percorrer atráves do FOR
print("Elementos um a um")
for item in minhaLista:
    print(item)
print('\n')
#percorrendo a lista pelos INDICES da lista
for i in  range(len(minhaLista)):
    print(minhaLista[i])
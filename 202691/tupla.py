#Tupla
#é também uma coleção
#ela é IMUTÁVEL: Gabriela - nasce e morre do mesmo jeito
#para ser uma tupla deve conter uma vírgula


print("Tupla")
minhaTupla= ("sol", "água", "natureza")
print(minhaTupla)

print("\nTipos de dados diferentes")
outraTupla= tuple(("a",45, True))
print(type(outraTupla))

print("\nAcessando pela posição")
print("1ª posição: {minhaTupla[0]}")
print("2ª posição: {minhaTupla[1]}")
print("Última posição: {minhaTupla[-1]}")

print("\nPegadinha 1")
tuplaVazia = ()
print(tuplaVazia)

print("\nPegadinha 2")
tuplaUmFalsa = ("sol")
print(tuplaUmFalsa)
print(type(tuplaUmFalsa))


tuplaUm = ("sol",)
print(tuplaUm)
print(type(tuplaUm))

print("\nAchando a posição de um elemento")
minhaTupla = ("sol", "água", "natureza", "sol")
print(minhaTupla)
print(f"A água está na posição: {minhaTupla.index("água")}")
print(f"O sol está na posição: {minhaTupla.index("sol")}")
print(f"O próximo sol está na posição: {minhaTupla.index("sol", 1)}")

minhaTupla = ("sol", "água", "natureza", "sol", "sol", "lago","sol")
print(f"O 1º sol está na posição: {minhaTupla.index("sol")}")
print(f"O 2º sol está na posição: {minhaTupla.index("sol", minhaTupla.index("sol") + 1)}")
print(f"O 3º sol está na posição: {minhaTupla.index("sol", minhaTupla.index("sol")+1)+1}")

print("\nPercorrendo a coleção toda")
minhaTupla = ("sol", "água", "natureza", "sol", "sol", "lago","sol")
print(minhaTupla)
for item in minhaTupla:
    print(item)

print('\nAchando as posições dos sóis')
for indice, item in enumerate(minhaTupla):
    if item == "sol":
        print(f"Posição {indice+1}: {minhaTupla[indice]}")

print("\nMatriz de Tuplas")
matrizTupla = (("café", "banho"),("almoço", "academia"), ("aula","series"))
print(matrizTupla)
print(matrizTupla[2][1])

#unpacking - atribuição múltipla 
pessoa = ("Otário", "Solteiro", 18)
nome, estado_civil, idade = pessoa
print(nome)
print(estado_civil)
print(idade)

print("\nConverção para gambiarra")
minhaTupla = ("sol", "água", "natureza", "sol", "sol", "lago","sol")
print(minhaTupla)
temp = list(minhaTupla)
minhaTupla.append("chuva")
print(type(temp))
minhaTupla = tuple(temp)
print(minhaTupla)
del temp
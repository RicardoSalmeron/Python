#Dicionários são coleções do tipo formulário
#chave:valor
#Exemplo
#Nome: Ricardo
#Idade : 18
#Sexo : Masculino
#Não São Posicionais - não tem indice
#Permitem tipo de dados diferentes
#Permitem valores repitidos, porém chaves São Únicas
#Permitem inclusão, alteração, exclusão, São Mutáveis
#Símbolo {}


aluno = {'nome':'Ricardo', "Idade":18, "Sexo":"Masculino"}
# print(aluno)
# print(aluno['nome'])
# print(aluno["Idade"])
# print(aluno["Sexo"])
# print(type(aluno))


#Dicionário vazio
vazio = {}
# print(vazio)

vazio["categoria"] = "Brinquedos"
# print(vazio)

aluno["profissão"] = "Estagiário"
# print(aluno)

aluno["nome"] = "CCDC"
aluno["Idade"] = 5
# print(aluno)
print(aluno.get("nome"))
aluno.update({"idade":55})
# print(aluno)


aluno.pop("nome")
# print(aluno) #Elimina chave
aluno.popitem() #Elimina o último
# print(aluno)
del aluno["Sexo"] #Elimina chave
# print(aluno)

aluno.clear()
# print(aluno)

#Troca de chave só acontece com a exclusão e criação de chave

aluno = {'nome':'Ricardo', "Idade":18, "Sexo":"Masculino"}
for caracteristica in aluno: #Quando coloco apenas o nome do dicionário estou pegando apenas as chaves
    print(caracteristica)

for chaves in aluno.keys():
    print(chaves)

for valores in aluno.values():
    print(valores)

for chave in aluno:
    print(aluno[chave])

for item in aluno.items():
    print(item)

for chave,valor in aluno.items():
    print(f"{chave} = {valor}")

#Atribuição múltipla
x, y, z = 0, 1, 2
print(f"{x}")
print(f"{y}")
print(f"{z}")

original = ["café", "pão", "leite"]
copiaFalsa = original
copia = original.copy()
print("l1", original)
print("l2", copiaFalsa)
copiaFalsa.append("cachorro")
copia.append("gato")
print("l1", original)
print("l2", copiaFalsa)
print(copia)

aluno = {'nome': 'CCDC', 'Idade': 5, 'Sexo': 'Masculino', 'profissão': 'Estagiário', 'idade': 55}

aluno2 = aluno.copy()
aluno2.update({"nome": "Teste"})
aluno2["Idade"] = 2
print (aluno2)
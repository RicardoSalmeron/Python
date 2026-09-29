#Pra tratar arquivos json o python tem uma biblioteca própria json

#Arquivos JSON são textos estruturados

pessoa = {'nome':"Augustinho Carrara", 'idade':"60", "hobbies":["taxista", "cozinheiro"]}
print(pessoa)

#A biblioteca JSON irá transformar o dicionário em um texto
#pq isso é interessante? Porque na hora de gravar um arquivo, nós precisamos de texto

import json
#método dumps da biblioteca json converte uma coleção em um texto
pessoa2=json.dumps(pessoa)
print(type(pessoa2))
print(pessoa2)

#O uso mais comum, no entanto é gravar essas informações em um arquivo
#O método agora muda de nome:dump

with open('pessoa.json','w',encoding='utf-8') as arqPessoas:
    json.dump(pessoa,arqPessoas)
    arqPessoas.write("\n")


with open('pessoa2.json','a',encoding='utf-8') as arqPessoas:
    json.dump(pessoa,arqPessoas,indent=4)
    arqPessoas.write("\n")

pessoaNova = {'nome':"Kid Bengala", 'idade':"69", "hobbies":["brincaderinhas", "libidgel"]}
pessoaNova2 = json.dumps(pessoaNova, indent=4, ensure_ascii=False)
print(type(pessoaNova2))
print(pessoaNova2)


with open('pessoa3.json','a',encoding='utf-8') as arqPessoas:
    json.dump(pessoaNova2,arqPessoas,indent=4)
    arqPessoas.write("\n")

#enquanto i dymps(str)/dump(arquivo) escreve no formato json
#o loads(str)load(arquivo) lê do formato JSON e coloca em uma coleção

pessoaTexto = '{"nome":"Antônio", "hobbies":["Aeromodelismo", "Board Games"]}'
print(type(pessoaTexto))
print(pessoaTexto)
#o metodo LOADS tranforma essa string em uma coleção
pessoaDicionario = json.loads(pessoaTexto)
print(type(pessoaDicionario))
print(pessoaDicionario)

#como ler de um arquivo? método load

with open("pessoa.json", 'r', encoding="utf-8") as arqPessoas:
    aluno = json.load(arqPessoas)
    print(type(aluno))
    print(aluno)

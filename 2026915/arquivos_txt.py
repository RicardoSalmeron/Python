#Muitas vezes precisamos acessar o conteúdo de um arquivo no file system
#Alguns tipos de arquivo o python lê naturalmente, outros ele precise de 
#Bibliotecas especializadas
#o arquivo textp é natural do python


#Para acessar um arquivo precisamos informaro ao SO que vamos manipular o arquivo
#Isso é feito através do OPEN / CLOSE
arqAlunos = open('alunos.txt', 'r')
# print(arqAlunos.readline(), end = '')
# print(arqAlunos.readline(), end = '')
# print(arqAlunos.readline(), end = '')
# print(arqAlunos.readline(), end = '')

#O texto que estou lendo do arquibo é um elemento iterável
# for linha in arqAlunos:
#     print(linha, end='')

# arqAlunos.seek(0)
# print(arqAlunos.readline(),end='')

listaLinhas = arqAlunos.readlines()
# print(listaLinhas)

# desafio: usando list comprehension, tirar '\n' dos elementos da lista 
listaAtualizada = {linha.replace('\n','') for linha in listaLinhas}
print(listaAtualizada)

arqOlaMundo = open('arquivoOlaMundo.txt', 'w')
arqOlaMundo.write("Ola Mundo")
arqOlaMundo.close
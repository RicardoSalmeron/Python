maiorQueAMedia=[]
listaNotas=[]

while True :
    nota = float(input("Insira suas notas: "))
    if nota<0:
        break
    listaNotas.append(nota)
print(listaNotas)
soma= sum(listaNotas)
media = soma / len(listaNotas)
for elemento in listaNotas:
    if elemento > media:
        maiorQueAMedia.append(elemento)

print(f"Listas de notas: {listaNotas}, soma: {soma}, média: {media}, notas maiores que a média: {maiorQueAMedia}")

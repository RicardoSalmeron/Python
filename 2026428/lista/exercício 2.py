from statistics import median

i=0
listaNumeros=[]
while i<10:
    if i<10 :
        n=int(input("Digite números: "))
        listaNumeros.append(n)
        soma= sum(listaNumeros)
        media= soma/10
        print(f"Média: {media}, soma: {soma}")
        i=i+1
    else:
        break
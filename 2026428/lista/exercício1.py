i=0
numerosPares=[]
numerosImpares=[]
while True:
    n = int(input("Informe um número: "))
    if i<10:
        if n%2 ==0:

            numerosPares.append(n)
            listaPar=[numerosPares]
        else:
            numerosImpares.append(n)
            listaImpar=[numerosImpares]
    i= i+1
    if i>10:
        break
print(f"Lista par: {listaPar}, Lista ímpar: {listaImpar}")
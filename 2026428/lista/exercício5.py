lista=[1,2,3,4,5,6,7,8,9,10]
numero=int(input("Digite um número inteiro: "))
quant=0
for i in lista:
    if i== numero:
        quant=quant+1

print(f"O número informado aparece {quant} vezes na lista")
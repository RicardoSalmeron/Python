maiorNum=0
menorNum=0
for i in range(10):
    n=int(input("Informe um número: "))
    if n>maiorNum:
        maiorNum = n
    if n<menorNum or i==0:
        menorNum=n

print(f"O maior número é: {maiorNum}, o menor é: {menorNum}")

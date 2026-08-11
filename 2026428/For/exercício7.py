num=int(input("Digite um número inteiro: "))

for elemento in range(1, num+1):
    if num%elemento ==0:
        print(f"{elemento}")
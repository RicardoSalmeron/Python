num = int(input("Informe um número inteiro: "))
n1 = num//100
n2= (num//10)%10
n3= num%10
# % pega o resto da divisão
print(f"O número invertido é :{n1,n2,n3}")
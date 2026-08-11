num=int(input("Digite um número inteiro: "))
qntdiv=0
for elemento in range(1, num+1):
    if num%elemento ==0:
        qntdiv= qntdiv+1

if qntdiv > 2:
    print(f"Não é primo")
else:
    print("É primo")

primo=True

for i in range(1, num+1):
    if num % i ==0:
        if i !=1 and i != num:
            primo=False
if primo:
    print("É primo")
else:
    print("Né n")
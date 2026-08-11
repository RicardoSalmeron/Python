num1=int(input("Indique o valor da hora"))
num2=int(input("Indique o valor do minuto"))
if num1>24:
    print('inválido')
else:
    print(f"são{num1}horas")
if num2>59:
    print('inválido')
else:
    print(f"e {num2} minutos")
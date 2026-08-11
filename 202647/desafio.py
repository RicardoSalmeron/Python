num1=float(input("Indique um numero: "))
num2=float(input("Indique um numero: "))
print("Escolha o que deseja fazer: 1-soma| 2-subtração | 3-multiplicação | 4-divisão")
opcao=int(input("Escolha um numero de 1 até 4: "))

match opcao:
    case 1:
       print(f"O resultado da soma é {num1+num2}")
    case 2:
        print(f"O resultado da subtração é {num1 - num2}")
    case 3:
        print(f"O resultado da multiplicação é {num1 * num2}")
    case 4:
        print(f"O resultado da divisão é {num1 / num2}")